# SF25D-T1201: Adaptive and Intelligent Space (AIS)

**Topic:** Adaptive and Intelligent Space (AIS)  
**Agency:** DoD STTR 2025.D  
**Branch:** USAF / Space Force  
**Customer:** Task Force Futures + SpaceWERX  
**Opens:** 10/08/2025  
**Closes:** 11/05/2025  
**Status:** Pre-Release  
**Type:** STTR Phase I (with unique Phase II selection process)

## Technology Areas
- Space Platforms

## Modernization Priorities
- Space Technology

## Keywords
Space Domain Awareness (SDA); Space Control (SC); Space Battle Management (SBM); Passive RF; LIDAR; Radar Detection Technologies; Next-Gen Sensor Solutions; Machine Learning; AI; Radiation-Hardened; Real-Time Data Processing; Rapid response

---

## Analysis: What You'd Actually Build

### The Core Problem
The Space Force needs satellites that can **think for themselves** in contested space. Current satellites are:
- **Dumb** - Require constant ground control
- **Slow** - Data goes to ground, humans analyze, commands sent back up (minutes to hours)
- **Vulnerable** - Can't respond to threats autonomously
- **Inflexible** - Can't adapt to new missions or threats

In a space war, communications could be jammed, ground stations attacked, or satellites need to respond in seconds, not hours. They need **autonomous, intelligent satellites** that can detect threats, make decisions, and take action without waiting for ground control.

### What You'd Build

This is a **research and feasibility study** topic (Phase I), not building hardware yet. You'd investigate one or more of three focus areas and develop a **Concept of Operations (CONOPS)** and **feasibility study** for future prototype development.

#### Three Focus Areas (Choose One or More):

**1. Edge Computing & Algorithms**
Build the "brain" - AI/ML systems that run onboard satellites for autonomous decision-making.

**What you'd research:**
- Onboard threat detection and response algorithms
- Radiation-hardened edge computing architectures
- AI/ML models that work in space (limited power, radiation, no internet)
- Autonomous maneuver detection and collision avoidance
- Data fusion from multiple sensors
- Reducing kill-chain latency by 50%+ and operator workload by 25%+

**Example capabilities:**
- Satellite detects another satellite maneuvering toward it → AI classifies threat level → Autonomously takes evasive action
- Fuses data from multiple sensors → Detects missile launch → Alerts network in <10 seconds
- Detects cyber attack or data poisoning → Self-heals and maintains mission

**2. Sensor Payloads**
Build the "eyes and ears" - Advanced sensors with integrated processing for space domain awareness.

**What you'd research:**
- Modular sensor packages (passive RF, LIDAR, radar, IR, hyperspectral)
- Multi-modal detection and fusion
- Software-defined/reconfigurable sensors
- Persistent tracking across LEO, GEO, XGEO, cislunar
- High-performance computing at the sensor (HPC-S)
- Improved resolution and sensitivity

**Example capabilities:**
- Passive RF sensor detects adversary satellite communications → Characterizes intent
- LIDAR tracks multiple objects simultaneously → Maintains custody through maneuvers
- Hyperspectral imaging identifies satellite type and payload → Attributes capabilities
- All-weather sensing (can look into sun, through clouds)

**3. Bus Design**
Build the "body" - Modular, autonomous spacecraft platforms that can adapt to changing missions.

**What you'd research:**
- Modular hardware/software architectures
- Autonomous vehicle management (power, thermal, propulsion)
- High delta-V for rapid maneuvers
- Autonomous collision avoidance
- Lifecycle extension and reconfigurability
- Integration-ready for sensors and compute

**Example capabilities:**
- Satellite autonomously load-sheds non-critical systems when under attack
- Rapidly integrates new sensor payload without redesign
- High maneuverability for evasive action or orbit changes
- Autonomous thermal management for edge computing loads

### Concrete Use Case Example

**Scenario:** Adversary satellite approaches U.S. asset in GEO

**Current System:**
1. Ground sensor detects approach (delayed)
2. Data downlinked to ground station (minutes)
3. Analysts assess threat (hours)
4. Commands uplinked to satellite (minutes)
5. Satellite maneuvers (if comms not jammed)
**Total time:** Hours. **Result:** Too slow, possibly compromised

