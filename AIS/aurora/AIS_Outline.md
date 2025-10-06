## AIS Proposal — Outline and Mapping Summary (Autonomous Updatable Resilient On-orbit Reasoning Architecture — AURORA)

### Executive Summary (What this proposal does)
- Proposes a resilient, certifiable edge‑autonomy and coordination architecture for contested space operations.
- Core subsystems: Edge Autonomy Stack; Safety/RTA + Operator Digest; Multi‑Host Tip‑and‑Cue (MARL); Space MLOps & V&V; Standards & Interfaces.
- Phase I validates feasibility via simulation/HIL, initial CONOPS/architecture, and a focused metrics plan; prepared with COSMIAC.

---

### Section-by-Section Outline
1) Front Matter
- Volume and Title: "Volume 2: Technical Volume"; Title: "AURORA: Resilient Edge Autonomy and Multi‑Agent Coordination for SDA".
- Definitions/Glossary: see AIS/aurora/Definitions.md

2) 1.0 Description of Proposed Phase I Technical Effort
- Problem: Ground‑loop latency, comms denial, and cognitive overload constrain SDA responsiveness; onboard autonomy and multi‑asset coordination are needed.
- Scenario: Cooperative SDA across GEO/XGEO/cislunar with intermittent/jammed links; assets must detect, classify, and act safely with minimal operator intervention.
- Proposed Solution (five innovations):
  - Edge Autonomy Stack — on‑device policy inference on rad‑tolerant compute with secure boot and safe runtime.
  - Safety/RTA + Operator Digest — runtime assurance and human‑oriented oversight artifacts.
  - Multi‑Host Tip‑and‑Cue (MARL) — collaborative tasking resilient to drop/jamming.
  - Space MLOps & V&V — signed updates, rollback, verification logs.
  - Standards & Interfaces — CCSDS/BM‑C2‑aligned schemas and stubs.
- Figures/Tables: Figure 1 (architecture). Table 1 (degree of innovation). Table 2 (topic alignment).
- Team: IA with COSMIAC; goal is a Phase I proof‑of‑feasibility and Phase II plan.

3) 1.01 Technical Approach
- Integrated, modular architecture: edge autonomy on rad‑tolerant compute; MARL coordination; safety/assurance; standards‑based interfaces.
- Subsections (each with challenge + DoI):
  1. Edge Autonomy Stack — low‑latency, low‑power policy inference with secure boot and memory‑safe runtime.
  2. Safety/RTA + Operator Digest — safety invariants, fallback behavior, and explainability traces.
  3. Multi‑Host Tip‑and‑Cue (MARL) — collaboration under comms limits; compare against baseline heuristics.
  4. Space MLOps & V&V — signed updates, rollback, SBOM/verification artifacts.
  5. Standards & Interfaces — CCSDS‑aligned data products and BM‑C2 stubs.
- Security & Compute: container hardening pathway; rad‑tolerant SoC/FPGA with optional accelerator within power/thermal envelopes.

4) 1.02 Alignment with Topic Requirements
- Table 2 maps AIS requirements to solution elements (edge autonomy, safety/assurance, coordination under comms limits, standards/interoperability, Phase I feasibility focus, STTR collaboration).

5) 1.03 Data, Evaluation, & Metrics
- Data: synthetic scenarios and heritage references for GEO/XGEO/cislunar; adversary and comms‑denied conditions.
- Table 3: metrics/goals/methods for autonomy latency/power, operator workload proxy, custody/time‑to‑classification, safety/RTA, and resilience.

6) 2.0 Phase I Technical Objectives
- Objective 1: Feasibility Study — documented technical/operational feasibility across focus areas; evidence: literature reviews, M&S, and trade studies; deliverables: initial report + feasibility assessment.
- Objective 2: CONOPS & Architectural Framework — system‑level CONOPS, operational overview, and architecture diagrams; deliverables: CONOPS document and architecture package.
- Objective 3: Edge Autonomy Stack Prototype (POLARIS) — on‑device policy inference on rad‑tolerant compute; evidence: HIL demo with latency/power traces; deliverables: prototype code + demo scorecard.
- Objective 4: Secure Updates & RTA Prototype — signed model/weight updates with rollback and safety cage; evidence: in‑the‑loop demo with audit/safety logs; deliverables: update runbook + logs.
- Objective 5: Multi‑Host Tip‑and‑Cue Feasibility — MARL‑based coordination resilient to comms limits; evidence: simulation campaign vs. baseline heuristics; deliverables: auto‑scorecards and comparison report.
- Objective 6: Standards & Interfaces Package — CCSDS/BM‑C2 schemas and interface stubs; evidence: sample data products and operator digest export; deliverables: schema set + stub endpoints.
- Objective 7: Space MLOps & V&V Pipeline Stub — signed export, verification artifacts, and SBOM; evidence: dry‑run update in sim/HIL; deliverables: CI template + verification logs.
- Objective 8: AIS Showcase & Phase II Proposal Package — final conference presentation and submission materials serving as the Phase II proposal; deliverables: slide deck and accompanying Phase II plan.
- Objective 9: POLARIS Advancement for Target HW & Multi‑Agent Scenarios — quantization/pruning/mapping for target SoC/FPGA and alignment to multi‑agent scenarios; evidence: perf vs. baseline on dev board + sim; deliverables: performance report + updated weights.

