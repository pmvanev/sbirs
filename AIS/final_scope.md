# Integrated Phase I Scope — POLARIS Edge Autonomy on Rad‑Tolerant Compute with Multi‑Agent Coordination and Standards (IA + COSMIAC)

## Introduction and provenance
This integrated scope blends and extends the following scope ideas from AIS/scope_ideas.md to form a cohesive, evaluator‑compelling Phase I concept:
- FA1‑3: POLARIS On‑Board RL Mission Autonomy
- FA1‑4: FPGA‑Resident RL Policy Inference + Secure Weight Updates
- FA1‑7: Collaborative Distributed Tip‑and‑Cue (Multi‑Host) (+ 7a MARL/CTDE)
- FA3‑2: Rad‑Tolerant Compute + Root‑of‑Trust + Memory‑Safe Runtime
- CC‑3: Space MLOps & V&V (certifiable on‑orbit updates)
- CC‑4: HIL/Prototype Test Plan
- CC‑5: Security & Compliance (zero‑trust enclaves, SBOM, ITAR/STTR workshare)
- CC‑9: Standards/Interoperability Hooks (CCSDS/BM‑C2)

For additional context on IA’s heritage (POLARIS, CMA‑SHIELD, NGSX, multi‑agent RL), see AIS/ia.md.

## Executive summary
We propose to demonstrate feasibility and de‑risk integrated edge autonomy for contested space by:
1) Running a POLARIS‑trained RL agent on realistic, radiation‑tolerant SoC/FPGA hardware with secure boot and a memory‑safe runtime (FA3‑2 + FA1‑4), validated in Hardware‑in‑the‑Loop (HIL) (CC‑4).
2) Extending POLARIS to multi‑agent coordination across hosts and orbital regimes (GEO/XGEO/cislunar), including inter‑host comms, comms jamming, and ground‑link denial; evaluating cooperative mission execution via collaborative tip‑and‑cue using MARL with run‑time safety (FA1‑7 + 7a + FA1‑3).
3) Defining standards and compliance artifacts for security, AI shielding/run‑time assurance, and certifiable model/weight updating with CCSDS/BM‑C2‑aligned data products and interfaces (CC‑3 + CC‑5 + CC‑9).

Outputs include: feasibility study, preliminary CONOPS, unified M&S evidence with quantitative metrics, a HIL bench test plan and initial bench results, and a standards‑forward security/update package to smooth Phase II transition.

## Why this meets real operational needs (USSF)
- Comms‑denied autonomy: Onboard decision‑making continues mission when adversaries jam crosslinks or ground links (R1, R2).
- Rapid decision advantage: >50% reduction in decision latency vs. ground loop; −25% operator workload (R2, R6).
- Persistent custody and attribution: Multi‑host tip‑and‑cue maintains tracks and speeds intent classification (R2, R3).
- Safety/certifiability: Run‑Time Assurance (RTA)/Simplex safety cage, memory‑safe runtimes, and zero‑trust enclaves mitigate autonomy risk (R3, R5).
- Secure, resilient compute: Radiation‑tolerant SoC/FPGA with secure boot, SBOM, and signed, rollback‑safe updates (R5, R6).
- Transition ready: CCSDS/BM‑C2‑aligned data and interfaces; DTN/BPv7‑aware downlink prioritization where appropriate (CC‑9; complements cross‑cutting enablers).

## Technical approach
### Thread A — Edge RL on rad‑tolerant compute with secure updates (FA3‑2, FA1‑4, CC‑4)
- Hardware concept: Rad‑tolerant SoC/FPGA (e.g., RISC‑V/ARM‑class with FPGA fabric), ECC/TMR mitigations, secure boot root‑of‑trust.
- Software/runtime: Memory‑safe runtime (e.g., Rust/WASM class), enclave execution path for policies and feature extractors.
- RL policy: POLARIS‑trained compact actor (quantized/pruned) mapped to SoC/FPGA for low‑latency, low‑power inference.
- Update protocol: Signed containerized weight/bias updates with versioning and rollback; integrity/tamper checks; SEU fault injection plan.
- HIL: Bench setup with power/thermal/SEU injection instrumentation; latency/throughput measurement and stability under induced faults.

