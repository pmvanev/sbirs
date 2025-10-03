# Primary Concerns of the AIS Solicitation Writer

## Mission and Operational Drivers
- Operate autonomously in contested/degraded space: co-orbital threats, jamming/dazzling, proximity/grappling, and degraded ground links; minimize debris and follow safe ROE while maintaining mission continuity. [Economist 2025; USSF Framework 2025]
- Collapse decision timelines from hours to minutes (target <5 minutes end-to-end) with onboard detection, classification, and response to preserve space superiority. [Economist 2025; USSF Framework 2025]
- Provide persistent, predictive, and precise Space Domain Awareness (SDA) across LEO/GEO/XGEO/cislunar, enabling rapid attribution and coordinated Space Control/Battle Management. [USSF Framework 2025]

## Technical Focus Areas and What Concerns Drive Them
### 1) Edge Computing & Algorithms
- Onboard threat analytics and maneuver/collision detection that run within strict SWaP, latency, and safety envelopes; achieve ≥50% kill-chain latency reduction and ≥25% operator workload reduction. [Solicitation]
- Resilient, secure, radiation-tolerant compute with power/thermal-aware AI pipelines; safe autonomy with deterministic bounds. [NASA 2024; Lockheed AIAA 2022]
- Robustness to data poisoning/OOD and domain shift; assurance, V&V, and monitoring suitable for safety-critical decisions. [RAND RRA2318-1]

### 2) Sensor Payloads
- Multi-modal sensing (passive RF, LIDAR, radar, IR, hyperspectral) with on-sensor processing (HPC-S) for immediate cueing/fusion and persistent custody through maneuvers and across regimes. [NASA 2024]
- Software-defined/reconfigurable payloads that sustain performance in blind spots and harsh conditions (solar exclusion, cislunar ranges). [Solicitation]

### 3) Bus Design
- Modular, integration-ready platform that can host evolving sensors/compute without re-architecture; all-of-vehicle autonomous optimization and load shedding under duress. [Solicitation]
- High delta-V and autonomous collision avoidance with provably safe trajectory planning suitable for onboard execution. [IEEE MPC 2023]

## Architecture and Integration Expectations
- Heterogeneous edge compute selection (CPU/GPU/FPGA/SoC/neuromorphic) with clear partitioning, scheduling, and update/certification pathways for on-orbit models. [NASA 2024; Lockheed AIAA 2022]
- Secure-by-design autonomy stack (memory-safe languages, zero-trust onboard computation, encryption/keying) aligned with mission risk posture. [Solicitation]
- End-to-end MLOps adapted to space: data curation/synthetic data, simulation, active learning, performance monitoring, and rollback strategies. [RAND RRA2318-1; NASA 2024]

## Verification, Validation, and Trust
- Evidence that autonomous behaviors are safe, bounded, and testable under adversarial conditions; simulation-backed performance envelopes and fail-safe modes. [RAND RRA2318-1]
- Debris-minimizing ROE and accountability/attribution considerations for autonomous actions. [Economist 2025]

## Programmatic and Process Constraints
- STTR compliance: partner with a research institution; meet workshare percentages; ITAR restrictions and disclosures. [Solicitation]
- Phase I deliverables emphasize research and communication quality: literature review, feasibility study with CTEs, CONOPS with ops/system diagrams, trade studies, risk/mitigation, and an excellent AIS Phase I Showcase (which functions as Phase II selection). [Solicitation]
- Practical constraints: page limits, six–eight month timeline, budget for showcase travel, clear Phase II transition path. [Solicitation]

## Quantitative Targets and Success Indicators
- ≥50% reduction in kill-chain latency; ≥25% reduction in operator workload demonstrated via modeling/simulation and traceable to CONOPS. [Solicitation]
- Real-time detection/classification timelines (e.g., alerting in <10 seconds for certain events; end-to-end response in <5 minutes) with power/thermal budgets that close. [Solicitation]
- Risk retirement for key CTEs with data-backed feasibility, including radiation tolerance, thermal management, and real-time throughput at TRL-appropriate fidelity. [Solicitation; NASA 2024]

## Risks the Solicitation Expects Proposers to Mitigate
- Data scarcity/labeling, domain shift, and trust/assurance for space AI/ML; adversarial robustness and monitoring. [RAND RRA2318-1]
- SWaP, power, and thermal limits for on-orbit compute; radiation-induced faults and fault tolerance. [NASA 2024; Lockheed AIAA 2022]
- Integration complexity across sensors/compute/maneuver; maintaining custody and performance across regimes including cislunar. [USSF Framework 2025; NASA 2024]

## Implications for a Strong Phase I Response
- Anchor architecture and CONOPS in USSF doctrine and contested-space realities; quantify latency/workload wins and trace them to on-orbit autonomy.
- Present a credible heterogeneous compute plan with certification/update pathways; show how power/thermal/rad budgets close.
- Provide a V&V plan for safety-critical autonomy with simulation evidence and risk retirement steps toward Phase II.
- Demonstrate a compliant STTR teaming plan and a compelling, concise showcase narrative.

---

### Evidence Base (non‑COSMIAC)
1) The Economist (2025): Satellite-on-satellite combat preparedness; rapid attribution; on‑orbit ROE; automation for decision speed.
2) USSF “Space Warfighting – A Framework for Planners” (2025): Doctrine for SDA/DSC/SBM; resilience; rapid, integrated kill chains.
3) RAND RRA2318-1: AI/ML for SDA; challenges (data, domain shift, V&V/trust); MLOps tailored to space.
4) IEEE Aerospace (2023): MPC for autonomous RPOD and collision avoidance with onboard-feasible controllers.
5) NASA “Current Technology in Space v4” (2024): Reference architecture; Space MLOps; rad‑tolerant compute; power/thermal; heterogeneous platforms; certifiable updates.
6) Lockheed AIAA (2022): Onboard AI/ML mission processing; SWaP-aware scheduling; heterogeneous compute; update strategies; latency outcomes.

