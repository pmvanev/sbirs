## Interactive Aptitude (IA) — Overview

Website: https://interactiveaptitude.com/

Interactive Aptitude LLC is a software engineering and AI/ML company focused on delivering mission-ready solutions for DoD and dual‑use customers. IA specializes in multi‑domain command and control (C2), platform‑level autonomy, data fusion/management, and research‑to‑operations transition. The team prototypes rapidly and integrates into existing DoD systems using a tiered, low‑risk approach.

### Capabilities and Technical Expertise
- Simulation and virtual environment modeling; dynamic system replication; scenario‑based training; predictive outcome analysis; interactive process simulations
- Business automation and operational workflow optimization; resource/cost efficiency; QA automation and cybersecurity hardening; predictable/scalable outcomes
- Machine learning and data intelligence: large‑scale analytics, cognitive computing, information extraction and analysis, strategic data interpretation
- Software engineering: cloud‑native platforms, comprehensive web engineering, cloud transformation, legacy system revitalization, software engineering process management
  - Source: https://interactiveaptitude.com/capabilities/

### Facilities, Security, and Infrastructure
- Secure computing: private cloud optimized for ML workloads (high‑end GPUs, large storage/memory); scalable AWS cloud (e.g., SageMaker, Redshift)
- Facility Clearance with DCSA; personnel hold active Secret clearances (upgradeable for future phases)
- Compliance and controls: DoD RMF, NIST SP 800‑171; FIPS 140‑2 encryption for data in transit/at rest; RBAC and MFA; regular audits/validation for CUI handling
- Classified workspaces: secure facilities at Robins AFB and Hanscom AFB; partner with Westway Enterprises for turn‑key secure space solutions
  - Local source: AIS/orchestra_example/orchestra_proposal_raw.md (Facilities/Equipment)

### Representative Work and Products (selected)
- DARPA ACK/ARAKNID (sub to RTX): advanced HTN kill‑webs; TRL‑9 deployment supporting NORAD/NORTHCOM; multiple live multi‑domain exercises, Platform One Certificates to Field
- IA Data Management Suite: multimodal ISR fusion, explainable AI, and edge processing; work spans DARPA SAIL‑ON, PerSEAS, SquadX, XAI, LwLL, PANDA
- Live Policy Advisor (commercial product): AI/LLM‑driven compliance automation; customers include Amazon and FlyWire
- CMA-SHIELD: TRL2 multi-satellite decentralized onboard C2 using Deep Reinforcement Learning policies; demonstrated superior performance over rule-based approaches
- NGSX: Next Generation Space eXchange - comprehensive platform for development and testing of single and multi-spacecraft autonomy in virtual, constructive, and live scenarios
- SIERO: Synchronized Intelligence for EMSO Rapid Orchestration - advanced AI technology for many vs. many wargaming scenarios with adaptive adversaries
- POLARIS: Platform for Operational Lifecycle, Algorithmic Research, and Integration in SDA-Operations - RL training platform with Basilisk + Gymnasium integration
  - Local source: AIS/orchestra_example/orchestra_proposal_raw.md (Related Work)

### Multi-Agent Reinforcement Learning Experience

Interactive Aptitude has extensive experience in multi-agent reinforcement learning (MARL) and collaborative autonomy systems:

#### POLARIS Platform
- **POLARIS (Platform for Operational Lifecycle, Algorithmic Research, and Integration in SDA-Operations)**: RL training platform integrating Basilisk astrodynamics simulator with Gymnasium environments
- Supports training and deployment of RL policies for space domain applications including GEO/XGEO/cislunar regimes
- Enables joint optimization of solar charging, sensor tasking, tip-and-cue, and communications downlink with safety constraints
- Provides sim-to-policy pipeline with safety shields and rule-based guardrails for "never exceed" constraints

#### Multi-Agent Space Systems
- **CMA-SHIELD (Collaborative Mission Autonomy with Shielded Deep Reinforcement Learning)**: TRL2 implementation of multi-satellite decentralized onboard command and control using novel Deep Reinforcement Learning policies
- Managed hundreds of dynamic prioritized ground imaging requests from dispersed tactical requestors
- Considered complex spacecraft constraints including momentum wheel desaturation and battery discharge limitations
- Demonstrated superior performance over rule-based approaches for request fulfillment, long-time-horizon spacecraft safety planning, and re-training generalizability
- Pioneered "Shielded Deep Reinforcement Learning" (SDRL) policies that outperform rule-based policies, especially for spacecraft safety metrics

#### Multi-Domain Command and Control
- **DARPA ACK/ARAKNID**: TRL9 deployment of Hierarchical Task Network (HTN) kill-webs for multi-domain C2
- Rapidly evaluates thousands of Courses of Action (CoAs) in seconds using HTN planning and probabilistic reasoning
- Automatically pairs sensors to effectors across space, air, ground, maritime, and cyber domains
- Validated through 23+ live multi-domain exercises and deployed to NORAD/NORTHCOM for missile defense operations
- Achieved Platform One integration with three Certificates to Field

#### Simulation and Training Platforms
- **NGSX (Next Generation Space eXchange)**: Comprehensive platform for development and testing of single and multi-spacecraft autonomy in virtual, constructive, and live scenarios
- Supports adversary modeling with wargaming research and development for multi-agent scenarios
- Enables training of spacecraft operators in collaborative autonomous operations
- **SIERO (Synchronized Intelligence for EMSO Rapid Orchestration)**: Advanced AI technology for many vs. many wargaming scenarios
- Integrates diverse EMSO data sources and simulates adaptive adversaries for air and space platforms
- Enables dynamic many vs. many wargaming scenarios including onboard Cognitive Electronic Warfare AI mode switching

