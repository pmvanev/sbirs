# AIS Phase I — Brainstormed Scope Ideas (IA + COSMIAC)

This list groups big‑picture Phase I ideas by AIS Focus Area, leveraging Interactive Aptitude (IA) strengths in AI/ML, simulation, RL, and software, and COSMIAC strengths in radiation‑tolerant embedded systems, RF/sensors, smallsat development, and test facilities. Each idea includes: concept, Phase I activities/deliverables, success signals/metrics, and IA/COSMIAC roles. Where helpful, bracketed tags [R#] tie ideas to key references summarized in ref_summaries.md.

## Summary of Scope Ideas

| ID     | Title                                                            | Brief summary                                                                                | Section ref            | Refs                 | How it meets real ops need                                                  | IA/COSMIAC fit | USSF relevance | Commercial potential                                         |
| ------ | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------- | -------------------- | --------------------------------------------------------------------------- | -------------- | -------------- | ------------------------------------------------------------ |
| FA1-1  | Onboard Threat & Maneuver Classification + Safe RL Action Broker | Onboard classifier fused with safe, constraint-aware action selection (evasive/observe/hold) | Focus Area 1, item 1   | R1,R2,R3,R5,C1,C3    | Cuts kill-chain latency under comms denial; debris/ROE-constrained autonomy | 5/5            | 5/5            | Constellation autonomy; industrial/defense robotics          |
| FA1-2  | Data Poisoning & OOD Resilience on the Edge                      | OOD/adversarial defenses, enclave execution, certifiable model updates                       | Focus Area 1, item 2   | R3,R5,C1,C2          | Trustworthy autonomy under attack; safe on-orbit updates                    | 5/5            | 5/5            | Safety-critical edge AI for vehicles, drones, infrastructure |
| FA1-3  | POLARIS On‑Board RL Mission Autonomy                             | Jointly optimizes power, sensing, tip‑and‑cue, and downlink with safety shields              | Focus Area 1, item 3   | R1,R2,R3,R5,R6,C1,C6 | Reduces decision latency; sustains mission under comms loss                 | 5/5            | 5/5            | Fleet ops optimization for commercial constellations         |
| FA1-4  | FPGA‑Resident RL Inference + Secure Weight Updates               | Quantized RL policy on FPGA/SoC; signed, rollback‑safe on‑orbit updates                      | Focus Area 1, item 4   | R3,R4,R5,R6,C1,C2,C6 | Meets SWaP and safety for on‑board autonomy; certifiable updates            | 5/5            | 4/5            | Edge AI accelerators and secure update pipelines             |
| FA1-5  | Cislunar Visualization + RL Training Toolchain                   | Scenario/vis tools with decision‑timeline overlays and CONOPS storyboards                    | Focus Area 1, item 5   | R1,R2,R3             | Showcase‑ready evidence and CONOPS for evaluators                           | 4/5            | 4/5            | Simulation/visualization software products                   |
| FA1-6  | Neuromorphic/FPGA Edge Anomaly Detection                         | Ultra‑low‑power anomaly kernels on neuromorphic/FPGA with rad considerations                 | Focus Area 1, item 6   | R5,R6,C1,C6          | Maintains custody with minimal power; extends endurance                     | 4/5            | 3/5            | Low‑power monitoring in IoT/space/industrial                 |
| FA1-7  | Collaborative Distributed Tip‑and‑Cue (Multi‑Host)               | Crosslink‑aware coordination to maintain custody and speed classification                    | Focus Area 1, item 7   | R2,R3,R5,C4,C7       | Improves custody and attribution timelines across assets                    | 4/5            | 5/5            | Multi‑drone/sensor fleet coordination                        |
| FA1-7a | MARL for Collaborative Tip‑and‑Cue (CTDE)                        | Centralized‑training, decentralized‑execution MARL for coordinated tasking                   | Focus Area 1, item 7a  | R2,R3,R4,R5          | Learns robust coordination under bandwidth/energy constraints               | 4/5            | 4/5            | Autonomous fleet MARL (UAV, maritime, logistics)             |
| FA1-8  | Onboard PNT Integrity Monitors                                   | GNSS spoofing/jamming detection and integrity gating of autonomy                             | Focus Area 1, item 8   | C1,C2,R3             | Prevents unsafe maneuvers; ensures nav trust under attack                   | 4/5            | 5/5            | GNSS integrity for UAV/automotive/IoT                        |
| FA1-9  | Intent Attribution (Behavior Models + KG)                        | Fuse kinematics + RF + history to infer hostile vs benign intent with XAI                    | Focus Area 1, item 9   | R1,R2,R3,C1,C7       | Speeds ROE decisions; reduces operator burden                               | 4/5            | 5/5            | Threat attribution in cyber/physical security                |
| FA2-1  | Passive RF SDA Micro‑Payload (HPC‑S)                             | Reconfigurable passive RF front‑end with on‑sensor features and triage                       | Focus Area 2, item 1   | R2,R6,C1,C4,C7       | Persistent custody and attribution when optical is degraded                 | 5/5            | 5/5            | Spectrum monitoring, commercial SSA services                 |
| FA2-2  | Software‑Defined Reconfigurable Multi‑Modal Sensing              | Retask between RF/IR/HSI; policy‑driven tip‑and‑cue and collection                           | Focus Area 2, item 2   | R2,R6,R5,C4,C5,C7,R3 | Fewer wasted collects; better maneuver/change detection                     | 4/5            | 4/5            | Software‑defined sensing for EO/IR markets                   |
| FA2-3  | Hyperspectral Change Detection + On‑Sensor Compression           | Rapid change cues with ROI prioritization and downlink savings                               | Focus Area 2, item 3   | R6,R3,R5             | Attribution under downlink constraints; faster alerting                     | 4/5            | 4/5            | Ag/energy/mining EO analytics                                |
| FA2-4  | LIDAR/Active Custody Fusion Simulation                           | LIDAR models and fusion with RF/optical to maintain custody in maneuvers                     | Focus Area 2, item 4   | R3,R5                | Reduces custody breaks; supports close‑in ops                               | 4/5            | 4/5            | Robotics/automotive active sensor fusion                     |
| FA2-5  | Sensor Self‑Calibration & Health Monitoring                      | Onboard calibration, drift detection, and diagnostics                                        | Focus Area 2, item 5   | R5,C4,C7             | Maintains sensing quality and trust over long missions                      | 4/5            | 4/5            | Predictive maintenance for sensors/IoT                       |
| FA3-1  | Safe Collision Avoidance & Evasive Executive                     | Constraint‑aware maneuver library and verification harness (MPC‑style)                       | Focus Area 3, item 1   | R1,R4                | Real‑time avoidance with debris‑minimizing ROE                              | 4/5            | 5/5            | Deconfliction for UAV/space traffic mgmt                     |
| FA3-2  | Rad‑Tolerant Compute + Root‑of‑Trust + Memory‑Safe Runtime       | Rad‑tolerant SoC/FPGA with secure boot and Rust/WASM‑class runtime                           | Focus Area 3, item 2   | R5,R6,C5,C6,C1       | Secure, resilient edge compute for autonomy and updates                     | 5/5            | 5/5            | Safety‑critical embedded platforms                           |
| FA3-3  | Modular Autonomy Manager (Power/Thermal/Compute)                 | Vehicle manager for throttling, duty cycling, and protection policies                        | Focus Area 3, item 3   | R5,R6,C5             | Keeps edge AI within thermal/power envelopes; mission continuity            | 5/5            | 5/5            | Platform power/thermal orchestration                         |
| FA3-4  | High Delta‑V Mission Study + Action Telemetry Protocol           | Co‑design autonomy with propulsion envelopes; secure action/health logging                   | Focus Area 3, item 4   | R1,R2,R3,R5          | Faster threat response; operator evidence and retraining data               | 4/5            | 4/5            | Mission planning + telemetry analytics                       |
| FA3-5  | Run‑Time Assurance (Simplex) Safety Cage                         | Verified safety monitor + certified fallback controller                                      | Focus Area 3, item 5   | R4,R3                | Zero invariant violations; certifiable autonomy                             | 4/5            | 5/5            | Certifiable autonomy middleware                              |
| CC-1   | CONOPS & Diagrams                                                | Operating concept and architecture aligned to USSF doctrine                                  | Cross‑Cutting Enablers | R2                   | Clear mission alignment; showcase‑ready artifacts                           | 5/5            | 5/5            | Consulting/tools for space CONOPS                            |
| CC-2   | Modeling & Simulation                                            | Unified Basilisk scenario pack and stress cases                                              | Cross‑Cutting Enablers | R1,R3                | Quantitative evidence for feasibility and metrics                           | 5/5            | 5/5            | Simulation frameworks                                        |
| CC-3   | Space MLOps & V&V                                                | Dataset curation, synthetic data, active learning, on‑orbit updates                          | Cross‑Cutting Enablers | R3,R5,R6,C1          | Trusted autonomy lifecycle; certifiable updates                             | 5/5            | 5/5            | Space MLOps platform                                         |
| CC-4   | HIL/Prototype Test Plan                                          | Bench tests at COSMIAC (power/thermal/SEU/SDR) with data capture                             | Cross‑Cutting Enablers | R5,C6,C4             | De‑risks Phase II; validates hardware/software                              | 5/5            | 5/5            | Test services and fixtures                                   |
| CC-5   | Security & Compliance                                            | Zero‑trust enclaves, SBOM, secure updates; ITAR/STTR workshare                               | Cross‑Cutting Enablers | R5                   | Operable and compliant in defense context                                   | 4/5            | 5/5            | Secure update/compliance tooling                             |
| CC-6   | Metrics & Evaluation                                             | Latency (>50%), workload (≥25%) and custody metrics                                          | Cross‑Cutting Enablers | R2,R6                | Mission‑relevant, decision‑grade evidence                                   | 5/5            | 5/5            | Analytics dashboards                                         |
| CC-7   | DTN/BPv7 + Downlink QoS                                          | Prioritized action/evidence/health data; survive comms denial                                | Cross‑Cutting Enablers | R2                   | Reliable alerts under intermittent links                                    | 4/5            | 5/5            | Space‑optimized DTN middleware                               |
| CC-8   | ROE‑Aware Operator Digest                                        | Concise, explainable action summaries with counterfactuals                                   | Cross‑Cutting Enablers | R2                   | Reduces operator workload; supports ROE decisions                           | 4/5            | 5/5            | Operator decision aids                                       |
| CC-9   | Standards/Interoperability Hooks                                 | CCSDS/BM‑C2 aligned data and interfaces                                                      | Cross‑Cutting Enablers | R2                   | Smooth Phase II/III integration and transition                              | 4/5            | 5/5            | Integration adapters                                         |


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


7) Collaborative Distributed Tip‑and‑Cue Across Multiple Hosts
- Concept: Policies that coordinate tasking across multiple friendly spacecraft via crosslinks to maintain custody and reduce time‑to‑classification; integrates onboard triage and priority queues for evidence sharing. [R2][R3]
- Phase I: design distributed tasking policies and conflict resolution; simulate crosslink‑limited coordination; evaluate robustness under comms degradation; interface hooks to BM/C2. [R2][R5]
- Metrics: time‑to‑classification −30%; custody gaps −25%; crosslink utilization within power budget; operator interventions −25%. [R2][R3]
- Roles: IA — distributed policy and M&S; COSMIAC — crosslink/SDR feasibility and power/thermal envelopes. [C4][C7]
- Why priority: “Tip & cue between SDA and coordination functions” is explicitly desired; directly improves custody and decision timelines under contested conditions.

