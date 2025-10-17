# Integrated Phase I Scope — SPECTRA Sensor-Compute Payload, Cross‑Modal Catalog, and HIL Simulation/Testing (Phase I focus: RF) (IA + COSMIAC)

## Value statement
- SDA/Catalog‑informed edge ML processing of sensor data for rapid alerting and fast, informed response
- Automated SDA reconnaissance

## Introduction and provenance
This integrated scope consolidates and extends scope elements in AIS/spectra/scope_idea.md, aligned to AIS Subtopic 3 (Sensor Payloads) and the solicitation’s primary concerns (AIS/primary_concerns.md). It reflects IA’s background (AIS/ia.md) and COSMIAC’s capabilities (AIS/cosmiac.md), targeting a Phase I feasibility package with clear Phase II pathways.

## Executive summary
SPECTRA (Sensor Processing at the Edge for Cognitive Threat Reconnaissance and Alert) is a three-tier, cross-modal architecture to deliver:

1) **SPECTRA HPC-S** (onboard, SOSA-compliant ML/AI/fusion compute): A modular, reconfigurable sensor-compute payload architecture that applies to arbitrary in-flight sensors; in Phase I we prototype and evaluate the feasibility of the RF path (passive RF front end) via sim/HIL runs and initial bench snapshots, while keeping interfaces modality-agnostic. The architecture supports multimodal sensor fusion at the edge, enabling joint RF/SAR/EO/IR/HSI processing for enhanced threat detection and classification. Receives raw sensor observations, applies AI/ML and data-fusion algorithms to generate threat events and alerts, and provides event detection data to SPECTRA Edge DB.

2) **SPECTRA Edge DB** (onboard, SOSA-compliant database): A schema and pipeline for a cross-modal Space EW Catalog with prioritized edge slices carried onboard for low-latency decisions and intermittent downlink. Maintains an updatable slice of the ground catalog, receives catalog updates when possible, provides catalog data to SPECTRA HPC-S for threat detection, and catalogs both raw observations and detected events. When connectivity permits, syncs to the ground threat/reconnaissance catalog, with attack-event reports and signal observations disseminated to the broader SDA community via UDL.

3) **SPECTRA Ground Processing** (ground-based data management): Receives events and observations from the spacecraft, disseminates them to mission operations and the broader SDA community via UDL, determines proper catalog updates based on SDA intelligence, manages SPECTRA HPC-S model updates and training with comprehensive mission data and HIL mod/sim. Phase I focuses on CONOPS development for this tier.

4) **Payload-in-the-Loop M&S and HIL Testing Framework**: A reusable simulation and HIL testing framework, including simulated EW attack scenarios, that can host different sensor models; in Phase I we realize the RF case.

Integration at a glance (Phase I feasibility):
- Edge ML threat detection from COSMIAC/PIGEON
- Edge processing hardware from COSMIAC
- Database/catalog techniques from IA (edge slices and ground integration, e.g., OmniCat where permissible)
- Simulation and HIL capabilities from IA (sensor‑agnostic harness with EW attack injectors)

Outputs include: literature/trade studies and architecture, preliminary CONOPS and system diagrams, payload‑in‑the‑loop M&S evidence with quantitative metrics, a HIL bench plan with initial results, risk register with CTEs, and a Phase II plan for a bench/flight‑like prototype.

## Why this meets real operational needs (USSF/AIS Subtopic 2)
- Modality‑agnostic sensor‑compute architecture (HPC‑S) that generalizes across RF, SAR/LIDAR/EO/IR/HSI; Phase I exercises the RF instantiation.
- Integrated sensor‑compute packaging reduces detection→classification latency and preserves mission utility in comms‑degraded/denied conditions.
- Multimodal sensor fusion at the edge combines complementary sensor modalities (RF, SAR, EO, IR, HSI) for robust threat detection and improved classification confidence, even under partial sensor degradation or denial.
- Fusion/tip‑and‑cue design maintains custody through maneuvers across LEO/GEO/XGEO/cislunar, independent of sensor modality.
- Evidence‑driven feasibility for edge‑hosted catalog slices and uncertainty‑aware alerts directly addresses evaluator concerns (latency, workload, trust/assurance).

