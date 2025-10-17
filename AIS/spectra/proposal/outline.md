## SPECTRA Proposal — Outline and Mapping Summary

### Executive Summary (What this proposal does)
- Proposes SPECTRA, a three-tier, reconfigurable, modality-agnostic architecture for contested space operations to accelerate threat detection, triage, and decision-making in contested/comms-denied space operations.

**Core Subsystems:**
- **(1) SPECTRA HPC-S** — Onboard ML/AI/fusion compute with edge threat detection and multimodal sensor fusion; modular sensor-compute payload with plugin-based architecture for RF/SAR/EO/IR/HSI.
- **(2) SPECTRA Edge DB** — Onboard SOSA-compliant database maintaining updatable catalog slices; cross-modal Space Threat Catalog with edge slices and downlink-efficient products.
- **(3) SPECTRA Ground Processing** — Ground-based data management, dissemination to mission operations and SDA community via UDL, catalog updates, and model training.

**Phase I Main Initiatives:**
- **Feasibility Studies for SPECTRA HPC-S and SPECTRA Edge DB** — RF instantiation to establish deterministic latency and SWaP baselines; simulation, HIL bench snapshots, latency/power/thermal profiling, and uncertainty calibration.
- **CONOPS for SPECTRA Ground Processing** — Operational workflows for receiving events/observations, disseminating to mission operations and SDA community, determining catalog updates, and managing model training and updates.
- **Test Harness Feasibility and CONOPS** — Comprehensive test harness architecture for SPECTRA DB and HPC-S validation; HIL simulation framework design; adversarial signal emitter concepts for live lab testing; test plan and CONOPS for bench and potential live testing.
- **Modality-Agnostic Plugin Architecture and Catalog Schema** — Establishes extensible design and plugin interfaces to enable Phase II multimodal expansion (SAR/EO/IR/HSI) without re-architecture.
- **Integration-Ready Interfaces and Evidence Packaging** — Modality-agnostic schemas for edge summaries, operator digests, evidence packaging, and preliminary standards alignment (CCSDS/BM-C2).

---

### Section-by-Section Outline

1) **Front Matter**
   - Volume and Title: "Volume 2: Technical Volume"; Title: "SPECTRA: Sensor Processing at the Edge for Cognitive Threat Reconnaissance and Alert".

2) **1.0 Description of Proposed Phase I Technical Effort**
   - Problem: Current space threat detection systems suffer from high detection→classification latency, operator workload bottlenecks, and custody gaps in comms-denied conditions; single-modality sensors (RF, SAR, EO, IR, HSI) miss complementary threat signatures; ground-centric processing delays decisions. Multimodal fusion at the edge is needed to accelerate threat detection and improve confidence across diverse sensor streams.
   - Scenario: Contested space operations with diverse threats (RF/EW, kinetic, maneuver, signature anomalies), bandwidth constraints, and maneuvering targets across LEO/GEO/XGEO/cislunar; operators need rapid, uncertainty-aware alerts and multimodal fusion (RF/SAR/EO/IR/HSI) to maintain custody and confidence. Phase I focuses on RF/EW instantiation to establish architecture and baselines; Phase II expands to additional modalities and threat types.
   - Proposed Solution (five innovations):
     - Modular Sensor-Compute Payload: reconfigurable, modality-agnostic plugin architecture for RF/SAR/EO/IR/HSI with deterministic latency and SWaP efficiency; SOSA-compliant design for interoperability.
     - Cross-Modal Space Threat Catalog: SOSA-compliant schema and edge slices for compact, downlink-efficient threat descriptors and observation products across modalities (initial EW focus, expandable to SAR/EO/IR/HSI).
     - Payload-in-the-Loop M&S: sensor-agnostic simulation harness with synthetic threat scenes and red-team attack injectors (Phase I RF, Phase II multimodal).
     - HIL Testing Framework: AWG-stimulated bench validation with latency/power/thermal profiling and uncertainty calibration.
     - Integration-Ready Interfaces: modality-agnostic schemas for edge summaries, operator digests, and standards alignment (SOSA, CCSDS/BM-C2).
   - Figures/Tables: Figure 1 (system architecture, end-to-end flow). Table 1 (degree of innovation). Table 2 (topic/AIS requirement alignment).
   - Team: COSMIAC (RF front-end, edge ML, FPGA, radiation expertise) + IA (simulation, catalog, HIL orchestration, autonomy/AI background).

