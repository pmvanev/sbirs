# AIS Sensors Subtopic — Real-World Warfighting Use Cases

Purpose: Provide concrete, operationally grounded use cases for space-based sensor payloads (with on-sensor/edge processing) aligned to Space Force missions (SDA, Space Control, Battle Management/C2, Missile Warning/Tracking) and AIS objectives (persistent custody, multi-spectral attribution, reduced kill-chain latency, reconfigurable/software-defined sensing).

---

## 1) GEO “Neighborhood Watch” and Close Approach Characterization
- Mission drivers: Defensive Space Control, Space Domain Awareness (SDA), Battle Management/C2
- Real missions:
  - GSSAP (Geosynchronous Space Situational Awareness Program) — space-based SDA in near-GEO supporting USSPACECOM space surveillance ops; “neighborhood watch” for GEO (USSF Fact Sheet)
  - Silent Barker / NROL-107 — joint USSF/NRO SDA architecture providing enhanced detection/monitoring of objects and behaviors in GEO
- Operational needs addressed:
  - Rapid detection of proximity operations, approach vectors, and conjunction risk in GEO
  - Onboard attribution cues (optical/IR signatures, kinematics) to classify intent and behavior changes without waiting on ground
  - Tip-and-cue to other sensors and battle management nodes to reduce response timelines
- Sensor payload angles:
  - Optical/IR star-camera-class sensors with high dynamic range; on-sensor image differencing for maneuver/change detection
  - Passive RF payloads to characterize emissions, support intent attribution
  - Software-defined sensing modes (long/short exposure switching, dynamic ROI)

References: USSF GSSAP Fact Sheet; NRO/USSF Silent Barker press; C4ISRNET coverage.

---

## 2) Missile Warning and Hypersonic/Dim-Target Tracking (OPIR + LEO Tracking Layers)
- Mission drivers: Missile Warning/Missile Defense, Battle Management/C2
- Real missions:
  - SBIRS (Space Based Infrared System) GEO/HEO — operational missile warning, missile launch detection and tracking
  - Next-Gen OPIR — modernized, more resilient OPIR for improved sensitivity/resilience
  - SDA Tracking Layer (Tranche 0/1/2) — proliferated LEO wide-FOV IR satellites for ballistic/hypersonic tracking and custody
  - HBTSS (Hypersonic and Ballistic Tracking Space Sensor) demos — MDA prototypes for regional fire-control quality tracking of dim/fast targets
- Operational needs addressed:
  - Faster launch detection, improved tracking through boost/midcourse for hypersonic and ballistic threats
  - Cross-strata cueing (OPIR → Tracking Layer → Fire Control), reducing kill-chain latency
  - On-sensor processing to filter clutter/earthlimb backgrounds and reduce downlink bandwidth while maintaining timeliness
- Sensor payload angles:
  - Multi-band MWIR/LWIR staring/scanning sensors; at-sensor background suppression and track-before-detect algorithms
  - Dynamic thresholding and on-orbit reconfigurable detection pipelines (software-defined)

References: SSC SBIRS and Space Sensing fact sheets; SDA releases; MDA/SDA HBTSS launch announcements; GAO reports.

---

## 3) Cislunar SDA and XGEO Custody (AFRL Oracle / CHPS Heritage)
- Mission drivers: Extend SDA beyond GEO into cislunar; competition–contest–conflict continuum
- Real missions:
  - AFRL Oracle (formerly CHPS) — cislunar SDA pathfinder aimed at detecting/characterizing objects in the Earth–Moon region; addresses unfamiliar backgrounds and sparse geometry
- Operational needs addressed:
  - Detect and maintain custody of objects operating beyond GEO where ground-based tracking is sparse
  - Onboard discrimination (targets vs. background, high phase angles) due to long latencies/sparse comm windows
- Sensor payload angles:
  - Optical/IR sensors optimized for dim, slow-moving targets; adaptive exposure stacking and transient rejection
  - Onboard catalog augmentation and confidence scoring to prioritize downlink events

References: Breaking Defense coverage on Oracle; Air & Space Forces reporting; broader cislunar SDA workshop materials.

---

## 4) Proximity Operations Safety and Threat Characterization (RPO/RSO)
- Mission drivers: Defensive Space Control, SDA, Safety of Flight
- Real missions:
  - ANGELS (AF Research Laboratory / AFSPC experiment, GEO vicinity) — demonstrated RPO sensors/techniques to characterize nearby objects and validate safe operations
  - GSSAP also supports RPO awareness in GEO regimes
- Operational needs addressed:
  - Onboard relative navigation, pose/attitude estimation, and collision-avoidance assessments during proximity events
  - Continuous change/maneuver detection and intent attribution for nearby Resident Space Objects (RSOs)
- Sensor payload angles:
  - Multi-modal sensing: optical/IR + LIDAR (where applicable) for relative range/pose; passive RF to detect emissions/health
  - On-sensor MPC/planner hooks for autonomous keep-out zones and safe hold behavior

References: NASA/USAF open literature on RPO/ANGELS context; AMOS technical papers on GEO RPO detectability.