7a) MARL for Collaborative Tip‑and‑Cue (CTDE)
- Concept: Centralized‑training, decentralized‑execution MARL learns coordinated tasking across assets with comms/energy budgets. [R2][R3]
- Phase I: MAPPO/QMIX vs CBBA baseline in crosslink‑limited sims; message‑dropout training; ROE‑constrained RTA/Simplex safety cage. [R4][R5]
- Metrics: time‑to‑classification −30–40%; custody gaps −25–35%; alert latency within target under bandwidth caps; 0 safety invariant violations.


8) Onboard PNT Integrity Monitors for Safe Autonomy
- Concept: GNSS spoofing/jamming detection and navigation integrity monitoring that gates autonomy; leverages SDR/FPGA pipelines and ML detectors. [C1][C2]
- Phase I: integrate spoofing/jamming detectors; define integrity metrics and fail‑safe behaviors; HIL plan with SDR; hazard log and V&V hooks. [R3][C1][C2]
- Metrics: spoofing detection TPR ≥0.95 at FPR ≤0.05; autonomy shutdown/hold latency <1 s upon integrity breach; recovery <10 s after restoration. [C2]
- Roles: IA — ML detectors/integration; COSMIAC — SDR/FPGA path and test vectors. [C1][C2]
- Why priority: Loss/corruption of PNT is a primary operational hazard; this de‑risks any autonomous maneuver logic.