7) 3.0 Phase I Statement of Work (Base and Option)
- Deliverable modality per task: prototype demo and/or feasibility report with auto‑scorecards.
- Table 4 (Base, ~6 months): T1 Kickoff & literature/trade studies (feasibility report); T2 Edge Autonomy Stack concept demo with POLARIS on dev board (prototype + traces); T3 Safety/RTA & signed‑update demo‑in‑the‑loop (prototype + audit logs); T4 Multi‑Host tip‑and‑cue feasibility (sim campaign vs baseline; report + scorecards); T5 Standards & interfaces + operator digest stubs (schemas + sample exports); T6 Integrated demos & Phase II planning (integrated demo + planning memo).
- Table 5 (Option, ~6 months): T7 Advance POLARIS for target HW & multi‑agent scenarios (quantization/pruning/scheduling; prototype + performance report); T8 Expand MARL + message policy under jamming (sim campaign + ablation report); T9 Mid‑fidelity operator digest/BM‑C2 stubs (UI/workflow prototype + usability notes); T10 Architecture hardening & security planning (SBOM/keys/runbooks; security plan).
- Forward look to Phase II: documented development and demonstration plan for a flight‑like prototype, relevant‑environment testing, and end‑to‑end tip‑and‑cue with secure updates and operator digests.

8) 1.3 Related Work
- Table 6: IA and COSMIAC heritage most relevant to AURORA; key comparators; differentiation.
  - Interactive Aptitude (IA): POLARIS (RL training platform integrating Basilisk + Gymnasium for GEO/XGEO/cislunar); CMA‑SHIELD (TRL‑2 shielded MARL for multi‑satellite C2); NGSX (multi‑spacecraft autonomy testbed); SIERO (many‑vs‑many wargaming); DARPA ACK/ARAKNID (TRL‑9 multi‑domain C2 with Platform One CtF); HIL and digital twin experience.
  - COSMIAC (UNM): Rad‑tolerant compute and secure embedded/FPGA expertise (secure boot/root‑of‑trust); radiation effects testing; SDR/crosslink emulation and RF from ~450 MHz–84 GHz; two 24/7 ground stations; PNT/GNSS hardening; small‑sat build/test facilities; TS/SCI‑capable staff and labs.
  - Relevance to AURORA: IA provides MARL/edge autonomy lineage and sim‑to‑HIL pipelines; COSMIAC provides hardware benches and RF/space environmental validation to de‑risk on‑device autonomy and updates.
  - Comparators: prior rule‑based/heuristic coordinators and non‑certifiable on‑orbit AI; AURORA differentiates via certifiable updates + RTA + MARL under comms limits and standards‑aligned interfaces.

9) 2.0 Key Personnel
- Table 7: Key personnel roles (IA and COSMIAC).
  - IA — Chief Scientist: multi‑agent RL/autonomy for SDA; leads POLARIS/CMA‑SHIELD lineage.
  - IA — Chief Technology Officer (CTO): secure cloud‑native platforms; Platform One CtF; MLOps/standards integration.
  - IA — Principal Software Engineer: RL systems, edge integration, HIL prototyping; POLARIS/NGSX.
  - COSMIAC — Chief Scientist: secure embedded systems/FPGA, GNSS; secure boot/root‑of‑trust; radiation testing coordination.
  - COSMIAC — Deputy Director: space systems, controls/dynamics, ML/vision; HIL bench and SDR/crosslink emulation.
  - COSMIAC — Chief Engineer: modeling/simulation; RF/comm integration to benches.
  - COSMIAC — Director of Innovation: satellite comms and ground‑station integration; program transition.

10) 3.0 Commercialization/Transition Plan Summary
- 3.1 Overview; transition pathway (USSF/SDA); Phase I–III plan; engagements; dual‑use expansion; differentiation; risks/mitigations; revenue/scaling.
- Table 9: commercialization timeline milestones.

11) 4.0 Facilities/Equipment
- Computing resources, simulation toolchains, secure repos; COSMIAC rad‑tolerant compute benches and SDR/crosslink emulation; security controls.

12) 5.0 References
- Citations aligned to standards and related literature.

---

### Content Mapping (Crosswalk)
- Problem/Scenario → 1.0; Figures illustrate architecture and workflows.
- Innovation Modules → 1.01 (Edge Autonomy; Safety/RTA; Multi‑Host Tip‑and‑Cue; Space MLOps & V&V; Standards & Interfaces).
- Topic Compliance → 1.02 Table 2 maps AIS guidelines to modules and deliverables.
- Evaluation Plan → 1.03 Table 3 defines metrics/methods/success criteria.
- Objectives → 2.0; SoW & Schedule → 3.0 Tables 4–5.
- Transition & Commercialization → plan, engagements, dual‑use, risks, timeline.
- Organizational Capacity → Related Work, Key Personnel, Facilities/Equipment.

---

### Compliance Checklist (Guidelines → Where Addressed)
- Feasibility via lit reviews, M&S, and trade studies → 1.0, 1.03, 3.0.
- Risk reduction, feasibility validation, mission alignment → 1.0, 1.01, 1.03, 2.0.
- Scope, methods, collaboration (COSMIAC), expected outcomes → 1.0–5.0.
- Focus areas (Edge Computing & Algorithms; integration for Sensors/Bus) → 1.02; 1.01.
- Initial CONOPS and architectural framework → 1.0, 1.01; figures/tables.
- Phase I deliverables (reports, feasibility, CONOPS/architecture, Phase II plan, showcase) → 1.02; 3.0.
- STTR compliance (research institution workshare) → 1.0 Team; 3.0 SoW; 4.0 Facilities.
- Phase II outlook and transition relevance → 3.0 forward look; 3.0 Commercialization.

---

### Figures and Tables (as referenced)
- Figures: 1 (Architecture), 2 (Edge Autonomy HIL/flow), 3 (Multi‑Host MARL workflow), 4 (Operator Digest & BM‑C2 view).
- Tables: 1 (Degree of Innovation), 2 (Topic Alignment), 3 (Metrics), 4 (Base SoW), 5 (Option SoW), 6 (Related Work), 7 (Key Personnel), 9 (Commercialization Timeline).