## Technical approach
### Thread A — Modular sensor‑compute payload (Phase I RF instantiation) with on‑sensor processing and secure pathways
- Modality‑agnostic plugin interface: define sensor‑specific front‑end/feature extractors and model containers so additional modalities can be swapped in without re‑architecture. Support fusion interfaces for combining multi‑modal feature streams and joint threat detection pipelines.
- Phase I RF instantiation: COSMIAC RF front end (e.g., PIGEON heritage) feeding on‑sensor feature extraction (PDW‑like vectors) and ML threat detection, uncertainty scoring, and event triage within SWaP/radiation/thermal limits. Design fusion pathways to enable future integration of SAR/EO/IR/HSI streams for enhanced edge classification.
- Compute options: Trade CPU/GPU/FPGA/SoC/neuromorphic candidates; early emphasis on FPGA/SoC for deterministic latency and power efficiency; plan for secure boot and signed model/config updates. Ensure compute headroom for multi‑modal fusion operations.
- Security‑by‑design: Memory‑safe runtime pathway, zero‑trust data handling, keying and telemetry redaction suitable for ITAR/CUI contexts.


- Example RF geolocation chain (non-binding): implement time/frequency difference-of-arrival (TDOA/FDOA) with time-sync and baseline geometry in simulation/HIL; report geolocation CEP vs SNR/interferer dwell as available.
- GEO emissions characterization (example workload): classifiers for comm/beacon signals and emissions-change detection to augment “neighborhood watch”; used to demonstrate tip-and-cue without constraining Phase I scope.

### Thread B — Cross‑modal Space EW Catalog and edge subset feasibility
- Catalog concept: Cross‑modal Space EW Catalog with modality‑aware parametric/emitter/event descriptors and observation products; evaluate feasibility of carrying prioritized slices onboard.
- Data products: Compact summaries (detections, PDW‑like features or analogous per‑modality features, UQ scores, maneuver/change flags) and evidence snippets for downlink (e.g., UDL) when connectivity permits.
- Ground integration: Use/adapt existing repositories (e.g., OmniCat) where permissible; otherwise stand up an unclassified scaffold with clear pathways to classified systems; Phase I populates the RF path while keeping schema modally extensible.


- Astrometry/POD hooks (future modalities): define placeholders for onboard centroiding and preliminary orbit determination so compact tracks can be transmitted alongside RF descriptors when optical/EO plugins are introduced.
- Tip-and-cue schema (minimal, modality-agnostic): specify a lightweight cue message (target/time/confidence/spec) to enable cross-sensor tasking (e.g., OPIR/optical) without implementing it fully in Phase I.

### Thread C — Payload‑in‑the‑loop M&S and HIL with simulated EW attacks
- Sensor‑agnostic framework: a reusable simulation/HIL harness that can host different sensor models and datasets; Phase I realizes the RF case.
- Simulation: Integrate the RF payload model into IA’s NGSX scenarios for SDA/RPO; generate synthetic RF scenes using EWIRDB‑like parametric threat models via an EMoP‑like process to evaluate custody and time‑to‑classification.
- HIL: Auto‑generate PDWs via an EMoP‑like process (using EWIRDB‑like models) to stimulate hardware via AWG, including simulated EW attack scenarios; validate onboard pre‑processing thresholds and latency; compare to lab/test data where available; uncertainty‑gate decisions using SIERO‑like methods.
- Evidence: Quantify latency improvements, power/thermal envelopes, uncertainty calibration, and robustness to adversarial conditions.

- Scenario pack example — Theater GPS jamming detection & geolocation: measure detection→geolocation alert latency and geolocation accuracy (CEP) across SNR/dwell variations.
- Scenario pack example — GEO emissions characterization: detect unusual emissions/behavior changes; measure timeliness and false-alert rates.
- RPO (sim-only) example: emissions-based proximity cueing and keep-out zone enforcement; log relative navigation/decision latency (no commitment to optical/LIDAR in Phase I).


### Thread D — Architecture, CONOPS, and integration‑ready interfaces
- System view: End‑to‑end block diagrams for sensor→edge compute→fusion/tip‑and‑cue→downlink→catalog growth.
- Interfaces: Modality‑agnostic schemas for edge summaries/evidence, health telemetry, and operator digests; hooks for future standards alignment (e.g., CCSDS/BM‑C2) without over‑scoping Phase I.
- Update pathway: Document a certifiable update concept (signed/config updates) appropriate to Phase I feasibility.


- Example interface stub — OPIR↔RF cueing (documentation only in Phase I): define notional JSON/protobuf fields {obs_time, target_region, cue_type, confidence, validity, contact} to illustrate future cross-sensor tasking.