9) Intent Attribution via Behavior Models and Knowledge Graph
- Concept: Fuse kinematics, RF/EM signatures, and historical patterns to attribute benign vs. hostile intent with explainable outputs for ROE. [R1][R2]
- Phase I: behavior model library; feature engineering and uncertainty handling; counterfactual explanations; operator digest schema. [R3]
- Metrics: attribution F1 ≥0.85 on simulated scenarios; calibrated uncertainty (ECE <0.05); operator trust/usability ≥4/5. [R2][R3]
- Roles: IA — models/explainability; COSMIAC — data realism and RF signature inputs. [C1][C7]
- Why priority: Rapid attribution is central to doctrine and ROE; ties autonomy to human‑on‑the‑loop acceptance.

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


5) Sensor Self‑Calibration and Health/Performance Monitoring
- Concept: Onboard calibration checks, drift detection, and health monitoring to keep sensing/AI within valid envelopes over long missions. [R5]
- Phase I: define calibration routines and drift metrics; simulate degradation scenarios; design self‑check schedules and downlink diagnostics. [R5]
- Metrics: detection of >2% sensitivity drift within 24 h; false alarm rate <5%; zero unsafe tasks triggered by degraded sensors in sim.
- Roles: IA — monitoring algorithms/integration; COSMIAC — sensor models and on‑sensor routine feasibility. [C4][C7]
- Why priority: Preserves custody/attribution quality and maintains trust in autonomous sensing.

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


