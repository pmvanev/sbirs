# AIS Phase I — Brainstormed Scope Ideas (IA + COSMIAC)

This list groups big‑picture Phase I ideas by AIS Focus Area, leveraging Interactive Aptitude (IA) strengths in AI/ML, simulation, RL, and software, and COSMIAC strengths in radiation‑tolerant embedded systems, RF/sensors, smallsat development, and test facilities. Each idea includes: concept, Phase I activities/deliverables, success signals/metrics, and IA/COSMIAC roles. Where helpful, bracketed tags [R#] tie ideas to key references summarized in ref_summaries.md.

---

## Focus Area 1 — Edge Computing & Algorithms

1) Onboard Threat and Maneuver Classification with Safe RL “Action Broker”
- Concept: Fuse kinematic + RF cues into an onboard classifier; couple to a safe RL “action broker” selecting evasive/observe/hold actions with constraints and explainability for rules‑of‑engagement and debris minimization. [R1][R2]
- Phase I: data model + synthetic generation; mobile‑friendly models; action broker with explicit constraint layer; verification harness and counterfactual/explanation logging; on‑orbit logging schema and downlink packaging for operator analysis and RL retraining datasets. [R3][R5][C1][C3]
- Metrics: classification F1>0.9 on synthetic adversary maneuvers; constraint violation ~0; operator workload proxy −25%. [R2][R3]
- Roles: IA — models, broker, verification; COSMIAC — compute footprint study, secure boot/root‑of‑trust feasibility. [R5][R6]
- Why priority: Directly hits onboard threat analytics and ≥50% latency/≥25% workload goals with ROE/debris‑minimizing autonomy under comms denial.

2) Data Poisoning and OOD Resilience on the Edge
- Concept: Onboard triage with OOD detectors, adversarial hardening, and sensor cross‑checks; memory‑safe language prototypes and zero‑trust enclaves for model execution and updates. [R3][R5]
- Phase I: evaluate OOD/adversarial defenses under SWaP; prototype enclave execution path; certifiable Space MLOps update concept for models. [R5][R6][C1][C2]
- Metrics: AUC>0.9 under poisoning; enclave overhead <20% compute; recovery time <10 s; secure update roll‑back path. [R5]
- Roles: IA — defenses, enclave pipeline; COSMIAC — trust anchors, key mgmt, firmware chain‑of‑custody. [R5]
- Why priority: Solicitation calls resilience to data poisoning, memory‑safe languages, and zero‑trust; de‑risks safety‑critical autonomy and on‑orbit updates.

3) POLARIS‑trained On‑Board RL Mission Autonomy (Power/Sensing/Downlink)
- Concept: Extend IA’s POLARIS RL training (Basilisk + Gymnasium) to GEO/XGEO/cislunar regimes and deploy an onboard policy that jointly optimizes solar charging, sensor tasking, tip‑and‑cue, and comms downlink while respecting safety/ITAR constraints. [R1][R2][R3]
- Phase I activities/deliverables:
  - Basilisk environment extensions (GEO→cislunar), synthetic scenarios, and domain randomization for comms‑denied ops. [R3]
  - Train/evaluate RL policies vs. baselines; generate traceable performance logs for latency/workload targets. [R2]
  - Safety shield + rule‑based guardrails and formal checks for “never exceed” constraints; initial hazard log and V&V plan. [R3]
  - HIL feasibility plan with COSMIAC prototype compute board; edge resource budget and thermal map. [R5][R6][C1][C6]
- Success signals/metrics: >50% reduction in decision latency vs. ground‑loop baseline; energy margin/downlink throughput gains; safe‑action rate >99.9%; robust to comms loss. [R1][R6]
- Roles: IA — RL/POLARIS models, safety shields, M&S; COSMIAC — prototype compute board selection (rad‑tolerant SoC/FPGA), HIL plan, thermal/power envelope. [R5]
- Why priority: Achieves AIS latency/workload targets via onboard autonomy; leverages IA POLARIS; strong Phase I M&S + HIL path to Phase II.