### Thread B — Multi‑agent POLARIS for collaborative tip‑and‑cue (FA1‑3, FA1‑7, 7a)
- Environment: GEO/XGEO/cislunar scenarios with friendly assets (3–6) and adversary behaviors; partial observability; crosslink budgets.
- Algorithms: Start with CTDE MARL (MAPPO/QMIX vs. CBBA/auction baseline); parameter sharing for homogeneous assets; message‑dropout training.
- Communications: Inter‑host messaging policies (what/when to communicate) within bandwidth/energy caps; ground‑link‑denied and jammed crosslink cases.
- Safety: RTA/Simplex safety cage plus rule‑based guardrails for keep‑out zones, delta‑V limits, and thermal/pointing constraints.
- Evidence: Time‑to‑classification, custody gaps, alert latency, and operator intervention rate vs. heuristics; ablation under jamming.

### Thread C — Standards, security, and Space MLOps (CC‑3, CC‑5, CC‑9)
- Standards & interfaces: CCSDS‑aligned data products, BM‑C2 interface stubs; schema for action traces, evidence snippets, and health telemetry.
- Security & compliance: Zero‑trust enclaves; SBOM; key management and trust anchors; ITAR/STTR workshare planning documentation.
- Space MLOps & V&V: Synthetic data, active learning hooks, on‑orbit update pathway with certification considerations; verification artifacts and logs.
- Optional: DTN/BPv7 and opportunistic downlink QoS for prioritized alerts/evidence in intermittent link environments (aligns with cross‑cutting enablers).

## Phase I activities and deliverables
- Literature review and trade studies across edge compute, MARL coordination, safety/RTA, and standards (R1‑R6; C1‑C7).
- POLARIS environment extensions (GEO→cislunar) and domain randomization for comms‑denied operations.
- Compact/quantized policy export and SoC/FPGA mapping prototype with performance characterization.
- HIL bench test plan and initial feasibility runs (power/thermal/SEU; signed‑update demo‑in‑the‑loop).
- MARL vs. CBBA/heuristic comparison under crosslink/ground jamming; message policy learning; safety cage integration.
- Preliminary CONOPS and architectural diagrams (Edge compute + Multi‑host coordination + Security/MLOps + Interfaces).
- Draft standards and compliance package (CCSDS/BM‑C2 schemas, SBOM, update policy, operator digest format).
- Risk register and mitigation plan; Phase II development roadmap.
- AIS Phase I Showcase artifacts: 5‑page technical volume outline, 10‑slide deck figures/plots, and traceable metrics.

## Quantitative success metrics (Phase I targets)
- Decision latency: >50% reduction vs. ground‑loop baseline in sim; <10 ms on‑device inference for core policy (SoC/FPGA prototype).
- Operator workload proxy: ≥25% reduction via autonomous action broker and operator digest.
- Custody/attribution: −25–35% custody gaps; −30–40% time‑to‑classification vs. heuristic baseline under bandwidth caps.
- Safety/certifiability: 0 invariant violations in stress sims; RTA fallback <100 ms; secure signed update + rollback demonstrated in HIL.
- Resilience: Autonomous hold/safe mode engagement <1 s on PNT/health integrity breach; recovery <10 s on restoration.


## Proposed Phase I final outcome
At the end of Phase I, we deliver a cohesive feasibility package proving the viability of autonomous, cooperative tasking across heterogeneous sensors and multiple orbital environments, optimized for both steady‑state operations and adversarial conditions (e.g., denied crosslinks/ground links, jamming, data poisoning):
- Feasibility study and trade studies: quantified viability of running POLARIS‑trained RL on rad‑tolerant SoC/FPGA; MARL coordination under bandwidth/energy caps; resilience of security/update mechanisms; standards alignment (CCSDS/BM‑C2).
- Preliminary CONOPS: end‑to‑end operating concept for multi‑host, heterogeneous sensing (e.g., passive RF, optical/IR/HSI/LIDAR as simulated) across GEO/XGEO/cislunar with ROE‑aware autonomy modes for normal and contested conditions.
- Architecture and interface specification: schemas for action traces, evidence/ROI snippets, health/decision telemetry; BM‑C2 interface stubs; optional DTN/BPv7 QoS profiles for prioritized alerts/evidence.
- HIL bench evidence: latency/power/thermal profiles, SEU tolerance posture, signed update + rollback demo‑in‑the‑loop, and RTA/Simplex safety response traces.
- Evaluation dossier: traceable metrics showing >50% decision‑latency reduction, ≥25% operator‑workload reduction proxy, custody‑gap and time‑to‑classification improvements under bandwidth caps and jamming; 0 safety‑invariant violations in stress scenarios.
- Transition readiness kit: SBOM, secure update runbooks, verification artifacts, test plans, and a Phase II development roadmap aligned to standards and integration pathways.