**With Your AIS Technology:**
1. **Onboard sensors** (your Focus Area 2) detect approach immediately
   - Passive RF characterizes adversary satellite
   - LIDAR tracks trajectory and closing velocity
   - Multi-modal fusion confirms threat
2. **Edge AI** (your Focus Area 1) analyzes in real-time
   - Threat classification: 95% confidence hostile intent
   - Predicts intercept in 45 minutes
   - Calculates evasive maneuver options
3. **Autonomous bus** (your Focus Area 3) responds
   - Prioritizes mission-critical systems
   - Executes evasive maneuver autonomously
   - Maintains sensor custody of threat
   - Alerts network of threat (when comms available)
**Total time:** <5 minutes. **Result:** Threat avoided, mission continues

### What You're Actually Delivering (Phase I)

**Phase I is RESEARCH, not building hardware:**

**Deliverables:**
1. **Literature Review** - State-of-the-art assessment
2. **Feasibility Study** - Technical viability analysis
3. **CONOPS** - Concept of Operations for USSF missions
4. **Modeling & Simulation** - Performance analysis
5. **Trade Studies** - Technology options and comparisons
6. **Risk Assessment** - Technical risks and mitigations
7. **Phase II Plan** - Roadmap for prototype development
8. **AIS Phase I Showcase** - Presentation and documentation (critical!)

**Key Requirement:** Must collaborate with a **research institution** (university or non-profit)

**Unique Aspect:** Phase I ends with **AIS Phase I Showcase** in El Segundo, CA. Your showcase presentation and documentation **IS your Phase II proposal**. No separate Phase II proposal required!

### Phase Deliverables

#### Phase I (~$200K-$300K, 6-8 months):
**Research Activities:**
- Literature reviews and state-of-the-art assessments
- Modeling, simulation, analytical studies
- Architecture definitions and trade space analysis
- Operational use case development
- Technical risk identification and mitigation strategies
- **Collaboration with research institution**

**Deliverables:**
- Initial report
- Documented feasibility assessment
- Initial CONOPS and architectural framework
- Proposed Phase II development plan
- Final report
- **AIS Phase I Showcase documentation:**
  - Proposal Cover Sheet (Volume 1)
  - Technical Volume (5 pages max) (Volume 2)
  - Cost Volume (Volume 3)
  - Company Commercialization Report (Volume 4)
  - Fraud, Waste, Abuse Training (Volume 6)
  - Foreign Affiliations Disclosure (Volume 7)
  - Presentation Slide Deck (10 slides max)

**Critical:** The showcase presentation IS your Phase II proposal!

**Travel:** Budget for 2 people to attend showcase in El Segundo, CA

#### Phase II (~$1.1M, 24 months):
**If selected at showcase, you'd build:**
- Functional prototype or proof-of-concept demonstration
- Software, hardware, or integrated systems
- Validation of capabilities identified in Phase I
- Demonstration in relevant environment
- Integration with Space Force mission concepts

**Example Phase II outcomes:**
- Working edge AI system for threat detection (TRL 5-6)
- Prototype sensor payload with integrated processing
- Modular bus design with autonomous capabilities
- Demonstrated 50% reduction in kill-chain latency

#### Phase III (follow-on):
- Operational deployment
- Commercial applications
- Certification and accreditation
- Integration with Space Force systems
- Scale-up and productization

### Key Technical Challenges

**Edge Computing & Algorithms:**
- **Radiation tolerance** - Space radiation destroys electronics
- **Power constraints** - Limited power for AI processing
- **Thermal management** - Heat dissipation in vacuum
- **Data poisoning resilience** - Adversary feeding bad data to AI
- **Autonomous decision-making** - Safety and reliability
- **Real-time processing** - Low latency requirements

**Sensor Payloads:**
- **SWaP** - Size, Weight, and Power constraints
- **Multi-modal fusion** - Combining different sensor types
- **Persistent tracking** - Maintaining custody through maneuvers
- **Blind spots** - Solar exclusion angles, cone of shame
- **Sensitivity** - Detecting small or stealthy objects
- **Cislunar operations** - Extreme distances