3) **1.01 Technical Approach**
   - Three-tier, integrated, modular architecture: **(1) SPECTRA HPC-S** ingests multimodal sensor observations (RF/SAR/EO/IR/HSI) and threat catalogs, applies AI/ML and data-fusion algorithms to generate threat events and alerts; **(2) SPECTRA Edge DB** maintains an updatable catalog slice, receives observations and events from HPC-S, catalogs them, and syncs to ground when possible; **(3) SPECTRA Ground Processing** receives events/observations, disseminates to mission operations and SDA community via UDL, determines catalog updates, and manages model training. Phase I instantiates RF pathway to establish deterministic latency and SWaP baselines; architecture supports plugin-based expansion to additional modalities in Phase II.
   - Subsections (each with challenge + DoI + methods + evidence/TRL + operational impact):
     1. SPECTRA HPC-S: Modular Sensor-Compute Payload (Phase I RF instantiation; Phase II multimodal-ready) — modality-agnostic plugin interfaces (front-end, feature extractors, model containers) designed for RF/SAR/EO/IR/HSI; Phase I realizes COSMIAC RF front-end (PIGEON heritage) with on-sensor feature extraction (PDW-like vectors) and ML threat detection; compute trades (CPU/GPU/FPGA/SoC/neuromorphic) with emphasis on FPGA/SoC for deterministic latency and power efficiency; security-by-design (memory-safe runtime, zero-trust data handling, signed model/config updates); observation-to-event processing pipeline; addresses latency, single-modality blindness, and SWaP/rad/thermal constraints; plugin stubs enable Phase II SAR/EO/IR/HSI integration.
     2. SPECTRA Edge DB: Cross-Modal Space Threat Catalog Schema (initial EW focus, multimodal-ready) — modality-aware parametric/emitter/event descriptors and observation/event products; Phase I focuses on RF threat models and EW descriptors; compact summaries (detections, PDW-like features, UQ scores, maneuver/change flags) and evidence snippets for downlink; edge slice feasibility (storage footprint, compression ratio, retrieval latency); observation and event cataloging pipeline: raw observations and edge-detected threat events update onboard slice; when connectivity permits, sync to ground catalog and disseminate attack-event reports and signal observations to broader SDA community via UDL; astrometry/POD hooks and tip-and-cue schema (minimal, modality-agnostic) for future cross-sensor tasking and Phase II SAR/EO/IR/HSI integration; addresses downlink efficiency, onboard decision support, multimodal expansion, and SDA community integration.
     3. SPECTRA Ground Processing: Operational Concept and Data Management — preliminary CONOPS for receiving events/observations from spacecraft, disseminating to mission operations and broader SDA community via UDL, with exploration of potential direct integration pathways with specialized consumers (e.g., Welder's Arc, SDA TAP Lab) for threat intelligence and catalog updates, determining catalog updates based on SDA intelligence, and managing HPC-S model updates and training with comprehensive mission data and HIL mod/sim; data flows and integration touchpoints; Phase I focuses on CONOPS development; Phase II implements operational systems; addresses ground integration, model improvement, and operational readiness.
     4. Payload-in-the-Loop M&S with EW Attack Injectors — sensor-agnostic simulation harness leveraging IA's SDA and EW modsim expertise; Phase I focuses on RF synthetic scenes via EWIRDB-like parametric threat models and EMoP-like scene generation; red-team EW attack injectors; uncertainty calibration using SIERO-like methods; scenario packs (Theater GPS jamming detection & geolocation, GEO emissions characterization, RPO proximity cueing); harness architecture supports Phase II expansion to SAR/EO/IR/HSI synthetic scene generators; observation-to-event pipeline validation; addresses feasibility validation, robustness under adversarial conditions, and custody/latency insights.
     5. HIL Testing Framework and ModSim CONOPS — bench validation with simulated threat scenarios; performance characterization (latency, power, thermal); robustness checks across scenario packs; observation-to-event pipeline testing; addresses feasibility validation, performance profiling, security readiness, and test methodology development.
     6. Integration-Ready Interfaces and Operator Digests — modality-agnostic schemas for edge summaries/evidence, health telemetry, and operator digests; preliminary interface design and data product definitions; addresses Phase II integration, operator trust, and future interoperability.

4) **1.02 Alignment with Topic Requirements (AIS Subtopic 2)**
   - Table 2 maps AIS requirements (integrated sensor-compute, multimodal fusion, reconfigurability, HPC-S, latency reduction, operator workload, custody, comms-denied resilience, unclassified Phase I, IA/classified readiness, transition/integration readiness) to solution elements.