#### Distributed Coordination and Tip-and-Cue
- Experience in collaborative distributed tip-and-cue across multiple spacecraft via crosslinks
- Policies that coordinate tasking to maintain custody and reduce time-to-classification
- Integration of onboard triage and priority queues for evidence sharing in multi-agent systems
- Demonstrated robustness under communications degradation and contested environments

### Major Program Experience and Funding

#### DARPA Programs (Total: $26.1M+)
- **DARPA SAIL-ON** (Science of Artificial Intelligence and Learning for Open-world Novelty): HR001120C0055; $6.89M; 2019-2023
- **DARPA PerSEAS** (Persistent Stare Exploitation and Analysis System): HR001110C0112; $8.92M; 2011-2014
- **DARPA SquadX** Core Technologies: BAA-15-26; $6.86M; 2015-2018
- **DARPA ACK** (Adaptive Cross-Domain Kill-Webs): FA8750-19-C-0056 (sub to RTX); $1.5M; 2019-2023
- **DARPA XAI** (Explainable AI): N66001-17-2-4028; $1.5M; 2017-2021
- **DARPA LwLL** (Learning with Less Labels): FA8750-19-1-0504 (sub to UC Berkeley); $1.86M; 2019-2020

#### Space Force/Air Force Programs (Total: $5.6M+)
- **NGSX** (Next Generation Space eXchange): Three task orders under HII subcontract P000047413; $2.89M; 2023-2025
- **SIERO** (Synchronized Intelligence for EMSO Rapid Orchestration): HII subcontract P000047413; $1.0M; 2023-2025
- **RAISR** (Robust Artificial Intelligence Simulation Registry): FA864923P1166; $1.25M; 2023-2025
- **CMA-SHIELD**: AFRL contracts FA864921P0137 (P1) and FA864922P0833 (P2); $0.85M; 2021-2023
- **ASTROEDGE**: SBIR FA875024CB122; 2024-2025
- **POLARIS**: STTR FA955025PB003; 2025

#### Current Active Programs
- **HERA** (Hypothesis Evaluation and Reasoning Assistant): STTR FA875025CB003; 2024-2025
- **BASETWIN** (Building Automation Systems for Efficient Twin-computation): STTR FA254124PB008; 2024-2025
- **OPTIMA** (OPTimization and In-process Monitoring for Additive-manufacturing): Army STTR W58RGZ25C0005; 2025

### Technical Achievements and Performance Metrics

#### Multi-Agent RL Performance Improvements
- **CMA-SHIELD**: Demonstrated superior performance over rule-based approaches for multi-satellite coordination
- **ASTROEDGE**: RL policy achieved 37% reduction in sensor operations, 42% increase in observation frequency, and 28% reduced power consumption
- **ARAKNID**: Evaluates thousands of CoAs in seconds with real-time sensor-effector pairing across multiple domains
- **POLARIS**: Targets >50% reduction in decision latency vs. ground-loop baseline with >99.9% safe-action rate

#### Operational Deployments and Validation
- **ARAKNID**: TRL9 deployment to NORAD/NORTHCOM for US-Canada missile defense operations
- **Platform One Integration**: Three Certificates to Field for ARAKNID system
- **Live Exercise Validation**: 23+ live multi-domain exercises demonstrating ARAKNID's adaptability and performance
- **Multi-Domain Operations**: Validated across space, air, ground, maritime, and cyber domains

#### Simulation and Training Capabilities
- **Basilisk Simulator**: Open-source astrodynamics simulation used by dozens of industry, academic, and government research labs
- **NGSX**: Supports thousands of Resident Space Objects (RSOs) with high-performance computing paradigms
- **Hardware-in-the-Loop**: Demonstrated HIL capabilities for spacecraft autonomy development and testing
- **Digital Twin Technology**: High-fidelity modeling for spacecraft systems including momentum wheel saturation, battery depletion, and fuel constraints

### Key Personnel
- James Vaccaro, PhD — Founder & Chief Scientist
- Victor Bajenaru — Chief Operating Officer
- Chris Wheeler — Chief Technology Officer
- Eran Swears, PhD — Chief Growth Officer
- Deborah Botkin — Principal Research Engineer
- Maxwell Calkin — Software Engineer
- Matt Folsom — Principal Research Engineer
- Phil Van Every — Principal Software Engineer
- David Rawlins — Principal Research Engineer
  - Source: https://interactiveaptitude.com/about/

### Registrations and Codes
- CAGE: 9APD7
- UEI: T6NLUFWABL29
- NAICS: 541715, 541511, 541512, 541513, 541519, 541611, 541614, 541618, 541690, 541990, 518210, 519290
  - Sources: https://interactiveaptitude.com/ and https://interactiveaptitude.com/capabilities/

### Customers and Collaborators (examples)
- DoD and DARPA programs; NORAD/NORTHCOM; Platform One integrations
- Commercial clients include Amazon and FlyWire (for compliance automation)
  - Local source: AIS/orchestra_example/orchestra_proposal_raw.md

### Quick Facts
- Headquarters: 13232 Carolee Ave., San Diego, CA 92129; distributed team operating across six states
- Contact: inquiries@interactiveaptitude.com
  - Sources: https://interactiveaptitude.com/ and https://interactiveaptitude.com/about/