4) FPGA-Resident RL Policy Inference + On-Orbit Weight Update Protocol
- Concept: Map a compact RL policy (e.g., actor network) to FPGA/SoC for low-latency, low-power inference; define a secure, certifiable mechanism to update weights/biases in flight via signed ground uploads with rollback. [R3][R5][R6]
- Phase I: evaluate quantization/pruning for FPGA; prototype HLS/HDL mapping for core layers; define update container/signing/rollback; SEU/SET impact analysis on fabric and mitigations; ground-to-onboard update demo-in-the-loop. [R5][R6][C1][C2][C6]
- Metrics: inference latency <10 ms; power <X W with >Y% savings vs. CPU; successful signed update + rollback in HIL; fault injection shows no unsafe action. [R4][R5]
- Roles: IA — model compression, HLS mapping, update tooling; COSMIAC — FPGA/rad-tolerant SoC feasibility, SEU test plan, secure boot/roots of trust. [R5]
- Why priority: Advances edge autonomy feasibility under SWaP and addresses certifiable on-orbit model update—a solicitation concern tied to trustworthy Space MLOps. [R3][R5][R6]


5) Cislunar Visualization + RL Training Toolchain
- Concept: Produce cislunar‑grade visualizations and simulators tied to POLARIS for planning, replay, and showcase; include decision‑timeline overlays and ROE constraints. [R1][R2][R3]
- Phase I: visualization tool, scenario pack, and CONOPS storyboard; “what‑if” latency/workload analysis hooks; exportable figures for the Showcase. [R2]
- Metrics: end‑to‑end sim‑to‑policy loop; stakeholder usability ≥4/5; clear traceability to USSF objectives. [R2]
- Roles: IA — tools; COSMIAC — scenario realism review, ops constraints.
- Why priority: AIS Phase I emphasizes CONOPS, modeling/simulation, and cislunar visualization—this yields Showcase‑ready artifacts and evaluation hooks.

6) Neuromorphic/FPGA Edge Inference Feasibility for Anomaly Detection
- Concept: Investigate spiking NN or FPGA‑accelerated anomaly detectors for ultra‑low‑power custody maintenance with radiation considerations. [R5][R6]
- Phase I: port a lightweight anomaly kernel to FPGA/spiking sim; compare watts/inference vs. CPU/GPU; radiation effects review and mitigation posture drawing on COSMIAC campaigns. [R5][C1][C6]
- Metrics: 3–10× energy/inference; accuracy within 5% of CPU ref; draft radiation risk/mitigation plan. [R5]
- Roles: IA — models/algorithms; COSMIAC — FPGA/neuromorphic feasibility, radiation test plan.
- Why priority: Neuromorphic is a desired tech; Phase I feasibility quantifies energy gains and radiation risk—secondary to core autonomy/resilience.

Ref‑informed priorities: emphasize comms‑denied autonomy and debris‑minimizing actions (R1), doctrinal alignment to USSF decision advantage (R2), and trustworthy MLOps + V&V for safety‑critical edge AI (R3,R5,R6).

---

## Focus Area 2 — Sensor Payloads

1) Passive RF SDA Micro‑Payload with On‑Sensor Pre‑Processing (HPC‑S)
- Concept: COSMIAC reconfigurable passive RF front‑end (SDR/FPGA) with on‑sensor feature extraction; IA onboard ML for maneuver/intent cues and compression for comms‑denied ops. [R2][R6][C1][C4][C7]
- Phase I: RF link budgets; feature pipelines (Doppler, TDOA/FDOA, emitter characterization); model sizing for on‑sensor inference; data reduction/compression. [R6]
- Metrics: custody persistence +X% in sims; compression ≥10× with <5% utility loss; inference latency <100 ms. [R6]
- Roles: COSMIAC — RF front‑end concept, FPGA mapping; IA — ML models, compression, fusion. [R6]
- Why priority: Explicitly called tech (passive RF, HPC‑S); on‑sensor processing cuts timelines and improves custody/attribution.