## Phase I activities and deliverables
- Phase I focus: feasibility analysis for SPECTRA HPC-S and SPECTRA Edge DB, and CONOPS development for SPECTRA Ground Processing; exercise the RF instantiation while ensuring all designs (payload, catalog, HIL) are modality-agnostic and reusable for other sensors. Additional thrust: feasibility study and CONOPS for a comprehensive test harness for SPECTRA DB and HPC-S validation, including HIL simulation and adversarial signal emitter concepts for live testing.
- Literature and trade studies: passive RF payloads, reconfigurable/SDR patterns, edge compute under SWaP/rad/thermal, catalog slicing/compression, assurance/monitoring, and test harness architectures.
- Architecture and feasibility: heterogeneous compute trades; prioritized catalog slice feasibility; memory‑safe runtime pathway; security/update concepts; test harness architecture for comprehensive validation.
- Payload‑in‑the‑loop M&S: synthetic EW scenes; custody/latency metrics; uncertainty calibration; ablation under comms‑degraded and maneuvering targets.
- HIL plan and initial bench results: AWG‑stimulated scenarios with simulated EW attacks; latency thresholds and power/thermal snapshots; early robustness checks; test harness framework design and initial validation.
- Test harness feasibility and CONOPS: Define comprehensive test harness architecture for SPECTRA Edge DB and HPC-S; design HIL simulation framework; assess adversarial signal emitter concepts for live testing; produce test plan and CONOPS for bench and potential live testing.
- Preliminary CONOPS and diagrams: mission threads for contested/degraded comms; integration‑ready payload‑compute packaging; test harness operational workflows.
- Risk register with CTEs and mitigation plan; Phase II roadmap to a bench/flight‑like prototype and limited over‑the‑air exercises where permissible; adversarial emitter development roadmap.
- AIS Phase I Showcase assets: concise technical narrative, figures/plots, and traceable metrics; test harness readiness assessment.

## Phase I Technical Objectives

Objective 1: SPECTRA HPC-S feasibility (Modular sensor-compute architecture, Phase I RF instantiation)
- R&D Questions: What modality-agnostic plugin interfaces are required (front-end, feature extractors, model containers)? What deterministic latency bounds are feasible on candidate SoC/FPGA under SWaP/rad/thermal? What lightweight signed config/update concept is viable for Phase I?
- Feasibility Determination: Edge pipeline latency/jitter bounds bench-measured; plugin API realized (stubs + example RF plugin); initial power/thermal snapshots; signed-config/update concept documented and emulated in bench loop.

Objective 2: SPECTRA Edge DB feasibility (Cross-modal Space EW Catalog schema + edge slice feasibility)
- R&D Questions: What schema supports cross-modal descriptors (RF, SAR/LIDAR/EO/IR/HSI) and observation/evidence products? What slice sizes/compression achieve onboard feasibility and manageable downlink bundles? How do observations and events flow through the Edge DB to update the catalog?
- Feasibility Determination: Slice storage footprint, compression ratio, and retrieval latency characterized; downlink bundle sizes for alert/evidence reported; schema validated with at least two modality exemplars (design-time), RF realized in Phase I; observation-to-event pipeline documented.

Objective 3: SPECTRA Ground Processing CONOPS (Concept of Operations)
- R&D Questions: What operational workflows enable SPECTRA Ground Processing to receive events/observations from spacecraft, disseminate to mission operations and SDA community via UDL, determine catalog updates based on SDA intelligence, and manage HPC-S model updates and training? What are the data flows, decision points, and integration touchpoints?
- Feasibility Determination: Preliminary CONOPS document produced; operational workflows and data flows diagrammed; integration points with UDL and mission operations identified; model update and training pipeline conceptualized.

Objective 4: Payload-in-the-loop simulation + HIL harness with EW attack injectors
- R&D Questions: What simulation fidelity is sufficient for Phase I custody/latency insights? How do EWIRDB-like/EMoP-like generators and red-team injectors drive realistic stress? What uncertainty calibration targets are attainable?
- Feasibility Determination: Sim/HIL harness executes RF scenarios with EW attack injectors; AWG-stimulated bench snapshots captured; uncertainty calibration curves (e.g., ECE/Brier) reported; stability demonstrated across scenario packs.

Objective 5: Test harness feasibility and CONOPS for SPECTRA DB and HPC-S
- R&D Questions: What test harness architecture enables comprehensive validation of SPECTRA Edge DB and SPECTRA HPC-S? What HIL simulation capabilities are required? What adversarial signal emitter concepts are viable for live testing? How can the test harness support both bench-based and potential live testing scenarios?
- Feasibility Determination: Test harness architecture documented; HIL simulation framework design completed; adversarial signal emitter concepts and feasibility assessed; test plan and CONOPS for bench and potential live testing produced; integration pathways with existing test facilities identified.