5) **1.03 Data, Evaluation, & Metrics**
   - Data: synthetic RF scenes (EWIRDB-like parametric threat models via EMoP-like generation), lab/test data where available, simulated EW attack scenarios, bench traces, and performance characterization under varying operational conditions.
   - Metrics: per-component (latency, power/thermal/SWaP characterization, uncertainty quantification, catalog slice viability, interface conformance) and system-level (end-to-end detection-to-alert latency, alert quality under stress, robustness to simulated threats).
   - Concrete scenario examples:
     - Theater GPS jamming detection & geolocation: measure detection-to-alert latency and accuracy across varying signal conditions.
     - GEO emissions characterization: detect unusual emissions/behavior changes; measure timeliness and alert quality under simulated threat scenarios.
     - RPO (sim-only): emissions-based proximity cueing and keep-out zone enforcement; characterize decision latency.
   - Table 3: metrics/goals/methods for Payload, Catalog, M&S/HIL, Interfaces, and integrated system; includes latency, power/thermal, uncertainty quantification, robustness assessment, catalog slice viability, and interface validation.

6) **2.0 Phase I Technical Objectives**
   - Objective 1: SPECTRA HPC-S Feasibility (Modular Sensor-Compute Payload, RF instantiation) — R&D questions: What modality-agnostic plugin interfaces (front-end, feature extractors, model containers) are required? What latency and performance characteristics are feasible on candidate SoC/FPGA under SWaP/rad/thermal constraints? What lightweight signed config/update concept is viable? How do observations flow through the HPC-S to generate events? Feasibility Determination: Edge pipeline performance characterized; plugin API realized (stubs + example RF plugin); power/thermal profiles captured; signed-config/update concept documented and emulated in bench loop; observation-to-event processing pipeline validated.
   - Objective 2: SPECTRA Edge DB Feasibility (Cross-Modal Space Threat Catalog Schema + Edge Slice Feasibility, initial EW focus) — R&D questions: What schema supports cross-modal descriptors (RF, SAR/LIDAR/EO/IR/HSI) and observation/event products? What slice sizes/compression achieve onboard feasibility and manageable downlink bundles? How do observations and events flow through the Edge DB to update the catalog? Feasibility Determination: Slice storage footprint and compression characteristics assessed; downlink bundle sizes for alert/evidence evaluated; schema validated with RF threat models and EW descriptors in Phase I, extensible design documented for Phase II modalities; observation and event cataloging pipeline demonstrated.
   - Objective 3: SPECTRA Ground Processing CONOPS — R&D questions: What operational workflows enable Ground Processing to receive events/observations, disseminate to mission operations and broader SDA community via UDL, and explore potential direct integration pathways with specialized consumers (e.g., Welder's Arc, SDA TAP Lab), determine catalog updates, and manage model training? What are the data flows and integration touchpoints? Feasibility Determination: Preliminary CONOPS document produced; operational workflows and data flows diagrammed; integration points with mission operations, UDL, and potential specialized consumers identified; model update and training pipeline conceptualized.
   - Objective 4: Payload-in-the-Loop M&S + HIL Harness with EW Attack Injectors — R&D questions: What simulation fidelity (via EWIRDB-like/EMoP-like generators and IA's SDA/EW modsim expertise) is sufficient for Phase I custody and performance insights? How do red-team injectors drive realistic stress? What uncertainty quantification approaches are viable? Feasibility Determination: Sim/HIL harness executes RF scenarios with EW attack injectors; bench performance data captured; uncertainty quantification methods demonstrated; stability assessed across scenario packs; observation-to-event pipeline validated.
   - Objective 5: Interfaces, Operator Digests, and Integration Readiness — R&D questions: What modality-agnostic schemas (summaries/evidence/health) and operator digest formats best support Phase II integration? What interface design principles enable future interoperability? Feasibility Determination: Schemas validated via round-trip examples; operator digest exemplars produced; preliminary interface design notes compiled.
   - Objective 6: Test Harness Feasibility and CONOPS for SPECTRA DB and HPC-S — R&D questions: What test harness architecture enables comprehensive validation of SPECTRA Edge DB and SPECTRA HPC-S? What HIL simulation capabilities are required? What adversarial signal emitter concepts are viable for live testing? Feasibility Determination: Test harness architecture documented; HIL simulation framework design completed; adversarial signal emitter concepts and feasibility assessed; test plan and CONOPS for bench and potential live testing produced.
   - Objective 7: Robustness and Assurance — R&D questions: What adversarial resilience is achievable under simulated EW attacks? What memory-safe runtime pathway is viable for Phase I? Feasibility Determination: Red-team injectors applied in sim/HIL; system behavior and stability under stress characterized; memory-safe implementation pathway documented.
   - Objective 8: Integrated Feasibility Assessment and Phase II Readiness — Synthesis of feasibility findings across HPC-S, Edge DB, Ground Processing CONOPS, M&S/HIL, Test Harness, and Interfaces; integrated feasibility summary; risk register with CTEs and mitigation plan; Phase II roadmap for multimodal expansion (SAR/EO/IR/HSI), prototype maturation, environmental testing, and validation pathways.

7) **3.0 Phase I Statement of Work (Base and Option)**
   - **Objective-to-Task Mapping (Base SoW):**
     - Objective 1 (HPC-S Feasibility) ← T2, T4, T8
     - Objective 2 (Edge DB Feasibility) ← T2, T3, T9
     - Objective 3 (Ground Processing CONOPS) ← T2, T7
     - Objective 4 (Payload-in-the-Loop M&S + HIL) ← T3, T4, T5
     - Objective 5 (Interfaces & Operator Digests) ← T6, T10
     - Objective 6 (Test Harness Feasibility & CONOPS) ← T5, T11
     - Objective 7 (Robustness & Assurance) ← T4, T5, T12
     - Objective 8 (Integrated Feasibility & Phase II Readiness) ← T6, T7
   - Table 4 (Base, 6 months):
     - T1 Kickoff + Feasibility Plan (M1): finalize objectives, simulation/HIL plans, dataset/signal scope; define three-tier architecture (HPC-S, Edge DB, Ground Processing) and observation-to-event data flows.
     - T2 Architecture & Catalog Schema Trades (M2–M3): SPECTRA HPC-S plugin interfaces and compute architecture; SPECTRA Edge DB cross-modal threat catalog schema + slice/compression trades (initial EW focus, multimodal extensibility); SPECTRA Ground Processing CONOPS preliminary outline; observation-to-event data flow design.
     - T3 Simulation Harness + Scenario Packs (M3–M4): RF payload-in-the-loop integration leveraging IA's SDA/EW modsim expertise; synthetic RF scene generation; EW attack injectors; uncertainty quantification approach; observation and event data flow validation.
     - T4 HIL Plan + Initial Bench Characterization (M4–M5): Bench validation runs; performance characterization (timing, power, thermal); signed-config emulation; observation-to-event pipeline testing; robustness assessment under simulated threat scenarios.
     - T5 Test Harness Feasibility and CONOPS (M4–M5): Define test harness architecture for comprehensive validation of SPECTRA Edge DB and HPC-S; design HIL simulation framework; assess adversarial signal emitter concepts for live testing; produce test plan and CONOPS for bench and potential live testing; robustness evaluation methodology.
     - T6 Interface Design & Operator Digest Prototyping (M5–M6): Modality-agnostic schemas for edge summaries/evidence and health telemetry; operator digest exemplars; preliminary interface design notes; round-trip validation examples.
     - T7 Feasibility Indicators + Evidence Package (M5–M6): Performance characterization, uncertainty quantification results, slice viability, interface validation; data capture for V&V; three-tier architecture feasibility summary; test harness readiness assessment.
     - T8 Phase II Design & Transition Readiness Outline (M6): prototype maturation plan; interoperability and standards considerations; SPECTRA Ground Processing CONOPS refinement plan; test harness and adversarial emitter development roadmap; risk register with CTEs and mitigation plan.
   - Table 5 (Option, 6 months):
     - T9 Advance Payload Compute Trades & Signed-Config Emulation: heterogeneous compute evaluation; rad-tolerant options; thermal throttling/graceful degradation.
     - T10 Expand Catalog Slice Compression & Retrieval: advanced compression techniques; downlink bundle efficiency assessment.
     - T11 Mid-Fidelity Operator Digest Prototyping: role/phase-aware UI exemplars; turnover clarity demonstrations.
     - T12 Adversarial Signal Emitter Development: Feasibility study and preliminary design for adversarial RF signal emitters for live testing; integration concepts with test harness; safety and regulatory considerations.
     - T13 Architecture & Security Planning for Phase II: memory-safe runtime pathway; on-orbit update concepts; advanced interoperability pathways.
   - Forward look to Phase II: multimodal sensor fusion (SAR/EO/IR/HSI) under same payload-compute framework; prototype maturation with environmental testing; validation exercises; extended catalog integration and interoperability pathways.

8) **1.3 Related Work**
   - Table 6: Prior work (COSMIAC PIGEON heritage, IA autonomy/simulation programs, space threat catalogs with EW focus, edge ML frameworks, HIL/M&S tools); differentiation (modality-agnostic plugin architecture, integrated sensor-compute-catalog flow, uncertainty-aware edge decisions, cross-modal extensibility).

