## References

1. "How US Space Command is preparing for satellite-on-satellite combat." The Economist, July 27, 2025.
   - Summary: Reporting indicates U.S. Space Command is preparing for co-orbital and on-orbit interference threats (jamming, dazzling, grappling, proximity ops) and rehearsing satellite-on-satellite contingencies. Themes include rapid attribution, rules of engagement that minimize debris, operating under comms/jamming, and accelerating decision timelines with automation.
   - Relevance to AIS: Underscores the solicitation’s need for onboard autonomy to detect, classify, and respond to threats when ground links are degraded; supports AIS aims to reduce kill-chain latency, enable autonomous collision avoidance/evasive maneuvers, and maintain mission under attack.

2. "Space Warfighting – A Framework for Planners." United States Space Force, April 10, 2025. PDF: https://www.spaceforce.mil/Portals/2/Documents/SAF_2025/Space_Warfighting_-_A_Framework_for_Planners_BLK2_(final_20250410).pdf
   - Summary: USSF doctrinal guidance describing the competition–contest–conflict continuum, the objective of space superiority, and mission areas including Space Domain Awareness (SDA), Defensive/Offensive Space Control, Battle Management/C2, and targeting. Emphasizes resilience, agility, and rapid, integrated kill chains across orbits.
   - Relevance to AIS: Provides authoritative language and mission alignment for AIS CONOPS. AIS deliverables (autonomy, resilient edge compute, sensor fusion, maneuver) map directly to doctrinal needs: persistent SDA, decision advantage with reduced timelines, and autonomy under contested conditions.

3. RAND Research Report: Artificial Intelligence and Machine Learning for Space Domain Awareness (RRA2318-1). Landing page: https://www.rand.org/pubs/research_reports/RRA2318-1.html
   - Summary: Surveys AI/ML applications for SDA (detection, classification, characterization, maneuver prediction, multi-sensor fusion), identifies key challenges (data scarcity/labeling, domain shift, on-orbit vs. ground processing trade-offs, verification/validation/trust), and recommends MLOps practices (simulation, synthetic data, active learning, performance monitoring) tailored to space.
   - Relevance to AIS: Directly informs Phase I literature review and feasibility analysis for Focus Area 1 (Edge Computing & Algorithms). Offers risk-reduction guidance for dataset curation, model selection for constrained hardware, and V&V strategies needed for autonomous, safety-critical decisions.

4. IEEE Aerospace 2023: "Autonomous Multi-phase Rendezvous, Proximity Operations, and Docking via Model Predictive Control" (DOI: 10.1109/AERO55745.2023.10115983). https://ieeexplore.ieee.org/document/10115983
   - Summary: Proposes a multi-phase Model Predictive Control (MPC) approach for RPOD with phase-specific controllers to handle differing constraints (e.g., LOS cones). Demonstrates in simulation fuel-efficient, constraint-respecting trajectories suitable for onboard computation.
   - Relevance to AIS: Provides a concrete, publishable method for autonomous maneuver planning and collision avoidance that can execute at the edge. Supports AIS Focus Areas 1 and 3 by showing how onboard algorithms can meet real-time and safety constraints.

5. NASA "Current Technology in Space v4 Briefing" (2024). PDF: https://ntrs.nasa.gov/api/citations/20240001139/downloads/Current%20Technology%20in%20Space%20v4%20Briefing.pdf
   - Summary: A broad reference on AI/ML for Ground, Edge/Tiny/Mobile, and Space environments, including a reference architecture, Space MLOps lifecycle, and a detailed hardware landscape. Compares processors for throughput/latency, radiation tolerance, power, sensor I/O, and maintainability; advocates heterogeneous compute and certifiable update pathways.
   - Relevance to AIS: Directly supports AIS architecture and trade studies across Focus Areas. Offers evidence-based choices for radiation-tolerant edge compute, power/thermal budgeting for AI workloads, and certified MLOps needed for safe on-orbit model updates and resilience.

