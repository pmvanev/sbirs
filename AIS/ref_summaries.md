## References

1. "How US Space Command is preparing for satellite-on-satellite combat." The Economist, July 27, 2025.
   - Summary: Reporting indicates U.S. Space Command is preparing for co-orbital and on-orbit interference threats (jamming, dazzling, grappling, proximity ops) and rehearsing satellite-on-satellite contingencies. Themes include rapid attribution, rules of engagement that minimize debris, operating under comms/jamming, and accelerating decision timelines with automation.
   - Relevance to AIS: Underscores the solicitation’s need for onboard autonomy to detect, classify, and respond to threats when ground links are degraded; supports AIS aims to reduce kill-chain latency, enable autonomous collision avoidance/evasive maneuvers, and maintain mission under attack.

2. "Space Warfighting – A Framework for Planners." United States Space Force, April 10, 2025. PDF: https://www.spaceforce.mil/Portals/2/Documents/SAF_2025/Space_Warfighting_-_A_Framework_for_Planners_BLK2_(final_20250410).pdf
   - Summary: USSF doctrinal guidance describing the competition–contest–conflict continuum, the objective of space superiority, and mission areas including Space Domain Awareness (SDA), Defensive/Offensive Space Control, Battle Management/C2, and targeting. Emphasizes resilience, agility, and rapid, integrated kill chains across orbits.
   - Relevance to AIS: Provides authoritative language and mission alignment for AIS CONOPS. AIS deliverables (autonomy, resilient edge compute, sensor fusion, maneuver) map directly to doctrinal needs: persistent SDA, decision advantage with reduced timelines, and autonomy under contested conditions.

3. RAND Research Report: Artificial Intelligence and Machine Learning for Space Domain Awareness (RRA2318-1). Landing page: https://www.rand.org/pubs/research_reports/RRA2318-1.html
   - Summary: Surveys AI/ML applications for SDA (detection, classification, characterization, maneuver prediction, multi-sensor fusion), identifies key challenges (data scarcity/labeling, domain shift, on-orbit vs. ground processing trade-offs, verification/validation/trust), and recommends MLOps practices (simulation, synthetic data, active learning, performance monitoring) tailored to space.
   - Relevance to AIS: Directly informs Phase I literature review and feasibility analysis for Focus Area 1 (Edge Computing & Algorithms). Offers risk-reduction guidance for dataset curation, model selection for constrained hardware, and V&V strategies needed for autonomous, safety-critical decisions.

4. IEEE Aerospace 2023: "Autonomous Multi-phase Rendezvous, Proximity Operations, and Docking via Model Predictive Control" (DOI: 10.1109/AERO55745.2023.10115983). https://ieeexplore.ieee.org/document/10115983
   - Summary: Proposes a multi-phase Model Predictive Control (MPC) approach for RPOD with phase-specific controllers to handle differing constraints (e.g., LOS cones). Demonstrates in simulation fuel-efficient, constraint-respecting trajectories suitable for onboard computation.
   - Relevance to AIS: Provides a concrete, publishable method for autonomous maneuver planning and collision avoidance that can execute at the edge. Supports AIS Focus Areas 1 and 3 by showing how onboard algorithms can meet real-time and safety constraints.

5. NASA "Current Technology in Space v4 Briefing" (2024). PDF: https://ntrs.nasa.gov/api/citations/20240001139/downloads/Current%20Technology%20in%20Space%20v4%20Briefing.pdf
   - Summary: A broad reference on AI/ML for Ground, Edge/Tiny/Mobile, and Space environments, including a reference architecture, Space MLOps lifecycle, and a detailed hardware landscape. Compares processors for throughput/latency, radiation tolerance, power, sensor I/O, and maintainability; advocates heterogeneous compute and certifiable update pathways.
   - Relevance to AIS: Directly supports AIS architecture and trade studies across Focus Areas. Offers evidence-based choices for radiation-tolerant edge compute, power/thermal budgeting for AI workloads, and certified MLOps needed for safe on-orbit model updates and resilience.

6. Lockheed Martin: "AI/ML Mission Processing Onboard Satellites" (AIAA paper, 2022). PDF: https://www.lockheedmartin.com/content/dam/lockheed-martin/space/documents/ai-ml/PIRA-aiaa-6.2022-1472-aiml-mission-processing-onboard-satellites-paper.pdf
   - Summary: Describes on-board mission processing architectures and pipelines for AI/ML on satellites, including SWaP-aware design patterns, data handling/compression, scheduling, and heterogeneous compute (CPU/GPU/FPGA/SoC). Includes mission use cases (e.g., onboard detection/classification) and performance considerations.
   - Relevance to AIS: Demonstrates feasibility and design patterns for achieving AIS objectives (e.g., >50% kill-chain latency reduction) with onboard inference. Informs hardware/software partitioning, toolchains, and update strategies for resilient autonomy under space constraints.
