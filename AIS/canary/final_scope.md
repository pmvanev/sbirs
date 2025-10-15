# Integrated Phase I Scope — CANARY Sensor Payloads for Passive RF EW Detection, On‑Sensor Processing, and Catalog Growth (IA + COSMIAC)

## Introduction and provenance
This integrated scope consolidates and extends scope elements in AIS/canary/scope_idea.md, aligned to AIS Subtopic 2 (Sensor Payloads) and the solicitation’s primary concerns (AIS/primary_concerns.md). It reflects IA’s background (AIS/ia.md) and COSMIAC’s capabilities (AIS/cosmiac.md), targeting a Phase I feasibility package with clear Phase II pathways.

## Executive summary
We propose a sensor‑compute payload concept centered on a passive RF front end with on‑sensor processing (HPC‑S) that:
1) Detects, triages, and summarizes EW events in real time at the edge, producing compact, uncertainty‑aware data products (e.g., PDW‑like feature vectors and maneuver/change flags) suitable for intermittent downlink.
2) Seeds and grows a "Space EW Catalog" by fusing on‑orbit observations with ground knowledge; defines and evaluates the feasibility of carrying prioritized catalog slices onboard.
3) Demonstrates payload‑in‑the‑loop modeling and HIL testing, including simulated EW attack scenarios, to quantify end‑to‑end latency, persistent custody improvements, and robustness.

Outputs include: literature/trade studies and architecture, preliminary CONOPS and system diagrams, payload‑in‑the‑loop M&S evidence with quantitative metrics, a HIL bench plan with initial results, risk register with CTEs, and a Phase II plan for a bench/flight‑like prototype.

## Why this meets real operational needs (USSF/AIS Subtopic 2)
- Integrated sensor‑compute packaging (HPC‑S) reduces detection→classification latency and preserves mission utility in comms‑degraded/denied conditions.
- Software‑defined/reconfigurable payload architecture supports modality expansion (future SAR/LIDAR/EO/IR/HSI) without wholesale re‑architecture.
- Multi‑modal fusion path and tip‑and‑cue design maintain custody through maneuvers across LEO/GEO/XGEO/cislunar regimes.
- Evidence‑driven feasibility for edge‑hosted catalog slices and uncertainty‑aware alerts directly addresses Phase I evaluator concerns (latency, workload, and trust/assurance).

## Technical approach
### Thread A — Passive RF payload with on‑sensor processing and secure pathways
- Payload concept: COSMIAC RF front end (e.g., PIGEON heritage) feeding on‑sensor feature extraction (PDW‑like vectors), uncertainty scoring, and event triage within SWaP/radiation/thermal limits.
- Compute options: Trade CPU/GPU/FPGA/SoC/neuromorphic candidates; early emphasis on FPGA/SoC for deterministic latency and power efficiency; plan for secure boot and signed model/config updates.
- Security‑by‑design: Memory‑safe runtime pathway, zero‑trust data handling, keying and telemetry redaction suitable for ITAR/CUI contexts.

### Thread B — Space EW Catalog and edge subset feasibility
- Catalog concept: A Space EW Catalog with parametric/emitter descriptors and observation products; evaluate feasibility of carrying prioritized slices onboard.
- Data products: Compact summaries (detections, PDW‑like features, UQ scores, maneuver/change flags) and evidence snippets for downlink (e.g., UDL) when connectivity permits.
- Ground integration: Use or adapt existing repositories where permissible; otherwise stand up an unclassified scaffold with clear pathways to classified systems in later phases.

### Thread C — Payload‑in‑the‑loop M&S and HIL with simulated EW attacks
- Simulation: Integrate the RF payload model into IA’s NGSX scenarios for SDA/RPO; generate synthetic RF scenes using EWIRDB‑like parametric threat models via an EMoP‑like process to evaluate custody and time‑to‑classification.
- HIL: Auto‑generate PDWs via an EMoP‑like process (using EWIRDB‑like models) to stimulate hardware via AWG, including simulated EW attack scenarios; validate onboard pre‑processing thresholds and latency; compare to lab/test data where available; uncertainty‑gate decisions using SIERO‑like methods.
- Evidence: Quantify latency improvements, power/thermal envelopes, uncertainty calibration, and robustness to adversarial conditions.

### Thread D — Architecture, CONOPS, and integration‑ready interfaces
- System view: End‑to‑end block diagrams for sensor→edge compute→fusion/tip‑and‑cue→downlink→catalog growth.
- Interfaces: Schema for edge summaries/evidence, health telemetry, and operator digests; hooks for future standards alignment (e.g., CCSDS/BM‑C2) without over‑scoping Phase I.
- Update pathway: Document a certifiable update concept (signed/config updates) appropriate to Phase I feasibility.

