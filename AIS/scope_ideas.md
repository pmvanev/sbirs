# AIS Phase I — Brainstormed Scope Ideas (IA + COSMIAC)

This list groups big‑picture Phase I ideas by AIS Focus Area, leveraging Interactive Aptitude (IA) strengths in AI/ML, simulation, RL, and software, and COSMIAC strengths in radiation‑tolerant embedded systems, RF/sensors, smallsat development, and test facilities. Each idea includes: concept, Phase I activities/deliverables, success signals/metrics, and IA/COSMIAC roles.

---

## Focus Area 1 — Edge Computing & Algorithms

1) POLARIS‑trained On‑Board RL Mission Autonomy (Power/Sensing/Downlink)
- Concept: Extend IA’s POLARIS RL training (Basilisk + Gymnasium) to GEO/XGEO/cislunar regimes and deploy an onboard policy that jointly optimizes solar charging, sensor tasking, tip‑and‑cue, and comms downlink while respecting safety/ITAR constraints.
- Phase I activities/deliverables:
  - Basilisk environment extensions (GEO→cislunar), synthetic scenarios, and domain randomization for comms‑denied ops.
  - Train/evaluate RL policies vs. baselines; generate traceable performance logs for latency/workload targets.
  - Safety shield + rule‑based guardrails and formal checks for “never exceed” constraints.
  - HIL feasibility plan with COSMIAC prototype compute board; edge resource budget and thermal map.
- Success signals/metrics: >50% reduction in decision latency vs. ground‑loop baseline; measurable improvement in energy margin and downlink throughput; safe‑action rate >99.9%; policy stability across disturbance cases.
- Roles: IA — RL/POLARIS models, safety shields, M&S; COSMIAC — prototype compute board selection (rad‑tolerant SoC/FPGA), HIL plan, thermal/power envelope.

2) Onboard Threat and Maneuver Classification with Safe RL “Action Broker”
- Concept: Fuse kinematic features + RF/sensor cues into an onboard classifier; couple to a safe RL “action broker” that selects evasive/observe/hold actions with constraints and explainability.
- Phase I: data model + synthetic generation; lightweight model selection (mobile‑friendly CNN/RNN/transformer); action broker with explicit constraint layer; verification harness and test cases.
- Metrics: classification F1>0.9 on synthetic adversary maneuvers; constraint violation rate ~0; operator workload proxy −25%.
- Roles: IA — models, broker, verification; COSMIAC — compute footprint study, secure boot/root‑of‑trust feasibility.

3) Data Poisoning and OOD Resilience on the Edge
- Concept: Onboard triage with OOD detectors, adversarial perturbation hardening, and sensor cross‑checks; memory‑safe language prototypes and zero‑trust enclaves for model execution.
- Phase I: evaluate OOD/adversarial defenses (e.g., energy‑based/OE) under SWaP limits; prototype enclave execution path; secure update concept for models.
- Metrics: maintained detection at AUC>0.9 under poisoning; enclave overhead <20% compute; recovery time <10 s.
- Roles: IA — defenses, enclave pipeline; COSMIAC — trust anchors, key mgmt, firmware chain‑of‑custody.

4) Neuromorphic/FPGA Edge Inference Feasibility for Anomaly Detection
- Concept: Investigate spiking NN or FPGA‑accelerated anomaly detectors for ultra‑low‑power custody maintenance.
- Phase I: port a lightweight anomaly kernel to FPGA/spiking sim; compare watts/inference vs. CPU/GPU; radiation effect literature review and risk posture.
- Metrics: 3–10× energy per inference improvement; accuracy within 5% of CPU ref; radiation risk/mitigation plan.
- Roles: IA — models/algorithms; COSMIAC — FPGA/neuromorphic feasibility, radiation test campaign plan.

5) Cislunar Visualization + RL Training Toolchain
- Concept: Produce cislunar‑grade visualizations and simulators tied to POLARIS for planning, replay, and showcase.
- Phase I: visualization tool, scenario pack, and CONOPS storyboard; hooks for “what‑if” latency/workload analysis.
- Metrics: end‑to‑end sim‑to‑policy loop demonstrated; stakeholder usability feedback ≥4/5.
- Roles: IA — tools; COSMIAC — scenario realism review, ops constraints.

---

## Focus Area 2 — Sensor Payloads

1) Passive RF SDA Micro‑Payload with On‑Sensor Pre‑Processing (HPC‑S)
- Concept: COSMIAC designs a reconfigurable passive RF front‑end (SDR/FPGA) with on‑sensor feature extraction; IA supplies onboard ML for maneuver/intent cues and compression for comms‑denied ops.
- Phase I: RF link budgets; feature pipelines (Doppler, TDOA/FDOA, emitter characterization); model sizing for on‑sensor inference; data reduction/compression.
- Metrics: custody persistence +X% in sims; compression ≥10× with <5% utility loss; inference latency <100 ms.
- Roles: COSMIAC — RF front‑end concept, FPGA mapping; IA — ML models, compression, fusion.