2) Software‑Defined, Reconfigurable Multi‑Modal Sensing Concept
- Concept: Define a payload that can retask between passive RF and IR/hyperspectral (sim in Phase I) with IA triage deciding when/where to collect; supports predictive “tip & cue.” [R2][R6]
- Phase I: sensor trade studies; reconfig profiles; tasking policies; on‑sensor compute budget. [R5][C4][C5][C7]
- Metrics: ≥30% fewer wasted collects; maneuver change detection ΔF1>0.1. [R3]
- Roles: IA — triage/tasking; COSMIAC — reconfigurable sensor architecture/constraints.
- Why priority: Software‑defined/reconfigurable payloads are solicited; boosts tip‑and‑cue efficiency across missions.

3) Hyperspectral Change Detection and On‑Sensor Compression
- Concept: Rapid change cues (plumes, panel reorientation) with in‑band compression and ROI prioritization for downlink‑limited conditions. [R6]
- Phase I: synthetic HSI generation; edge kernels; ROI prioritization policies for downlink. [R3][R6]
- Metrics: change detection latency <10 s; ROI PSNR/SSIM within 5% loss; downlink savings ≥10×.
- Roles: IA — algorithms/policies; COSMIAC — edge hardware mapping and memory bandwidth plan. [R5]
- Why priority: Supports attribution/change detection under downlink constraints; aligns with onboard compression and HPC‑S patterns.

4) LIDAR/Active Sensing Custody Simulation with Fusion Hooks
- Concept: Simulate LIDAR for close‑in custody and fuse with RF/optical to improve track continuity during maneuvers. [R3]
- Phase I: sensor models, fusion study, degraded‑sensing scenarios; design envelope for power/thermal. [R5]
- Metrics: custody break rate −25% in maneuver scenarios; fusion latency <200 ms.
- Roles: IA — fusion/M&S; COSMIAC — power/thermal envelope, mounting/field‑of‑regard constraints.
- Why priority: Improves custody through maneuvers; complements multi‑modal fusion central to SDA.

Ref‑informed priorities: multi‑sensor fusion for SDA and attribution (R2,R3), onboard processing to cut timelines (R6), and hardware tradeoffs grounded in space processor data (R5).

---

## Focus Area 3 — Bus Design

1) Safe Collision Avoidance and Evasive Maneuver Executive
- Concept: Guidance executive integrating conjunction alerts with safe maneuver templates; leverage MPC‑style controllers for constraint‑aware RPOD/evasion. [R4]
- Phase I: maneuver library; verification harness; delta‑V budget trade space; debris‑minimizing ROE. [R1][R4]
- Metrics: 0 constraint violations; decision latency <5 s; custody maintained ≥80% during avoidance.
- Roles: IA — algorithms/verification; COSMIAC — propulsion/ADCS constraints and actuator models.
- Why priority: Autonomous collision avoidance is explicitly required; MPC‑style methods provide constraint‑respecting, debris‑minimizing evasions.

2) Rad‑Tolerant Compute Stack with Root‑of‑Trust and Memory‑Safe Runtime
- Concept: COSMIAC prototypes rad‑tolerant compute (RISC‑V/FPGA SoC + TMR/ECC) with secure boot; IA provides memory‑safe runtime (e.g., Rust/WASM) and enclave execution path. [R5]
- Phase I: block diagram, parts/availability, SEU/SET mitigation approach, secure boot chain; sample micro‑services; Space MLOps update plan; secure FPGA weight/bias update protocol with signed container and rollback. [R5][R6][C5][C6][C1]
- Metrics: boot‑to‑mission <10 s; SEU tolerance plan; enclave perf overhead <20%.
- Roles: COSMIAC — hardware concept; IA — runtime + app containerization.
- Why priority: Directly addresses radiation‑tolerant edge, memory‑safe languages, zero‑trust, and certifiable update pathways.

3) Modular Autonomy Manager for Power/Thermal/Compute Load‑Shedding
- Concept: Software “vehicle manager” orchestrating compute throttling, sensor duty cycling, thermal protection by mission phase and threat posture; integrates with Edge policies. [R5][R6]
- Phase I: architecture, state machine + policy hooks, thermal/power budget models; hardware abstraction layer. [R5][C5]
- Metrics: thermal violations ≥80% reduction; mission utility loss <5%; autonomy safety incidents = 0 in sim.
- Roles: IA — autonomy stack; COSMIAC — bus interfaces, thermal/power models, component selection.
- Why priority: Matches all‑of‑vehicle autonomous optimization, autonomous load‑shedding, and thermal management for edge compute.

