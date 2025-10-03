`1. Explore novel concepts and architectures that support enhanced autonomy,
survivability, and responsiveness in degraded or adversarial space
environments.`

- novel software hardware codesign, minimal, radiation hardened, cosmiac
- RL for rapid autonomy


`2. Assess the feasibility of onboard edge intelligence, predictive threat
analytics, and autonomous decision-making systems suitable for bandwidth-limited
or contested conditions.`

we could train an RL agent in POLARIS and deploy it on custom hardware with cosmiac
- FPGA, xilinx, etc
- custom minSOC, ASICS

assess feasibility of model updates in fpga fabric from ground upload

RL record autonamous decision and data, report back to ground


`3. Analyze modular, scalable systems—including sensor payloads, computing
elements, and spacecraft buses—that can adapt to evolving missions and orbital
domains.`

Can we make a modular "self driving brain" that can be attached to hosts?

standardized hw protocols/drivers and interface to RL control?


`4. Develop preliminary Concepts of Operations (CONOPS) aligned with
future USSF mission needs and evaluate potential integration paths with Space
Force operational constructs.`

Standardized hw protocols/drivers
RL update protocol
RL recording and reporting protocol

other conops:
when does RL kick in? 
can it override ground control and commands?
can we configure it's level of override access?

similar to self driving cars or driver augmenting emergency systems

could those override behaviors and emergency systems be exploited?
e.g. someone jumps in front of self driving car to force a stop so they can rob it. 
Is there an analog for an autonomous spacecraft?


Scope:
Polaris for RL training
Cosmiac collab for 
  - RL deployment
  - HW design
  - Radiation Hardening
  - Testing
  - update protocol
  - record and report protocol

Research methods:
use POLARIS (citations)

collaboration plan: -- cosmiac  TODO: more info

How work could inform a Phase II prototype or proof of concept demo and support longer term relevance:

Actually build out hardware, sat bus
Actually deploy RL agent on hardware
Actually test in COSMIAC labs 
Actually deploy to space!

Q: RL training across multiple assets in constellation? Hive RL? 
Q: can our deployed RL agent continuously collect training data for future RL agents?

areas to address:

1. Edge computing -- this is us!

2. Sensors payloads: eyes and ears of RL system ?

3. Bus design  -- yes this one!
This could be us!
hw sw modularity
reconfigurability
architectures enabling lifecycle extension

Proposal must haves :
- research plan including
  - modeling and sim (POLARIS)
  - lit review
  - or trade studies

I think we could develop RL agent friendly and performant HW
Use prototype SW/HW codesign tools like Xilinx
Plan out custom HW solution

CONOPS guide:
communicate how tech is intended to support military mission
help develop operational and system-level requirements
- point out specific USSF mission and objectives
- problem addressed by technology
- operational overview diagram
- integration-ready design for sensors, computing, and maneuver systems

End goals of feasibility study
- identify benefits over existing solutions (or lack thereof)
- identifie risks, uncertanties, unkowns, anad mitigations
- idtentify critical technology elements (CTEs)
- data supporting feasibility of each CTE

outline:
15 page max length
efforts may include:

lit review
model and sim studies
preliminary architecture definitions, trade space analysis
operational use case development, mapped to current or projected Space Force mission needs
identification of technical risks and mitigation strategies

We must clearly describe how effort will:
- Leverage the capabilities and domain expertise of the affiliated research institution
  - cosmiac for research, hw testing, lab, etc.
- Advance the small business’s internal research and development (IR&D) toward a defensible technical approach
  - use POLARIS for RL training
- Inform a future Phase II prototype or proof-of-concept demonstration effort, including early thoughts on transition, testability, and alignment with Space Force capability development priorities
  - develop custom IC with cosmiac, deploy on cube sat!

P1 deliverables:
- feasibility assessment
- initial conops and architecture framework
- phase II development plan
- final report for AIS showcase (must be included in milestone schedule)