9) **2.0 Key Personnel and Workshare**
   - Table 7: PI and key SMEs with relevant DoD/DARPA/space programs and publications.
   - COSMIAC (UNM) expertise: RF front-end design/integration (PIGEON heritage), edge ML threat detection prototyping, radiation test planning/mitigation, FPGA acceleration options, smallsat/ground-station integration, environmental testing, HIL bench setup/execution, bench hardware/instrumentation, power/thermal profiling, security/update feasibility support, interface schema validation.
   - Interactive Aptitude (IA) expertise: SDA and EW modeling/simulation expertise, sensor-agnostic payload-in-the-loop simulation framework and scenario packs, synthetic RF scene generation (EMoP-like approaches), red-team EW attack injectors, HIL orchestration/control software and data collection pipelines, uncertainty gating methods (SIERO-like), Cross-modal Space EW Catalog schema and development leadership, edge slice feasibility, data product schema design, edge summary/evidence packaging, preliminary CONOPS, metrics and ablation studies, Showcase artifacts.

10) **3.0 Commercialization/Transition Plan Summary**
    - 3.1 Overview; 3.1.1 DoD/USSF transition pathway; 3.1.2 transition plan by phase (Phase I–III); 3.1.3 engagement strategy (USSF, NRO, commercial constellation operators, SDA community);
    - 3.1.4 Commercial/dual-use expansion:
      - Phase I RF anomaly detection and catalog products for unclassified space operations and commercial constellation operators; Phase II/III multimodal expansion (SAR/EO/IR/HSI) for enhanced threat detection across modalities.
      - Safety-critical anomaly detection for automotive (fighter jets, commercial airliners), maritime, aviation, and critical infrastructure; multimodal sensor fusion for improved confidence and reduced false-alert rates.
      - HIL simulation and test toolchains for multimodal EW robustness evaluations; training products for operations and test teams; modality-agnostic framework enables rapid customization for new sensor types.
    - 3.1.5 Competitive differentiation: modality-agnostic plugin architecture (enables rapid sensor expansion), integrated sensor-compute-catalog flow (reduces latency and operator workload), uncertainty-aware edge decisions (improves trust and assurance), multimodal fusion at the edge (enhances detection confidence).
    - 3.1.6 Risks/mitigations: SWaP/thermal/radiation (derive budgets/margins, evaluate rad-tolerant compute, prototype thermal throttling); integration complexity (modular interfaces, memory-safe implementations, deterministic latency paths); data poisoning/robustness (onboard anomaly detection, signed models/configs, uncertainty-gated autonomy, simulation-based red-teaming).
    - 3.1.7 Revenue/scaling model: Phase II quantitative targets (>50% decision latency reduction, ≥25% operator workload reduction, −25–35% custody gaps, −30–40% time-to-classification vs. baselines); Phase II/III maturation to flight-like prototype and limited over-the-air exercises; standards alignment (SOSA, CCSDS/BM-C2) for broader adoption and interoperability.
    - Table 9: commercialization timeline milestones (Q4 2025 – Q4 2027).

