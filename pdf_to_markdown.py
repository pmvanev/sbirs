#!/usr/bin/env python3
"""
PDF to Markdown Converter

This script converts PDF files to Markdown format using PyMuPDF.
It processes all PDF files in the instructions/ directory and creates
corresponding .md files in the same directory.
For image-based PDFs, it attempts OCR using pytesseract.
"""

import os
import sys
import fitz  # PyMuPDF
import re
from pathlib import Path
from PIL import Image
import io

# Try to import OCR functionality
try:
    import pytesseract
    # Set tesseract path for Windows
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False
    print("Warning: pytesseract not available. OCR functionality disabled.")


def clean_text(text):
    """Clean and format extracted text for markdown."""
    # Remove excessive whitespace
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)

    # Fix common PDF extraction issues
    # Add space between camelCase
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    # Add space between word and number
    text = re.sub(r'(\w)(\d)', r'\1 \2', text)
    # Add space between number and capital letter
    text = re.sub(r'(\d)([A-Z])', r'\1 \2', text)

    # Clean up multiple spaces
    text = re.sub(r' +', ' ', text)

    # Remove trailing spaces from lines
    text = '\n'.join(line.rstrip() for line in text.split('\n'))

    return text


def extract_text_with_ocr(page):
    """Extract text from a page using OCR."""
    if not OCR_AVAILABLE:
        return ""

    try:
        # Convert page to image
        # 2x zoom for better OCR
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        img_data = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_data))

        # Perform OCR
        text = pytesseract.image_to_string(img, lang='eng')
        return text
    except Exception as e:
        print(f"OCR failed for page: {str(e)}")
        return ""


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file, with fallback to OCR for image-based PDFs."""
    try:
        doc = fitz.open(pdf_path)
        text_content = []
        pages_with_text = 0
        total_pages = len(doc)

        print(f"Processing {total_pages} pages...")

        for page_num in range(total_pages):
            page = doc.load_page(page_num)
            text = page.get_text()

            if text.strip():  # Page has extractable text
                pages_with_text += 1
                # Add page separator for multi-page documents
                if page_num > 0:
                    text_content.append(f"\n---\n**Page {page_num + 1}**\n")
                text_content.append(clean_text(text))
            else:
                # Try OCR for pages without extractable text
                print(
                    f"  Page {page_num + 1}: No extractable text, trying OCR...")
                ocr_text = extract_text_with_ocr(page)
                if ocr_text.strip():
                    if page_num > 0:
                        text_content.append(
                            f"\n---\n**Page {page_num + 1}** *(OCR)*\n")
                    text_content.append(clean_text(ocr_text))
                else:
                    print(
                        f"  Page {page_num + 1}: No text found via OCR either")

        doc.close()

        if pages_with_text == 0 and not text_content:
            print(f"Warning: No text could be extracted from {pdf_path}")
            if not OCR_AVAILABLE:
                print("Consider installing tesseract-ocr for image-based PDF support")
            return "No text could be extracted from this PDF. It may be image-based or protected."

        print(f"Successfully extracted text from {len(text_content)} pages")
        return '\n'.join(text_content)

    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return None


def convert_pdf_to_markdown(pdf_path, output_path):
    """Convert a single PDF file to Markdown."""
    print(f"Converting {pdf_path} to {output_path}...")

    # Extract text from PDF
    text_content = extract_text_from_pdf(pdf_path)

    if text_content is None:
        print(f"Failed to extract text from {pdf_path}")
        return False

    # Create markdown content
    pdf_name = Path(pdf_path).stem
    markdown_content = f"# {pdf_name}\n\n"
    markdown_content += f"*Converted from PDF: {Path(pdf_path).name}*\n\n"
    markdown_content += "---\n\n"
    markdown_content += text_content

    # Write to markdown file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Successfully created {output_path}")
        return True
    except Exception as e:
        print(f"Error writing to {output_path}: {str(e)}")
        return False


def main():
    """Main function to process all PDF files in the instructions directory."""
    instructions_dir = Path("instructions")

    if not instructions_dir.exists():
        print(f"Instructions directory not found: {instructions_dir}")
        return

    # Find all PDF files in the instructions directory
    pdf_files = list(instructions_dir.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in the instructions directory.")
        return

    print(f"Found {len(pdf_files)} PDF file(s) to convert:")
    for pdf_file in pdf_files:
        print(f"  - {pdf_file.name}")

    print("\nStarting conversion...")

    successful_conversions = 0

    for pdf_file in pdf_files:
        # Create output markdown file path
        md_file = pdf_file.with_suffix('.md')

        if convert_pdf_to_markdown(pdf_file, md_file):
            successful_conversions += 1

    print(f"\nConversion complete!")
    print(
        f"Successfully converted {successful_conversions} out of {len(pdf_files)} PDF files.")


if __name__ == "__main__":
    main()