4) High Delta‑V Mission Profile Study for Rapid Evasion/Retasking
- Concept: Co‑design autonomy policies with high‑delta‑V envelopes; quantify gains in threat response for co‑orbital harassment and proximity threats. [R1][R2]
- Phase I: mission analysis; policy coupling; delta‑V vs. custody/latency curves.
- On-Orbit Data Logging & Reporting Protocol: schema for action traces, sensor snippets, and health/decision telemetry; secure downlink packaging for operator analysis and RL retraining datasets. [R3][R5]

- Metrics: intercept‑avoidance probability +X%; time‑to‑safe‑state <5 min in worst cases. [R2]
- Roles: IA — policy coupling/M&S; COSMIAC — propulsion options/thermal impacts.
- Why priority: High delta‑V is a desired capability; this analysis couples autonomy with propulsion envelopes to quantify feasibility.

Ref‑informed priorities: constraint‑respecting maneuver logic (R4), resilience and rapid decision cycles (R1,R2), and heterogenous compute/secure update paths (R5,R6).

---

## Cross‑Cutting Enablers (apply across Focus Areas)
- CONOPS & Diagrams: GEO→cislunar operating concept, architecture, and integration storyboard for the Showcase; align language to USSF doctrine. [R2]
- Modeling & Simulation: unified Basilisk scenario pack with RF/optical/LIDAR models; stress cases for comms‑denied ops and proximity threats. [R1][R3]
- Space MLOps & V&V: pipeline for dataset curation, synthetic data, active learning, performance monitoring, certifiable on‑orbit updates, secure rollback. [R3][R5][R6][C1]
- HIL/Prototype Test Plan: bench test outline at COSMIAC (power/thermal/SEU injection/SDR), with data capture for Phase II gating. [R5][C6][C4]
- Security & Compliance: zero‑trust enclaves, SBOM, secure update pathways; ITAR and STTR workshare planning. [R5]
- Metrics & Eval: latency reductions (>50%), operator workload proxy (≥25% reduction), custody continuity, zero constraint‑violation target. [R2][R6]

---

## Example Integrated Phase I Threads (IA + COSMIAC)
- Thread A (Edge+Bus): POLARIS policy + autonomy manager + safe action broker, with HIL feasibility on a rad‑tolerant SoC/FPGA concept. [R5][R6][C1][C5][C6]
- Thread B (Sensors+Edge): Passive RF micro‑payload with on‑sensor features and triage; compression + tip‑and‑cue to reduce downlink. [R2][R6][C4][C7][C1]
- Thread C (All‑Up Sim): Cislunar scenario pack with visualization and CONOPS, reporting latency/workload/custody metrics for Showcase. [R2][R3]

---

## Phase II Trajectory Pointers
- Mature the HIL prototype into an integrated flight‑like payload/processor; thermal‑vac and radiation testing; limited over‑the‑air ground station exercises via COSMIAC. [R5]
- Advance TRL for onboard autonomy, secure runtime, and on‑sensor HPC‑S; expand to multi‑sat coordination and cross‑vendor bus interfaces. [R6]

---

## Reference linkage (R#)
- R1: The Economist — satellite‑on‑satellite threats, comms‑denied ops, debris minimization
- R2: USSF Space Warfighting Framework — doctrine, decision advantage, SDA/SC/SBM
- R3: RAND — AI/ML for SDA; data, domain shift, V&V, trust, synthetic data
- R4: IEEE AERO 2023 — MPC for RPOD; constraint‑aware controllers for onboard maneuvering
- R5: NASA Current Technology in Space v4 — hardware tradeoffs, Space MLOps, certifiable updates
- R6: Lockheed Martin AIAA — on‑board AI/ML mission processing patterns and performance