---

## 5) Space-Based RF Interference/Jamming Detection and Geolocation (Commercial + Government)
- Mission drivers: Protect PNT, SATCOM, and tactical links; support electronic protection and attribution
- Real-world precedent:
  - HawkEye 360 commercial clusters mapped GPS interference in/around Ukraine (2022–2024), informing coalition situational awareness
  - NRO engagement with commercial RF geolocation providers for operational products
- Operational needs addressed:
  - Rapid detection and geolocation of GPS jamming/spoofing and SATCOM interference affecting theater operations
  - Cross-cueing OPIR/EO sensors and terrestrial EW assets to shorten the Find–Fix–Finish timeline
- Sensor payload angles:
  - Passive multi-channel RF payloads with time/frequency difference-of-arrival (TDOA/FDOA) geolocation; waveform classification at the edge
  - Software-defined radio front-ends to reconfigure bands/missions dynamically

References: Air & Space Forces Magazine; Breaking Defense; HawkEye 360 releases; academic/EW trade press.

---

## 6) Catalog Augmentation and Conjunction Risk Reduction (Sensor–Radar Fusion)
- Mission drivers: SDA, Battle Management/C2, Safety of Flight
- Real systems:
  - Space Fence (S-band ground radar) — IOC 2020, detects/track small LEO objects; fuses with space-based observations for custody and conjunction assessment
- Operational needs addressed:
  - Reduce ephemeris uncertainty, improve conjunction screening fidelity, and enable timely collision avoidance advisories
  - Prioritize sensor tasking to fill observation gaps and maintain continuous custody
- Sensor payload angles:
  - On-sensor astrometric extraction and preliminary orbit determination to send compact tracks rather than raw imagery
  - AI-driven tasking suggestions (tip-and-cue) to ground radar networks and other space-based sensors

References: DOT&E Space Fence reports; Lockheed Space Fence materials; AMOS technical papers.

---

## 7) On-Orbit Change Detection and Attribution of Adversary Actions
- Mission drivers: Space Control, Indications & Warning, Attribution
- Real missions and doctrine:
  - USSF “Space Warfighting – A Framework for Planners” highlights attribution, persistent SDA, and rapid decision timelines
  - Reporting on satellite-on-satellite interference preparation underscores need for onboard autonomy and reduced human-in-the-loop delay
- Operational needs addressed:
  - Detect solar array/articulation changes, payload deployments, or unusual station-keeping indicative of hostile preparation
  - Provide onboard, low-latency alerts and confidence scores even under degraded comms
- Sensor payload angles:
  - Multi-spectral optical/IR with on-sensor change detection (temporal differencing, feature tracking)
  - Passive RF to correlate emissions changes with physical observations (sensor fusion for attribution)

References: USSF doctrinal framework (2025); Economist reporting.

---

## Alignment to AIS Sensors Subtopic
- Integrated sensor + edge-compute packages for persistent custody and attribution across GEO/XGEO/cislunar
- Multi-modal fusion (optical/IR/RF/LIDAR) with software-defined/reconfigurable payload behavior
- On-sensor AI/ML to cut kill-chain latency (>50%) and operator workload (>25%), enabling autonomy in contested/degraded links
- Support for USSF mission areas: SDA; Space Control; Battle Management/C2; Missile Warning/Tracking

---

## Selected References (authoritative & open sources)
- GSSAP Fact Sheet (USSF): https://www.spaceforce.mil/About-Us/Fact-Sheets/Article/2197772/geosynchronous-space-situational-awareness-program/
- Silent Barker/NROL-107 (NRO/USSF): https://www.nro.gov/news-media-featured-stories/news-media-archive/News-Article/Article/3512996/silentbarkernrol-107-press-conference/
- SBIRS/Space Sensing (USSF/SSC): https://www.ssc.spaceforce.mil/Portals/3/FACT%20SHEETS%202024/SSC_Fact_Sheet_SN_Oct_2024_b.pdf
- SDA Tracking Layer overview: https://www.sda.mil/how-the-sdas-satellite-swarm-will-track-hypersonic-missiles-where-others-cant/
- HBTSS launches (DoD/Navy): https://www.war.gov/News/Releases/Release/Article/3676902/
- AFRL Oracle (CHPS heritage) coverage: https://breakingdefense.com/2022/11/oracles-vision-understanding-cislunar-satellite-images-poses-afrls-biggest-challenge/
- ANGELS/RPO context (AMOS/NASA docs): https://amostech.com/TechnicalPapers/2021/Conjunction-RPO/George.pdf
- Space Fence (DOT&E): https://www.dote.osd.mil/Portals/97/pub/reports/FY2020/af/2020spacefence.pdf

Supporting AIS references already summarized in AIS/ref_summaries.md:
- USSF Space Warfighting Framework (2025)
- RAND AI/ML for SDA (RRA2318-1)
- IEEE Aerospace RPOD MPC paper (10115983)
- NASA “Current Technology in Space v4” (2024)
- Lockheed “AI/ML Mission Processing Onboard Satellites” (2022)