## Phase I activities and deliverables
- Literature and trade studies: passive RF payloads, reconfigurable/SDR patterns, edge compute under SWaP/rad/thermal, catalog slicing/compression, and assurance/monitoring.
- Architecture and feasibility: heterogeneous compute trades; prioritized catalog slice feasibility; memory‑safe runtime pathway; security/update concepts.
- Payload‑in‑the‑loop M&S: synthetic EW scenes; custody/latency metrics; uncertainty calibration; ablation under comms‑degraded and maneuvering targets.
- HIL plan and initial bench results: AWG‑stimulated scenarios with simulated EW attacks; latency thresholds and power/thermal snapshots; early robustness checks.
- Preliminary CONOPS and diagrams: mission threads for contested/degraded comms; integration‑ready payload‑compute packaging.
- Risk register with CTEs and mitigation plan; Phase II roadmap to a bench/flight‑like prototype and limited over‑the‑air exercises where permissible.
- AIS Phase I Showcase assets: concise technical narrative, figures/plots, and traceable metrics.

## Quantitative success metrics (Phase I targets)
- Detection→classification latency: ≥50% reduction vs. ground‑loop baseline in sim; on‑device pre‑processing under deterministic latency bounds.
- Operator workload proxy: ≥25% reduction via onboard triage and operator digests.
- Custody and maneuver/change detection: −25–35% custody gaps; −30–40% time‑to‑classification vs. heuristic baseline under bandwidth caps.
- Power/thermal/SWaP: Profiles close under realistic or conservatively modeled envelopes for selected edge hardware.
- Robustness/trust: Uncertainty‑calibrated thresholds with low false‑alert rates in red‑teamed simulated EW attack scenarios.

## Proposed Phase I final outcome
By end of Phase I, CANARY delivers a coherent feasibility package for a reconfigurable passive RF sensor‑compute payload that produces uncertainty‑aware, downlink‑efficient products and grows a Space EW Catalog:
- Feasibility study and trades: payload and compute selections; catalog slice viability; security/update pathway.
- Preliminary CONOPS and architecture: end‑to‑end design for contested space operations; integration‑ready interface schemas.
- M&S + HIL evidence: latency/power/thermal profiles; uncertainty calibration; robustness to simulated EW attack scenarios.
- Evaluation dossier: traceable metrics demonstrating latency/workload improvements and custody gains; no safety‑invariant violations in stress tests.
- Phase II transition plan: bench/flight‑like prototype maturation and limited over‑the‑air exercises, with a modality expansion path (e.g., SAR/EO/IR/HSI) without re‑architecture.

## Roles, workshare, and facilities (STTR‑compliant)
- COSMIAC (UNM)
  - RF front‑end design/integration (PIGEON heritage), radiation test planning/mitigation, FPGA acceleration options, smallsat/ground‑station integration, environmental testing.
  - HIL bench setup and execution; power/thermal profiling; support security/update feasibility and interface schema validation.
- Interactive Aptitude (IA)
  - EMoP‑like (EWIRDB‑like‑to‑PDW/model generation approaches), SIERO‑like uncertainty gating methods, NGSX payload‑in‑the‑loop scenarios.
  - Data product schema design; edge summary/evidence packaging; preliminary CONOPS; metrics and ablation studies; Showcase artifacts.

## Risks and mitigations
- SWaP/thermal/radiation: Derive budgets/margins; evaluate rad‑tolerant compute; prototype thermal throttling and graceful degradation.
- Blind spots/cislunar ranges: Design for multi‑modal expansion in Phase II; tip‑and‑cue threads and dynamic scheduling to sustain custody.
- Data poisoning/robustness: Onboard anomaly detection, signed models/configs, uncertainty‑gated autonomy; simulation‑based red‑teaming in NGSX using SIERO‑like methods.
- Integration complexity: Modular interfaces for sensor‑compute packages; memory‑safe implementations and deterministic latency paths; early interface schema definition.

## Phase II trajectory (preview)
- Mature HIL prototype into an integrated, flight‑like payload/processor; thermal‑vac and radiation testing; limited over‑the‑air exercises with partner ranges where permissible.
- Expand to additional modalities (SAR/EO/IR/HSI) under the same payload‑compute framework; add on‑sensor fusion and more advanced tip‑and‑cue.
- Extend catalog integration and on‑orbit update pathways; prepare standards alignment (e.g., CCSDS/BM‑C2) and transition artifacts.

## Commercial potential (dual‑use)
- RF anomaly detection and catalog products for unclassified space operations and commercial constellation operators.
- Safety‑critical RF anomaly detection for automotive, maritime, and aviation (fighter jets and commercial airliners), and critical infrastructure.
- HIL simulation and test toolchains for EW robustness evaluations; training products for operations and test teams.

## References and evidence base
- AIS/primary_concerns.md — operational drivers, technical focus areas, architecture/integration expectations, V&V and trust, program constraints, quantitative targets.
- AIS/ia.md — IA background in autonomy, simulation, and edge AI; relevant programs and infrastructure.
- AIS/cosmiac.md — COSMIAC RF, radiation, small‑sat, and FPGA expertise; facilities and personnel.
- AIS/ais_solicitation_raw.md — Subtopic 2: Sensor Payloads desired capabilities and technologies (integrated sensor‑compute, multi‑modal fusion, reconfigurability, HPC‑S).