6. Lockheed Martin: "AI/ML Mission Processing Onboard Satellites" (AIAA paper, 2022). PDF: https://www.lockheedmartin.com/content/dam/lockheed-martin/space/documents/ai-ml/PIRA-aiaa-6.2022-1472-aiml-mission-processing-onboard-satellites-paper.pdf
   - Summary: Describes on-board mission processing architectures and pipelines for AI/ML on satellites, including SWaP-aware design patterns, data handling/compression, scheduling, and heterogeneous compute (CPU/GPU/FPGA/SoC). Includes mission use cases (e.g., onboard detection/classification) and performance considerations.
   - Relevance to AIS: Demonstrates feasibility and design patterns for achieving AIS objectives (e.g., >50% kill-chain latency reduction) with onboard inference. Informs hardware/software partitioning, toolchains, and update strategies for resilient autonomy under space constraints.


## COSMIAC Publications & Projects (C#)

- [C1] COSMIAC Positioning, Navigation, and Timing (PNT) Project Page — ORDWG/SDR receivers, ML-based threat detection/mitigation, GNSS signal dataset, and multi-target model deployment options (FPGA, GPU, ARM, TPU, VPU).
  - Link: https://cosmiac.unm.edu/projects/pnt.html
  - Relevance: Supports onboard threat analytics, OOD/adversarial resilience, and heterogeneous/FPGA deployment for edge AI; informs Space MLOps/dataset curation.

- [C2] Morales Chacon, Clarizza (2023). “Design, Optimization, and Hardware Deployment of a Deep Learning Model for GPS Spoofing Detection using GNSS Satellite Receiver Protocol Data.” UNM ECE MS Thesis. Committee includes Dr. James Aarestad and Mr. Brian Zufelt.
  - Link: https://digitalrepository.unm.edu/ece_etds/626/
  - Relevance: Demonstrates GNSS spoofing detection via ML and real-time deployment on Xilinx Kria KV260 FPGA; aligns with FPGA-resident inference and PNT resilience.

- [C3] ION Joint Navigation Conference (JNC) — Sessions/Tutorials featuring COSMIAC’s Andrew Cochrane and Dr. James Aarestad on spoofing detection and ML for PNT.
  - Links: Program reference (2021): https://www.ion.org/jnc/upload/JNC21-Onsite.pdf | Tutorials: https://www.ion.org/jnc/tutorials.cfm
  - Relevance: Establishes COSMIAC leadership in GNSS interference/spoofing detection and ML-based PNT analytics relevant to onboard threat classification and resilience.

- [C4] SPARC‑1 (6U CubeSat) — On‑orbit Agile Space Radio (reconfigurable transceiver) and SSA camera; launched 2019.
  - Link: https://cosmiac.unm.edu/projects/sparc-1.html
  - Relevance: Heritage for software‑defined, reconfigurable RF payloads and on‑sensor/edge preprocessing concepts.

- [C5] Trailblazer / Space Plug‑and‑Play Avionics (SPA) — Modular avionics and rapid integration for CubeSats (Kief et al.).
  - Overview with references: https://www.eoportal.org/satellite-missions/trailblazer (includes: “The Advent of the PnP Cube Satellite,” IEEE Aerospace 2012)
  - Relevance: Informs bus abstraction, modular autonomy manager concepts, and rapid HIL/prototyping paths for flight‑like systems.

- [C6] RHEME — Radiation Hardened Electronic Memory Experiment (ISS/STP flights in 2016/2018/2022).
  - Link: https://cosmiac.unm.edu/projects/rheme.html | NSREC brochure refs mentioning RHEME‑2/3: https://www.nsrec.com/wp-content//uploads/2023/07/NSREC-2023BROCHURE-07.05.2023.pdf
  - Relevance: Radiation effects and SEU/TID mitigation heritage informing rad‑tolerant compute, SEU fault injection, and FPGA resilience strategies.

- [C7] UNM Antennas & RF Lab (Christos Christodoulou) — Reconfigurable antennas, cognitive radio, phased arrays, and deployable/3D‑printed antennas.
  - Link: https://rfant.unm.edu/
  - Relevance: Front‑end technology for passive RF micro‑payloads and software‑defined, reconfigurable sensing architectures.