**Bus Design:**
- **Modularity** - Plug-and-play sensors and compute
- **High delta-V** - Fuel for rapid maneuvers
- **Thermal management** - Handling edge computing heat
- **Autonomous operations** - Safe, reliable autonomy
- **Lifecycle extension** - Adapting to new missions
- **Integration** - Sensors, compute, propulsion working together

### Dual Use Applications

Strong commercial potential across multiple sectors:

**Space Industry:**
- **Commercial satellite operators** - Autonomous operations for mega-constellations
- **Space situational awareness** - Commercial SSA services
- **On-orbit servicing** - Autonomous rendezvous and proximity operations
- **Cislunar economy** - Moon missions and beyond

**Other Industries:**
- **Autonomous vehicles** - Edge AI and sensor fusion
- **Critical infrastructure** - Autonomous threat detection
- **Maritime** - Autonomous ship operations
- **Aviation** - Autonomous aircraft systems
- **Robotics** - Autonomous decision-making in harsh environments

---

## Why This Fits Your Criteria

This is an **OUTSTANDING fit** for:
- ✅ **AI/ML** - Core focus on autonomous decision-making
- ✅ **Edge Computing** - Running AI on resource-constrained hardware
- ✅ **Sensor Fusion** - Multi-modal data integration
- ✅ **Real-time Systems** - Low-latency processing requirements
- ✅ **Software Engineering** - Complex autonomous systems
- ✅ **Modeling & Simulation** - Phase I is heavily simulation-focused
- ✅ **Computer Vision** - Sensor processing and object detection
- ✅ **Reinforcement Learning** - Autonomous decision-making
- ✅ **Databases** - Managing sensor data and knowledge bases
- ⚠️ **Space Domain** - Understanding of space operations helpful
- ⚠️ **Research Institution** - MUST partner with university/non-profit (STTR requirement)

**This is probably your BEST fit overall** - combines AI/ML, edge computing, sensor fusion, real-time systems, and has massive commercial potential. Plus, Phase I is research-focused (your strength) before committing to hardware.

---

## Topic Details from Solicitation

### Objective
Investigate technical and operational feasibility of emerging space concepts and dual-use technologies for autonomous, resilient, and intelligent space operations across LEO, GEO, XGEO, and cislunar environments.

### Phase I Focus
Early-stage research activities:
- Literature reviews
- Modeling and simulation
- Trade space analyses
- University/non-profit research collaborations
- Reduce risk and validate feasibility
- Refine mission alignment

### Core Objectives
1. Explore novel concepts for enhanced autonomy, survivability, responsiveness in degraded/adversarial environments
2. Assess feasibility of onboard edge intelligence, predictive threat analytics, autonomous decision-making
3. Analyze modular, scalable systems adaptable to evolving missions
4. Develop preliminary CONOPS aligned with USSF mission needs

---

## Three Focus Areas (Detailed)

### 1. Edge Computing & Algorithms

**Desired Capabilities:**
- Onboard threat analytics
- Resilient, secure, radiation-tolerant edge computing
- 50% reduction in kill-chain latency
- 25% reduction in operator workload
- Discrimination in contested environments
- Resilience to data poisoning, sensor degradation

**Desired Technologies:**
- Predictive threat analytics and orchestrated response
- Thermal management and radiation-hardened solutions
- Neuromorphic computing
- Data security and encryption
- Anomaly/maneuver detection AI/ML
- Tip & Cue capability between SDA and coordination functions
- Memory-safe language applications
- Zero-trust onboard computation
- Data compression algorithms
- Cislunar simulation and visualization tools

### 2. Sensor Payloads

**Desired Capabilities:**
- Integrated sensor-computing packages for persistent tracking
- Novel SDA collection and data fusion
- Higher fidelity persistent space object custody
- Attribute in-space actions across multiple spectra
- Software-defined or reconfigurable payloads
- Improved satellite change detection and maneuvers

**Desired Technologies:**
- Passive RF, LIDAR, radar, IR, hyperspectral sensors
- HPC-S (high-performance computing at the sensor)
- Space-based sensing for GEO, XGEO, cislunar
- Quantum sensors
- SAR (Synthetic Aperture Radar)
- Neuromorphic sensors

### 3. Bus Design

**Desired Capabilities:**
- Hardware modularity for rapid technology integration
- Software modularity for autonomous capabilities
- Reconfigurability across mission profiles
- All-of-vehicle autonomous optimization
- Autonomous load-shedding under duress
- Autonomous collision avoidance maneuvers