11) **4.0 Facilities/Equipment**
    - Computing resources (COSMIAC lab, IA cloud/on-prem), HIL bench hardware (AWG, instrumentation), simulation infrastructure (SDA/EW modsim frameworks), security controls (memory-safe runtime, signed updates, NIST/FIPS as applicable).

12) **5.0 References**
    - Citations covering RF payloads, edge ML, sensor fusion, space EW, catalog systems, uncertainty quantification, and relevant standards.

---

### Content Mapping (Crosswalk)
- Problem Context → 1.0; Scenario (contested space ops, comms-denied, diverse threats including RF/EW, kinetic, maneuver, signature anomalies) → 1.0; Figures 1–3 illustrate architecture, payload, and operator digest.
- Core Subsystems & Phase I Initiatives → 1.0 Executive Summary:
  - SPECTRA HPC-S (Modular Sensor-Compute Payload) → multimodal-ready plugin architecture, performance characterization, RF Phase I instantiation; meets: Integrated Sensor-Compute, Reconfigurability, HPC-S, Latency Reduction.
  - SPECTRA Edge DB (Cross-Modal Space Threat Catalog) → edge slices, downlink efficiency, extensible schema, SOSA-compliant design; meets: Multimodal Fusion Support, Operator Workload Reduction, Comms-Denied Resilience.
  - SPECTRA Ground Processing → CONOPS development, dissemination via UDL, exploration of specialized consumer integration (e.g., Welder's Arc); meets: Ground Integration, Model Management, Operational Readiness.
  - Payload-in-the-Loop M&S with EW Attack Injectors → sensor-agnostic simulation harness, RF Phase I, multimodal Phase II; meets: Feasibility Validation, Robustness/Trust, Uncertainty Quantification.
  - HIL Testing Framework and ModSim CONOPS → bench validation, performance characterization, robustness assessment; meets: Test Methodology Development, Security Readiness, Feasibility Validation.
  - Integration-Ready Interfaces and Operator Digests → modality-agnostic schemas, preliminary interface design; meets: Phase II Integration, Operator Trust, Future Interoperability.
  - Test Harness Feasibility and CONOPS → comprehensive validation architecture, HIL simulation framework, adversarial signal emitter concepts; meets: Validation Readiness, Live Testing Pathways.
- Topic Compliance → 1.02 Table 2 explicitly maps AIS requirements to solution elements; includes unclassified Phase I compliance and classified Phase II readiness.
- Evaluation Plan → 1.03 defines data sources, metrics, and scenario examples; emphasizes performance characterization and robustness assessment without over-committing to specific methodologies.
- Technical Objectives → 2.0 enumerates eight objectives with R&D questions and feasibility criteria; Objective-to-Task Mapping shows Base SoW coverage of all objectives.
- SoW & Schedule → 3.0 Tables 4–5 provide Base/Option tasks (T1–T8 Base, T9–T13 Option) with explicit objective mapping and logical task sequencing.
- Transition & Commercialization → 3.0 provides DoD/USSF pathway, engagements, dual-use markets, differentiation, risks, and revenue model with SOSA/CCSDS/BM-C2 standards alignment; Table 9 timeline.
- Organizational Capacity → Related Work (1.3), Key Personnel (2.0), Facilities/Equipment (4.0), and References (5.0) substantiate credibility and readiness.

---

### Reuse Notes (for SPECTRA proposal writing)
- Open with a strong problem-context + scenario (contested space ops, comms-denied, multimodal threats) that directly motivates the feature set and evaluation plan. Emphasize that SPECTRA is a multimodal architecture, not just RF.
- Define 5 named innovations; for each: challenge, DoI/novelty, methods, evidence/TRLs, and operational impact. Include figures (architecture, payload, operator digest). Clearly distinguish Phase I RF instantiation from Phase II multimodal expansion.
- Provide an early crosswalk table (Topic Alignment) and a focused metrics table. Highlight how Phase I RF work establishes baselines and plugin architecture for Phase II modalities.
- Articulate Phase I objectives with R&D questions and feasibility determination criteria; align SoW tasks/milestones to those objectives. Frame objectives as establishing foundations for multimodal expansion.
- Include transition path by phase (I/II/III), concrete stakeholder engagements (USSF, NRO, SDA community), and dual-use expansion logic. Emphasize Phase II multimodal roadmap and commercial scalability.
- Close with facilities, personnel, and references to demonstrate capability and compliance.
- Use present-tense capability framing ("SPECTRA delivers multimodal threat detection…", "Payload architecture supports RF/SAR/EO/IR/HSI…") and power verbs (accelerates, fuses, triage, calibrates, enables, expands).
- Emphasize integration-ready language and prototype maturity signals (TRL levels, bench evidence, simulation validation). Stress modality-agnostic design and plugin extensibility.

---

### Figures and Tables (as referenced)
- Figures: 1 (End-to-end system architecture, sensor→edge compute→fusion→downlink→catalog), 2 (Payload block diagram, RF front-end + compute + interfaces), 3 (Operator digest and alert UI exemplar).
- Tables: 1 (Degree of Innovation), 2 (AIS Topic/Requirement Alignment), 3 (Metrics), 4 (Base SoW), 5 (Option SoW), 6 (Related Work), 7 (Key Personnel), 9 (Commercialization Timeline).