Objective 6: Interfaces, operator digests, and integration readiness
- R&D Questions: What modality-agnostic schemas (summaries/evidence/health) and operator digest formats best support Phase II integration? What preliminary standards fit (e.g., CCSDS/BM-C2) can be documented without Phase I compliance?
- Feasibility Determination: Schemas validated via round-trip examples; operator digest exemplars produced; preliminary standards-fit notes compiled.

## Phase I Base (6 mo) Statement of Work (example)
T1 — Kickoff + Feasibility Plan (M1): finalize objectives, simulation/HIL plans, dataset/signal scope; define three-tier architecture (HPC-S, Edge DB, Ground Processing) and observation-to-event data flows; outline test harness requirements.
T2 — Architecture & Catalog Schema Trades (M2–M3): SPECTRA HPC-S plugin interfaces; SPECTRA Edge DB catalog schema + slice/compression trades; SPECTRA Ground Processing CONOPS preliminary outline; test harness architecture preliminary design.
T3 — Simulation Harness + Scenario Packs (M3–M4): RF payload-in-the-loop integration; EW attack injectors; uncertainty calibration plan; observation and event data flow validation.
T4 — HIL Plan + Initial Bench Snapshots (M4–M5): AWG-stimulated runs; timing/power/thermal snapshots; signed-config emulation; observation-to-event pipeline testing.
T5 — Test Harness Feasibility and CONOPS (M4–M5): Define test harness architecture for comprehensive validation of SPECTRA Edge DB and HPC-S; design HIL simulation framework; assess adversarial signal emitter concepts for live testing; produce test plan and CONOPS for bench and potential live testing.
T6 — Feasibility Indicators + Evidence Package (M5–M6): latency/jitter, calibration curves, slice viability, interface validation; trace capture for V&V; three-tier architecture feasibility summary; test harness readiness assessment.
T7 — Phase II Design & Transition Readiness Outline (M6): prototype maturation plan; standards-fit and integration roadmap; SPECTRA Ground Processing CONOPS refinement plan; test harness and adversarial emitter development roadmap.

## Data, Evaluation, & Metrics (Phase I methods)
- Latency/jitter bounds: on‑bench timing logs for read→process→emit; controlled load sweeps; stability across runs.
- Power/thermal/SWaP: bench measurements + modeled envelopes for selected configurations; margin analysis.
- Uncertainty calibration: ECE/Brier on synthetic + bench traces; threshold selection and calibration plots.
- Robustness (EW attacks): red‑team injectors applied in sim/HIL; false‑alert rates; stability/throughput traces under stress.
- Catalog slice viability: footprint, compression, retrieval latency; downlink bundle size for alert/evidence; schema round‑trip checks.
- Interfaces & operator digests: schema conformance tests; sample digests; preliminary standards‑fit notes captured.


- Geolocation accuracy: CEP50/CEP90 vs SNR and interferer dwell time (sim/HIL).
- Alert timeline: detection→triage→geolocation latency distribution.
- RPO (example) metric: relative nav decision latency and keep-out violation risk (sim-only).

## Phase I feasibility indicators (evidence-focused)
- **SPECTRA HPC-S**: Edge pipeline latency and jitter bounds for feature extraction/triage on candidate SoC/FPGA (bench-measured, repeatable); observation-to-event processing pipeline validated.
- **SPECTRA Edge DB**: Catalog slice feasibility (storage footprint, compression ratio, retrieval latency); schema validation for modality-agnostic products; downlink size for alert/evidence bundles; observation and event cataloging pipeline demonstrated.
- **SPECTRA Ground Processing**: Preliminary CONOPS document; operational workflows and data flows diagrammed; integration points with UDL and mission operations identified.
- **Integrated System**: Simulated end-to-end observation→event→alert latency vs. ground-loop baseline in controlled scenarios (report observed improvements with confidence bounds; no fixed % commitments in Phase I).
- Power/thermal/SWaP: bench snapshots and modeled envelopes that close for selected configurations.
- Uncertainty calibration (e.g., ECE/Brier) on synthetic + bench traces; false-alert rates under red-teamed simulated EW attack injectors.
- HIL: deterministic read→process→emit loop with measured timing bounds; initial stability across scenario packs; trace capture for V&V.
- Interfaces: modality-agnostic schemas validated; preliminary fit to future standards (e.g., CCSDS/BM-C2) documented without committing Phase I compliance.