5) Run‑Time Assurance (Simplex) Safety Cage for Autonomy
- Concept: Verified safety monitor with certified fallback controller that enforces invariants on AI/RL policies (keep‑out zones, propellant, thermal, pointing). [R4]
- Phase I: specify safety invariants and fallback controller; formalize monitor checks; co‑simulation with autonomy stack; fault injection to validate guarantees. [R3][R4]
- Metrics: 0 invariant violations in stress sims; safe fallback engagement within <100 ms; mission utility loss <5% vs. unconstrained policy.
- Roles: IA — RTA design, verification, and integration with policies; COSMIAC — actuator/ADCS/thermal constraints and certification path.
- Why priority: Converts autonomy into a certifiable operational capability; reduces evaluator risk and aligns with debris‑minimizing ROE.

Ref‑informed priorities: constraint‑respecting maneuver logic (R4), resilience and rapid decision cycles (R1,R2), and heterogenous compute/secure update paths (R5,R6).

---

## Cross‑Cutting Enablers (apply across Focus Areas)
- CONOPS & Diagrams: GEO→cislunar operating concept, architecture, and integration storyboard for the Showcase; align language to USSF doctrine. [R2]
- Modeling & Simulation: unified Basilisk scenario pack with RF/optical/LIDAR models; stress cases for comms‑denied ops and proximity threats. [R1][R3]
- Space MLOps & V&V: pipeline for dataset curation, synthetic data, active learning, performance monitoring, certifiable on‑orbit updates, secure rollback. [R3][R5][R6][C1]
- HIL/Prototype Test Plan: bench test outline at COSMIAC (power/thermal/SEU injection/SDR), with data capture for Phase II gating. [R5][C6][C4]
- Security & Compliance: zero‑trust enclaves, SBOM, secure update pathways; ITAR and STTR workshare planning. [R5]
- Metrics & Eval: latency reductions (>50%), operator workload proxy (≥25% reduction), custody continuity, zero constraint‑violation target. [R2][R6]

- Delay‑Tolerant Networking (DTN/BPv7) and opportunistic downlink QoS: onboard prioritization for action telemetry, evidence, and health; survives comms denial and exploits short ground/crosslink windows. [R2]
- ROE‑aware operator digest (human‑on‑the‑loop): concise, explainable action summaries, counterfactuals, and escalation controls aligned to Space Battle Management workflows; ties to operator workload reduction. [R2]
- Standards and interoperability hooks: CCSDS‑aligned data products and BM/C2 interface stubs to de‑risk Phase II/III transition and integration. [R2]

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


## Other
- tasking multiple sensors on a single host to optimally collect data, particularly adversarial positions and maneuvers
- tasking multiple sensors on multiple hosts to optimally collect data, particularly adversarial positions and maneuvers
- is our RL agent capable of running on rad-hard SoC?