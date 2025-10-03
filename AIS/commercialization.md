# AIS Commercialization Concepts (derived from scope_ideas.md)

This document translates Phase I scope concepts into commercialization-ready product offerings geared for near-term traction and Phase II/III transition.

---

### 1) Safe Autonomy “Action Broker” + Threat Classifier SDK
- What: Onboard maneuver/threat classifier with a constraint-aware action broker that enforces ROE and debris-minimizing policies.
- Buyers: Space primes, smallsat bus vendors, SatOps platforms, USSF programs.
- Why it wins: Cuts operator workload and decision latency; aligns to comms-denied ops and doctrine.
- MVP: Containerized SDK, verification harness, explainability/counterfactual logging; on-orbit log schema.
- Pricing: Per-satellite runtime license + support/assurance.
- Derived from: FA1-1

### 2) Edge OOD/Poisoning Resilience Module
- What: Lightweight OOD detection, adversarial hardening, zero-trust enclave execution and rollback path for on-orbit models.
- Buyers: Primes, space cybersecurity vendors, payload OEMs.
- Why it wins: Trustworthy autonomy and secure updates are procurement priorities.
- MVP: OOD + enclave path with <20% runtime overhead; signed update + rollback demo.
- Pricing: Per-device license + annual maintenance.
- Derived from: FA1-2

### 3) POLARIS Autonomy Studio (Sim-to-Policy Platform)
- What: Basilisk-backed simulation, RL training, safety shields, and cislunar visualization/replay for mission planning and V&V.
- Buyers: USSF labs, primes, SatOps tool vendors, academia.
- Why it wins: Accelerates experimentation with measurable latency/workload gains; strong Phase I → II path.
- MVP: Scenario pack, policy baselines, metrics dashboards, replay tooling.
- Pricing: Annual seats + integration services.
- Derived from: FA1-3, FA1-5

### 4) FPGA RL Inference IP + Secure Weight Update Protocol
- What: Low-latency, low-power RL inference IP for FPGA/SoC with signed weight update and rollback; SEU-aware mitigations.
- Buyers: FPGA vendors, bus integrators, payload OEMs.
- Why it wins: SWaP savings + certifiable update story tailored to space compute.
- MVP: Quantized actor core, HLS/HDL reference, signing/rollback toolchain, HIL demo.
- Pricing: IP license + per-program royalty + support.
- Derived from: FA1-4

### 5) On-Sensor ML for Passive RF Micro-Payload (HPC-S)
- What: Reference design + software pipelines (Doppler/TDOA/FDOA features, compression, fusion) for custody maintenance.
- Buyers: Small payload houses, defense primes, SSA startups.
- Why it wins: Demonstrable downlink reduction and custody improvement.
- MVP: RF budgets, feature extraction, ≥10× compression with <5% utility loss.
- Pricing: NRE + per-unit SDK/license bundle.
- Derived from: FA2-1

### 6) Multi-Modal Sensor Tasking Orchestrator
- What: Software that retasks between RF/IR/HSI in real time with tip-and-cue policies to minimize wasted collects.
- Buyers: Reconfigurable payload vendors, mission integrators.
- Why it wins: Software-defined payloads with clear ≥30% efficiency gains.
- MVP: Policy engine, simulation integration, clean APIs.
- Pricing: Module license + integration services.
- Derived from: FA2-2

### 7) Hyperspectral Edge Change Detection SDK
- What: On-sensor change detection and ROI-aware compression tuned for downlink-limited operations.
- Buyers: HSI payload vendors, EO providers, defense ISR teams.
- Why it wins: Faster detection + cheaper downlink; dual-use across EO/industrial inspection.
- MVP: Edge kernels, ROI prioritization, quality controls and benchmarks.
- Pricing: Per-payload SDK license + support.
- Derived from: FA2-3

### 8) Modular Autonomy Manager (Power/Thermal/Compute)
- What: Vehicle manager orchestrating compute throttling, sensor duty cycling, and thermal protection tied to autonomy policies.
- Buyers: Bus OEMs, primes, constellation operators.
- Why it wins: Reduces thermal violations and preserves mission utility; integrates with edge AI.
- MVP: State machine + HAL + power/thermal/compute budget models; safety hooks.
- Pricing: Platform license + support SLAs.
- Derived from: FA3-3

### 9) Rad-Tolerant Secure Compute Stack + Rust/WASM Runtime
- What: Dev kit combining rad-tolerant SoC/FPGA concept, secure boot, enclave execution, and memory-safe runtime.
- Buyers: Primes, advanced smallsat OEMs, research labs.
- Why it wins: Turnkey path to trustworthy autonomy and secure updates.
- MVP: Hardware concept, boot chain, sample microservices, Space MLOps hooks.
- Pricing: Hardware dev kit + runtime license.
- Derived from: FA3-2

### 10) Secure Space MLOps Update Service (Ground-to-Orbit)
- What: Managed signing, SBOM, policy gating, telemetry capture, and rollback for on-orbit model/weight updates.
- Buyers: Operators, primes, SatOps platforms.
- Why it wins: Solves governance/compliance and reduces risk for AI at the edge.
- MVP: Signing pipeline, policy gate, audit logs, on-orbit packaging schema.
- Pricing: Annual subscription + per-update fee.
- Derived from: FA1-2, FA1-4, Cross-Cutting

### 11) Cislunar Visualization & Mission Replay Workbench
- What: Operator-ready timelines, ROE overlays, counterfactuals, and exportable artifacts for acquisition reviews.
- Buyers: Program offices, primes, wargaming/training units.
- Why it wins: Immediate value for CONOPS/storytelling and V&V traceability.
- MVP: Replay tool, scenario pack, explainability panels, export tools.
- Pricing: Seat license + scenario/content add-ons.
- Derived from: FA1-5

### 12) HIL Testbed for Edge Autonomy & Secure Updates
- What: Bench kit for power/thermal/SEU injection with data capture and secure update-in-the-loop validation.
- Buyers: Primes, payload vendors, labs.
- Why it wins: De-risks Phase II/III transitions and accelerates vendor adoption.
- MVP: Fixtures, scripts, standard test reports, reference datasets.
- Pricing: Equipment + services bundles.
- Derived from: Cross-Cutting

---

## Quick Prioritization (fastest path to traction)
- Software-first (lowest friction): 1, 2, 3, 7, 8, 11
- Dual hardware+software with strong demand: 4, 5, 6, 9, 12
- Platform/service recurring revenue: 3, 10, 11

## Immediate Next Steps
- Select top 3 for MVP build and pilot customers.
- Prepare a one-page for each (problem, proof, plan, price) and a 90-day build plan.
- Map Phase I deliverables directly to MVP milestones and demo criteria.