In effect, Phase I culminates in a smart, standards‑aligned constellation concept: a resilient network of cooperating sensors that “see and report” the maximum mission‑relevant SDA information possible while remaining robust to adversarial attacks and communications denial.

## Roles, workshare, and facilities
- Interactive Aptitude (IA)
  - POLARIS/MARL algorithm design and training; safety shields and RTA integration; sim/M&S; metrics and ablation studies.
  - Model compression/quantization and SoC/FPGA mapping support; update tooling; operator digest and explainability artifacts.
  - Standards/interface schemas; Space MLOps/V&V pipeline and certification documentation; CONOPS and Showcase assets.
- COSMIAC
  - Rad‑tolerant compute concept (SoC/FPGA selection, ECC/TMR), secure boot/root‑of‑trust, key management, SBOM pipeline.
  - HIL bench setup and execution (power/thermal/SEU injection/SDR crosslink emulation); signed update demo‑in‑the‑loop.
  - Crosslink/SDR feasibility and power/thermal envelopes; support CCSDS/BM‑C2 interface stubs and DTN/BPv7 evaluation as needed.

## Commercial potential
- Constellation autonomy platform: fleet‑level tasking and health management for commercial operators (GEO/LEO mega‑constellations).
- Space‑rated edge autonomy stack: rad‑tolerant compute with secure update, RTA safety cage, and Space MLOps lifecycle.
- MARL fleet coordination: multi‑vehicle (UAV/maritime/ground) coordination under comms limits and adversarial conditions.
- Secure edge AI: safety‑critical embedded platforms (industrial/energy/transport) with certifiable model updates and SBOM.
- Simulation & training products: cislunar‑grade visualization, scenario packs, and autonomy evaluation toolchains.
- Weather/meteorology constellations: smart onboard agents optimize collection planning (cloud‑aware), ROI compression to minimize downlink, and solar‑charging‑aware duty cycling to extend lifetime (e.g., [ESA Φ‑sat‑1 onboard AI cloud filtering](https://www.eoportal.org/satellite-missions/phisat-1)).
- Environmental disaster monitoring (wildfire, floods, hurricanes, oil spills): event‑driven tip‑and‑cue across sensors; prioritize urgent ROIs and opportunistic downlink for faster response timelines ([NASA Disasters | Floods](https://appliedsciences.nasa.gov/what-we-do/disasters/floods), [NASA FIRMS](https://www.earthdata.nasa.gov/data/tools/firms)).
- PNT/GNSS augmentation constellations: on‑orbit integrity monitoring and anti‑spoofing; coordinated health reporting and safe autonomy to preserve service availability ([FAA WAAS integrity](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gnss/waas/howitworks), [Galileo OSNMA authentication](https://www.gsc-europa.eu/galileo/services/galileo-open-service-navigation-message-authentication-osnma)).
- Broadband/mesh networking constellations (e.g., Starlink, OneWeb): multi‑agent coordination for beam steering, inter‑sat handoffs, and power/thermal balancing to maximize capacity and availability under outages ([LEO ISL routing/load balancing survey](https://arxiv.org/abs/2406.05078)).
- SAR constellations: multi‑sat revisit optimization and on‑sensor change detection; cross‑cue optical/IR assets to confirm events with minimal bandwidth ([ICEYE rapid‑revisit fleet](https://iceye-ltd.github.io/product-documentation/5.0/productguide/fleet/), [Onboard SAR processing](https://ieeexplore.ieee.org/document/10547107)).
- Maritime/aviation tracking (AIS/ADS‑B relay) constellations: cooperative tasking to maintain custody of high‑value targets and reduce latency to shore networks ([Aireon space‑based ADS‑B](https://aireon.com/wp-content/uploads/2024/09/Aireon-White-Paper_En-route-Turbulence-Detection_Sept2024.pdf), [Spire satellite AIS](https://www.eoportal.org/satellite-missions/spire-global)).
- On‑orbit servicing/tugs and debris removal: safe RPOD planning with RTA/Simplex, crosslink‑aware coordination, and certifiable update pathways ([Northrop Grumman MEV‑1/2](https://www.eoportal.org/satellite-missions/mev-1), [JAXA ADRAS‑J](https://www.kenkai.jaxa.jp/eng/crd2/)).
- Agriculture/land‑use analytics: targeted HSI collections with weather‑aware planning and ROI prioritization to cut costs per insight ([Pixxel HSI constellation](https://www.eoportal.org/satellite-missions/pixxel), [NASA SBG mission](https://www.sciencedirect.com/science/article/pii/S0034425721000675)).
- Space weather/heliophysics monitoring: energy‑aware scheduling and prioritized alerting via DTN for geomagnetic storm events ([NOAA SWFO‑L1](https://www.noaa.gov/news-release/noaas-swfo-l1-observatory-heads-to-orbit-for-groundbreaking-mission)).
- IoT/LPWAN constellations: gateway scheduling and coverage optimization under power/link constraints; DTN‑backed firmware/model update logistics ([Kineis satellite IoT](https://space.skyrocket.de/doc_sdat/kineis-1.htm), [DTN BPv7 RFC 9171](https://datatracker.ietf.org/doc/rfc9171/)).


## Risks and mitigations
- Hardware SWaP limits for inference: mitigate via quantization/pruning, FPGA offload, and heterogeneous compute design (R5, R6).
- Certification of autonomy: RTA/Simplex architecture, memory‑safe runtime, and traceable logs/digests; align to standards early (CC‑9, CC‑5).
- Data scarcity/domain shift: synthetic data, active learning, performance monitoring; robust sim‑to‑edge validation (R3, R5).
- Comms fragility: message‑dropout training; opportunistic downlink prioritization; deterministic CBBA fallback.

## Phase II trajectory (preview)
- Mature HIL prototype into an integrated flight‑like payload/processor; thermal‑vac and radiation testing; limited over‑the‑air exercises.
- Expand to multi‑sat coordination with cross‑vendor bus interfaces; integrate standards package into partner ecosystems.
- Demonstrate end‑to‑end tip‑and‑cue with secure updates and operator digests aligned to BM‑C2 workflows.

## References (from AIS/ref_summaries.md)
- R1: The Economist — satellite‑on‑satellite threats; comms‑denied ops; debris minimization
- R2: USSF Space Warfighting Framework — doctrine; decision advantage; SDA/SC/SBM
- R3: RAND — AI/ML for SDA; data, domain shift, V&V, trust; synthetic data
- R4: IEEE AERO 2023 — MPC for RPOD; constraint‑aware onboard maneuvering
- R5: NASA Current Technology in Space v4 — hardware tradeoffs; Space MLOps; certifiable updates
- R6: Lockheed AIAA — onboard AI/ML mission processing patterns and performance
- C1: COSMIAC PNT projects; ML‑based GNSS threat detection/mitigation
- C2: UNM Thesis on GPS spoofing detection with FPGA deployment
- C3: ION JNC materials on spoofing detection and ML for PNT
- C4: SPARC‑1: Agile Space Radio + SSA camera; reconfigurable RF payload heritage
- C5: Trailblazer/SPA: Modular avionics and rapid integration for CubeSats
- C6: RHEME: Radiation Hardened Electronic Memory Experiment (ISS/STP flights)
- C7: UNM Antennas & RF Lab: reconfigurable antennas; cognitive radio; phased arrays