**Desired Technologies:**
- Lifecycle extension architectures
- Modular tech and adaptive interfaces
- Platforms designed to adapt without re-architecture
- Integration-ready design for sensors, compute, maneuver
- High delta-V with thermal management
- Onboard power for edge computing

---

## CONOPS and Feasibility Study Requirements

### CONOPS Must Include:
- USSF mission and military objectives
- Problem being addressed (capability gap)
- Operational overview diagram
- System architecture overview diagram
- Integration-ready design for sensors, computing, maneuver

### Operating Concept:
Space Control and Battle Management supported through total Space Domain Awareness:
- Persistent, predictive, precise SDA
- Tracking and characterization of objects
- Attribution of intent and behavioral analysis
- Predictive targeting
- Integration across commercial sensors
- AI-driven decision aids
- Real-time orbital maneuver detection

### Feasibility Study Must Include:
- Benefits of new technology over existing solutions
- Risks, uncertainties, issues with mitigation measures
- Critical Technology Elements (CTEs)
- Data supporting feasibility of each CTE:
  - Literature research
  - Trade studies
  - Technical analysis
  - Heritage usage of similar technology

---

## References

1. "How US Space Command is preparing for satellite-on-satellite combat." The Economist, July 27, 2025.

2. "Space Warfighting - A Framework for Planners." Space Force, April 10, 2025.

3. RAND Research Report: https://www.rand.org/pubs/research_reports/RRA2318-1.html

4. IEEE Paper on Space AI/ML: https://ieeexplore.ieee.org/document/10115983

5. NASA Current Technology in Space: https://ntrs.nasa.gov/api/citations/20240001139/downloads/Current%20Technology%20in%20Space%20v4%20Briefing.pdf

6. Lockheed Martin AI/ML Mission Processing: https://www.lockheedmartin.com/content/dam/lockheed-martin/space/documents/ai-ml/PIRA-aiaa-6.2022-1472-aiml-mission-processing-onboard-satellites-paper.pdf

---

## Q&A from Solicitation

**Q: Would a hardware-agnostic flight software architecture inclusive of autonomy stack with OODA capability be of interest?**
A: Response Pending

**Q: For Sensors Payload, is there interest in characterization of charged particles from artificial source vs environmental plasma?**
A: Response Pending

**Q: Page limit clarification - does 15 pages include cover, TOC, glossary?**
A: For Phase I proposals, you do NOT need to include TOC, Glossary, or other supporting documents. Those are only for Phase II/D2P2 proposals.

---

## Important Notes

### STTR Requirement
**MUST partner with a research institution** (university or non-profit). This is a Small Business Technology Transfer (STTR) topic, not SBIR. The research institution must perform at least 30% of the work in Phase I and 40% in Phase II.

### Unique Phase II Selection Process
- Phase I ends with **AIS Phase I Showcase** in El Segundo, CA
- Your showcase presentation and documentation **IS your Phase II proposal**
- No separate Phase II proposal submission
- Phase II awards decided based on showcase performance
- Budget for 2 people to travel to showcase

### Proposal Requirements
- **Phase I:** 15 page technical volume limit
- **Showcase:** 5 page technical volume + 10 slide deck
- Must include CONOPS and feasibility study
- Must describe research institution collaboration
- Must outline Phase II transition plan

### Phase I Deliverables
- Initial report
- Feasibility assessment
- CONOPS and architectural framework
- Phase II development plan
- Final report
- **AIS Phase I Showcase documentation** (critical!)

### Customer
- Primary: Task Force Futures
- Partner: SpaceWERX
- End user: U.S. Space Force

### ITAR
**Yes, this topic is ITAR-restricted.** Must disclose foreign nationals and comply with export control laws.

### Funding Estimates
- Phase I: ~$200K-$300K, 6-8 months
- Phase II: ~$1.1M, 24 months
- Phase III: Non-SBIR/STTR funding

### Key Success Factors
1. Strong research institution partnership
2. Clear, compelling CONOPS aligned with USSF needs
3. Rigorous feasibility study with technical depth
4. Excellent showcase presentation
5. Demonstrated understanding of space operations
6. Clear path to Phase II prototype

