# AURORA — Acronyms and Definitions

This document spells out acronyms used in the AURORA proposal materials and provides concise definitions.

- AURORA — Autonomous Updatable Resilient On-orbit Reasoning Architecture: The integrated system/architecture for resilient edge autonomy, multi-agent coordination, runtime assurance, and standards-aligned interfaces.
- POLARIS — Platform for Operational Lifecycle, Algorithmic Research, and Integration in SDA-Operation: A previously demonstrated reinforcement learning (RL) policy engine integrated within AURORA’s edge autonomy stack.
- RL — Reinforcement Learning: A learning paradigm where agents learn policies to maximize expected reward through interaction with an environment.
- MARL — Multi-Agent Reinforcement Learning: RL with multiple interacting agents that must coordinate and/or compete under partial observability and communication constraints.
- CTDE — Centralized Training, Decentralized Execution: A MARL paradigm where training leverages centralized/global information, but execution uses only each agent’s local observations and limited comms.
- CBBA — Consensus-Based Bundle Algorithm: A distributed auction/market-style task allocation algorithm where agents greedily build ordered bundles of tasks and resolve conflicts via consensus steps.
- RTA — Run-Time Assurance: A safety mechanism (often using a Simplex architecture) that monitors a learning controller and intervenes/fallbacks to a safe controller when safety constraints are at risk.
- Simplex (Architecture) — A runtime safety pattern featuring a high-performance (possibly learning-based) controller overseen by a verified safety controller with arbitration to ensure constraint satisfaction.
- HIL — Hardware-in-the-Loop: Testing methodology where real hardware (e.g., compute boards, sensors) is integrated into a simulation to measure realistic latency, power, thermal, and fault behaviors.
- SoC — System on Chip: An integrated circuit that consolidates CPU, memory, and peripherals; in this context, a low-power rad-tolerant compute target for on-orbit inference.
- FPGA — Field-Programmable Gate Array: Reconfigurable hardware used for accelerating inference and implementing fault-tolerant logic in rad-tolerant designs.
- ECC — Error-Correcting Code (Memory): Memory techniques that detect and correct bit errors caused by radiation effects.
- TMR — Triple Modular Redundancy: A fault-tolerance technique that triplicates logic and uses majority voting to mask faults (e.g., radiation-induced upsets).
- SEU — Single Event Upset: A radiation-induced transient change of state (bit flip) in electronic devices.
- CCSDS — Consultative Committee for Space Data Systems: International standards body defining space data and communication standards used for interoperability.
- BM-C2 — Battle Management Command and Control: Command-and-control workflows and interfaces for operational decision support and tasking (often stylized BM/C2).
- DTN — Delay/Disruption-Tolerant Networking: Networking architecture designed for intermittent, high-latency links typical of space environments.
- BPv7 — Bundle Protocol version 7: The IETF/DTN protocol for store-and-forward message delivery in DTN networks.
- V&V — Verification and Validation: Processes for ensuring a system meets specifications (verification) and fulfills its intended purpose (validation).
- SBOM — Software Bill of Materials: A manifest of software components and dependencies to support supply-chain security and certification.
- M&S — Modeling and Simulation: Synthetic environment generation and simulation for evaluation, trade studies, and training.
- CONOPS — Concept of Operations: An operational description that articulates how a capability will be used, by whom, and under what conditions.
- SoW — Statement of Work: Contractual description of tasks, deliverables, and milestones for program execution.
- TRL — Technology Readiness Level: A scale (1–9) for assessing maturity of technologies.
- SDA — Space Domain Awareness: Detection, tracking, characterization, and understanding of resident space objects and activities.
- GEO — Geostationary Earth Orbit: Orbit at ~35,786 km altitude where satellites appear stationary relative to Earth’s surface.
- XGEO — Extended GEO regimes: Regions beyond GEO (e.g., high-altitude and cislunar regimes) relevant to SDA and mission operations.
- Cislunar — The space between Earth and Moon orbits, including lunar vicinity operations.
- USSF — United States Space Force: The U.S. military service branch responsible for space operations.
- ITAR — International Traffic in Arms Regulations: U.S. regulations controlling the export of defense-related materials and information.
- STTR — Small Business Technology Transfer: U.S. program funding R&D with mandatory small business–research institution collaboration.
- COSMIAC — Configurable Space Microsystems Innovations & Applications Center: A research center (University of New Mexico) specializing in space microelectronics and rad-tolerant compute; AURORA’s research institution partner.
- RMF — Risk Management Framework: NIST framework for managing information security and risk in federal systems.
- NIST SP 800-171 — Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations: Security requirements for handling CUI.
- FIPS 140-2 — Federal Information Processing Standard 140-2: U.S. government standard for cryptographic modules.
- DPU — Data/Deep-Learning Processing Unit: A dedicated accelerator for onboard inference (e.g., FPGA-resident deep-learning processing core); an optional adjunct to rad-tolerant SoC/FPGA within power/thermal/radiation envelopes.