2) Software‑Defined, Reconfigurable Multi‑Modal Sensing Concept
- Concept: Define a payload that can retask between passive RF and IR/hyperspectral (simulation‑only in Phase I) with IA triage deciding when/where to collect.
- Phase I: sensor trade studies; reconfig profiles; tasking policies; on‑sensor compute budget.
- Metrics: improved “tip & cue” efficiency (≥30% fewer wasted collects); maneuver change detection ΔF1>0.1.
- Roles: IA — triage/tasking; COSMIAC — reconfigurable sensor architecture/constraints.

3) Hyperspectral Change Detection and On‑Sensor Compression
- Concept: Pipeline for rapid change cues (e.g., plume, panel reorientation) with in‑band compression and ROI prioritization.
- Phase I: synthetic HSI generation; change‑detection kernels on edge; ROI prioritization policies for downlink.
- Metrics: change detection latency <10 s; compressed ROI PSNR/SSIM within 5% loss threshold; downlink savings ≥10×.
- Roles: IA — algorithms/policies; COSMIAC — edge hardware mapping and memory bandwidth plan.

4) LIDAR/Active Sensing Custody Simulation with Fusion Hooks
- Concept: Simulate LIDAR for close‑in custody and fuse with RF/optical for improved track continuity through maneuvers.
- Phase I: sensor models, fusion study, and degraded‑sensing scenarios; produce design envelope for power/thermal.
- Metrics: custody break rate −25% in maneuvering scenarios; fusion latency <200 ms.
- Roles: IA — fusion/M&S; COSMIAC — power/thermal envelope, mounting/field‑of‑regard constraints.

---

## Focus Area 3 — Bus Design

1) Modular Autonomy Manager for Power/Thermal/Compute Load‑Shedding
- Concept: A software “vehicle manager” that orchestrates compute throttling, sensor duty cycling, and thermal protection based on mission phase and threat posture.
- Phase I: architecture, state machine + policy hooks (from Edge ideas), thermal/power budget models; hardware abstraction layer.
- Metrics: thermal violations reduced ≥80% in stress tests; mission utility loss <5%; autonomy safety incidents = 0 in sim.
- Roles: IA — autonomy stack; COSMIAC — bus interfaces, thermal/power models, component selection.

2) Safe Collision Avoidance and Evasive Maneuver Executive
- Concept: Lightweight guidance executive integrating real‑time conjunction alerts with safe maneuver templates, verified against prop/attitude limits.
- Phase I: maneuver library; verification harness; delta‑V budget trade space.
- Metrics: 0 constraint violations; maneuver decision latency <5 s; custody maintained ≥80% during avoidance.
- Roles: IA — algorithms/verification; COSMIAC — propulsion/ADCS constraints and actuator models.

3) Rad‑Tolerant Compute Stack with Root‑of‑Trust and Memory‑Safe Runtime
- Concept: COSMIAC prototypes a rad‑tolerant compute architecture (RISC‑V/FPGA SoC + TMR/ECC) with secure boot and IA’s memory‑safe runtime for autonomy apps.
- Phase I: block diagram, parts/availability survey, SEU/SET mitigation approach, secure boot chain design; sample WASM/Rust micro‑services.
- Metrics: boot‑to‑mission <10 s; SEU tolerance plan; enclave perf overhead <20%.
- Roles: COSMIAC — hardware concept; IA — runtime + app containerization.

4) High Delta‑V Mission Profile Study for Rapid Evasion/Retasking
- Concept: Co‑design autonomy policies with high‑delta‑V capability envelopes; quantify gains in threat response.
- Phase I: mission analysis; policy coupling; delta‑V vs. custody/latency curves.
- Metrics: threat intercept‑avoidance probability +X%; time‑to‑safe‑state <5 min in worst‑case sims.
- Roles: IA — policy coupling/M&S; COSMIAC — propulsion options/thermal impacts.

---

## Cross‑Cutting Enablers (apply across Focus Areas)
- CONOPS & Diagrams: GEO→cislunar operating concept, system architecture, and integration storyboard for showcase.
- Modeling & Simulation: unified Basilisk scenario pack with RF/optical/LIDAR models; stress cases for comms‑denied ops.
- HIL/Prototype Test Plan: bench test outline at COSMIAC labs (power/thermal/SEU injection/sdr), with data capture for Phase II gating.
- Security & Compliance: zero‑trust enclaves, SBOM, secure update pathways; ITAR and STTR workshare planning.
- Metrics & Eval: latency reductions (>50%), operator workload proxy (≥25% reduction), custody continuity, constraint‑violation zero target.

---

## Example Integrated Phase I Threads (IA + COSMIAC)
- Thread A (Edge+Bus): POLARIS policy + autonomy manager + safe action broker, with HIL feasibility on a rad‑tolerant SoC/FPGA board concept.
- Thread B (Sensors+Edge): Passive RF micro‑payload concept with on‑sensor features and triage; compression + tip‑and‑cue to reduce downlink.
- Thread C (All‑Up Sim): Cislunar scenario pack with visualization and CONOPS, reporting latency/workload/custody metrics for showcase.

---

## Phase II Trajectory Pointers
- Mature the HIL prototype into an integrated flight‑like payload/processor; thermal‑vac and radiation testing; limited over‑the‑air ground station exercises via COSMIAC.
- Progress TRL for onboard autonomy, secure runtime, and on‑sensor HPC‑S; expand to multi‑sat coordination and cross‑vendor bus interfaces.

