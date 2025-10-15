# scope idea

## Cosmiac's piece:

Deploy PIGEON in flight for detection of attack signals.

Phase I -- feasibility study
rad hard hardware
interface with IA signal DB

## IA's piece:

- Space EW catalog (kind of like EWIRDB for space)
  - including catalog expansion as edge deployment in flight collects data
- signal observations for SDA publishes (maybe to UDL) as edge deployment in flight observes data
- figuring out feasibility of having access to whole DB on edge compute resources
- setting up on ground backing DB or figuring out how to use existing ones
  - there are probably siloed existing ones that are classified or proprietary, but we can try an unclass version or make our own
- simulation and mocking of space EW threats from for AI training, ops training, testing, etc.

## commercialization piece:

- RF attacks in cell phones, self driving cars, etc.
- unclass space EW DB


## stretch piece

We actually design a system for arbitrary sensor types, not just RF.
Lidar, EO, IR, etc.
But in Phase I we focus on RF to establish the end to end framework.
We still study feasibility of other sensors in Phase I though.





## Further ideas and relevant details for Sensor Payloads (AIS Subtopic 2)

### Payload concept and edge architecture
- Primary Phase I focus: passive RF payload (e.g., COSMIAC’s PIGEON) with on-sensor processing (HPC-S) for immediate detection, feature extraction (e.g., PDWs/feature vectors), uncertainty scoring, and event triage.
- Software-defined/reconfigurable path: architecture and interfaces designed to accommodate additional modalities in later phases (LIDAR, radar/SAR, EO/IR, hyperspectral) without re-architecting; emphasize modular sensor-compute packaging.
- Onboard fusion and tip-and-cue: enable payload-to-payload and payload-to-bus “tip-and-cue” with change/maneuver detection to maintain custody across LEO/GEO/XGEO/cislunar.
- Security-by-design: memory-safe language pathways and zero-trust data handling onboard; signed model updates; telemetry redaction for ITAR/CUI constraints.

### Phase I scope expansions (feasibility and M&S)
- Architecture trades for edge compute (CPU/GPU/FPGA/SoC/neuromorphic) under SWaP, radiation, and thermal constraints; identify CTEs and risk retirement steps.
- Define “Space EW Catalog” subset for edge: feasibility of carrying prioritized DB slices onboard; compression/summary products (detections, PDWs, features, UQ, maneuver flags) for downlink when comms permit (e.g., UDL).
- Payload-in-the-loop M&S: integrate the RF payload model into IA’s NGSX simulation for SDA/RPO scenarios; drive synthetic RF scenes using EWIRDB-like parametric threat models via an EMoP-like process; quantify persistent custody and time-to-classification.
- Lab HIL: auto-generate PDWs via an EMoP-like process (using EWIRDB-like parametric models) to stimulate hardware via AWG, including simulated EW attack scenarios; validate onboard pre-processing thresholds/latency; compare to lab/test data where available; gate decisions with a model-uncertainty evaluation engine (SIERO-like).
- Preliminary CONOPS & diagrams: ops overview, system architecture, integration-ready design for sensors/compute/maneuver; mission threads for contested/degraded comms.

### Roles and STTR teaming
- COSMIAC (UNM): RF front-end design and integration (PIGEON), radiation test planning/mitigation, FPGA acceleration options, smallsat/ground-station integration, environmental testing; contribute ≥30% Phase I effort.
- Interactive Aptitude (IA): EMoP-like (EWIRDB-like-to-PDW/model generation approaches), SIERO-like uncertainty quantification, and NGSX payload-in-the-loop scenarios.

### Risks and mitigations (Phase I feasibility)
- SWaP/thermal/radiation: derive budgets and margins; evaluate rad-tolerant compute options; prototype thermal throttling and graceful degradation.
- Blind spots and cislunar ranges: multi-modal design path (future phases), dynamic scheduling (RL) to sustain custody, and tip-and-cue across assets.
- Data poisoning/robustness: onboard anomaly detection, signed models, and uncertainty-gated autonomy; simulation-based red-teaming in NGSX using SIERO-like methods.
- Integration complexity: adopt modular interfaces for sensor-compute packages; prioritize memory-safe implementations and deterministic latency paths.

### Evidence, metrics, and Phase II path
- Metrics: reductions in detection→classification latency; persistent custody rates; onboard power/thermal profiles that close; uncertainty-calibrated thresholds for alerts.
- Phase I deliverables: literature/trade studies (passive RF + reconfigurable payloads), feasibility of edge DB subsets and compression, payload-in-the-loop M&S and HIL demos, risk registers with CTEs, preliminary CONOPS, and a Phase II plan for a bench/flight-like prototype.
- Dual-use: unclass space EW catalog offerings; RF anomaly detection for automotive, maritime, and aviation (fighter jets and commercial airliners), and critical infrastructure; roadmap for additional modalities (SAR, EO/IR, hyperspectral) using the same payload-compute framework.