## Phase II projections (alignment to AIS evaluator targets)
- Decision latency: target >50% reduction vs. ground‑loop baseline in ops‑like simulations/bench‑in‑the‑loop.
- Operator workload proxy: target ≥25% reduction via onboard triage and operator digests.
- Custody/time‑to‑classification: target −25–35% custody gaps and −30–40% time‑to‑classification vs. heuristic baselines under bandwidth caps and jamming.
- Robustness/trust: maintain alert quality under simulated EW attack injectors; signed update/config pathway matured for flight‑like prototypes.

## Proposed Phase I final outcome
By end of Phase I, SPECTRA delivers a coherent feasibility package for a three-tier architecture (SPECTRA HPC-S, SPECTRA Edge DB, SPECTRA Ground Processing) with an RF instantiation that produces uncertainty-aware, downlink-efficient products and grows a cross-modal Space EW Catalog:
- **SPECTRA HPC-S Feasibility**: Modular sensor-compute payload architecture with modality-agnostic plugin interfaces; RF instantiation with deterministic latency bounds bench-measured; compute trade studies; security/update pathway.
- **SPECTRA Edge DB Feasibility**: Cross-modal catalog schema with edge slice viability; observation and event cataloging pipeline; storage footprint and compression ratios characterized; downlink bundle efficiency demonstrated.
- **SPECTRA Ground Processing CONOPS**: Preliminary operational concept; data flows from spacecraft to ground; dissemination to mission operations and SDA community via UDL; model update and training pipeline conceptualized.
- **Preliminary Architecture and Interfaces**: End-to-end design for contested space operations; observation-to-event data flows documented; integration-ready interface schemas; modality-agnostic design for Phase II expansion.
- **M&S + HIL evidence**: Latency/power/thermal profiles; uncertainty calibration; robustness to simulated EW attack scenarios; observation-to-event pipeline validation.
- **Evaluation dossier**: Traceable metrics demonstrating latency/workload improvements and custody gains; no safety-invariant violations in stress tests.
- **Phase II transition plan**: Bench/flight-like prototype maturation and limited over-the-air exercises, with a modality expansion path (e.g., SAR/EO/IR/HSI) without re-architecture; SPECTRA Ground Processing CONOPS refinement.

## Roles, workshare, and facilities (STTR‑compliant)
- COSMIAC (UNM)
  - RF front‑end design/integration (PIGEON heritage), edge ML threat detection prototyping leveraging PIGEON heritage, radiation test planning/mitigation, FPGA acceleration options, smallsat/ground‑station integration, environmental testing.
  - HIL bench setup and execution; bench hardware/instrumentation; power/thermal profiling; support security/update feasibility and interface schema validation; IA provides HIL control software.
- Interactive Aptitude (IA)
  - Simulation development: sensor‑agnostic payload‑in‑the‑loop simulation framework and scenario packs (NGSX integration), synthetic RF scene generation via EMoP‑like approaches and red‑team EW attack injectors; HIL orchestration/control software and data collection pipelines.
  - EMoP‑like (EWIRDB‑like‑to‑PDW/model generation approaches) and SIERO‑like uncertainty gating methods; calibration/validation against lab/test data where available.
  - Cross‑modal Space EW Catalog schema and catalog development leadership; edge slice feasibility; ground catalog integration (e.g., OmniCat) where permissible; data product schema design; edge summary/evidence packaging; preliminary CONOPS; metrics and ablation studies; Showcase artifacts.

## Risks and mitigations
- SWaP/thermal/radiation: Derive budgets/margins; evaluate rad‑tolerant compute; prototype thermal throttling and graceful degradation.
- Blind spots/cislunar ranges: Design for multi‑modal expansion in Phase II; tip‑and‑cue threads and dynamic scheduling to sustain custody.
- Data poisoning/robustness: Onboard anomaly detection, signed models/configs, uncertainty‑gated autonomy; simulation‑based red‑teaming in NGSX using SIERO‑like methods.
- Integration complexity: Modular interfaces for sensor‑compute packages; memory‑safe implementations and deterministic latency paths; early interface schema definition.

## Phase II trajectory (preview)
- Mature HIL prototype into an integrated, flight‑like payload/processor; thermal‑vac and radiation testing; limited over‑the‑air exercises with partner ranges where permissible.
- Expand to additional modalities (SAR/EO/IR/HSI) under the same payload‑compute framework; implement multimodal sensor fusion at the edge for joint threat detection and improved classification confidence across complementary sensor streams.
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

