# SPECTRA Proposal — Acronyms and Definitions

## Technical Acronyms

| Acronym | Full Term                                            | Definition                                                                                                                                        |
| ------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWG     | Arbitrary Waveform Generator                         | Laboratory test equipment that generates synthetic RF (radio frequency) signals for bench validation and hardware-in-the-loop testing.            |
| CEP     | Circular Error Probable                              | A measure of geolocation accuracy; CEP50 is the radius within which 50% of measurements fall, CEP90 is the radius for 90%.                        |
| CCSDS   | Consultative Committee for Space Data Systems        | International standards organization that develops protocols and standards for space systems data exchange and command/control.                   |
| BM-C2   | Battle Management Command and Control                | Military standard for command, control, and coordination of space operations.                                                                     |
| ECE     | Expected Calibration Error                           | A metric for evaluating the calibration quality of uncertainty estimates in machine learning models.                                              |
| EO      | Electro-Optical                                      | Sensors that detect visible light and near-infrared radiation; includes cameras and imaging systems.                                              |
| EW      | Electronic Warfare                                   | Military operations involving detection, analysis, and response to electromagnetic threats and emissions.                                         |
| EWIRDB  | Electronic Warfare Integrated Reprogramming Database | A parametric database of threat emitter characteristics and behaviors used for synthetic scene generation.                                        |
| FPGA    | Field-Programmable Gate Array                        | Reconfigurable hardware that can be programmed to implement custom logic; used for deterministic, low-latency processing.                         |
| GEO     | Geostationary Orbit                                  | Orbital altitude (~36,000 km) where satellites remain fixed over a point on Earth's equator.                                                      |
| HIL     | Hardware-in-the-Loop                                 | Testing methodology where physical hardware is integrated with simulation software to validate system behavior.                                   |
| HPC-S   | High-Performance Computing in Space                  | Integrated sensor-compute architecture that performs data processing and analysis onboard spacecraft.                                             |
| HSI     | Hyperspectral Imaging                                | Sensors that capture imagery across many narrow spectral bands for detailed material/target identification.                                       |
| IR      | Infrared                                             | Sensors that detect thermal radiation; used for detecting heat signatures and night-time imaging.                                                 |
| LEO     | Low Earth Orbit                                      | Orbital altitude (typically 160–2,000 km) where satellites orbit relatively close to Earth.                                                       |
| M&S     | Modeling and Simulation                              | Computer-based tools and frameworks for simulating system behavior and validating designs.                                                        |
| ML      | Machine Learning                                     | Computational techniques that enable systems to learn patterns from data and make predictions or decisions.                                       |
| NGSX    | [IA's simulation framework]                          | Interactive Aptitude's sensor-agnostic simulation environment for Space Domain Awareness and Rendezvous & Proximity Operations scenarios.         |
| OmniCat | [Ground catalog system]                              | Integrated ground-based catalog system for threat and object tracking data; integration point for Phase II.                                       |
| PDW     | Pulse Descriptor Word                                | A compact data structure capturing key parameters of detected RF pulses (frequency, time, amplitude, etc.).                                       |
| PIGEON  | [COSMIAC RF heritage]                                | COSMIAC's prior RF front-end and signal processing baseline; provides foundation for Phase I RF instantiation.                                    |
| POD     | Probability of Detection                             | Metric indicating the likelihood that a sensor will detect a target or threat when present.                                                       |
| RPO     | Rendezvous and Proximity Operations                  | Space operations involving close approach, station-keeping, and coordination between spacecraft.                                                  |
| SAR     | Synthetic Aperture Radar                             | Active radar sensor that synthesizes a large antenna aperture through motion; provides high-resolution imaging regardless of weather/time of day. |
| SDA     | Space Domain Awareness                               | Operational capability to detect, track, and characterize objects and activities in space.                                                        |
| SIERO   | [Uncertainty gating method]                          | Approach for uncertainty-aware decision-making; gates autonomy decisions based on confidence thresholds.                                          |
| SoC     | System-on-Chip                                       | Integrated circuit containing processor, memory, and I/O on a single chip; compact and power-efficient.                                           |
| SOSA    | Sensor Open Systems Architecture                     | Open-standard framework for interoperable sensor systems and data integration, enabling modular and composable sensor networks.                   |
| SWaP    | Size, Weight, and Power                              | Key constraints for space systems; refers to physical footprint, mass, and power consumption budgets.                                             |
| TRL     | Technology Readiness Level                           | Scale (1–9) measuring maturity of a technology from concept to operational deployment.                                                            |
| UQ      | Uncertainty Quantification                           | Methods for estimating and communicating confidence/reliability of predictions and measurements.                                                  |
| XGEO    | Beyond Geostationary Orbit                           | Orbital altitudes beyond GEO (~36,000 km); includes highly elliptical and deep-space orbits.                                                      |

## Program/Organization Acronyms

| Acronym | Full Term                          | Definition                                                                                                                                         |
| ------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| COSMIAC | [University of New Mexico center]  | Center for Space Situational Awareness and Rapid Innovation; provides RF expertise, PIGEON heritage, and radiation testing capabilities.           |
| IA      | Interactive Aptitude               | Industry partner providing simulation, catalog, and HIL orchestration expertise.                                                                   |
| NRO     | National Reconnaissance Office     | U.S. intelligence agency responsible for space-based reconnaissance systems.                                                                       |
| SBIR    | Small Business Innovation Research | U.S. federal program funding R&D by small businesses; typically 3 phases over 2–3 years.                                                           |
| STTR    | Small Business Technology Transfer | Variant of SBIR requiring university partnership; focuses on technology transfer.                                                                  |
| UDL     | Unified Data Layer                 | Standardized interface and data format for disseminating space domain awareness observations and threat intelligence to the broader SDA community. |
| USSF    | United States Space Force          | U.S. military branch responsible for space operations and capabilities.                                                                            |

## Key Concepts

| Term                      | Definition                                                                                                                                                                                                                                          |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Modality-Agnostic**     | Architecture or design that is independent of specific sensor types; supports RF, SAR, EO, IR, HSI, etc. through plugin interfaces.                                                                                                                 |
| **Edge Processing**       | Data processing performed on the spacecraft/payload rather than transmitted to ground; reduces latency and bandwidth.                                                                                                                               |
| **Payload-in-the-Loop**   | Simulation methodology where the actual payload software/hardware is integrated into a simulation environment for validation.                                                                                                                       |
| **Red-Team Injectors**    | Simulated adversarial scenarios (e.g., jamming, spoofing, deception) used to stress-test system robustness.                                                                                                                                         |
| **Custody**               | Continuous tracking and awareness of a target's location and status; critical in contested/comms-denied environments.                                                                                                                               |
| **Comms-Denied**          | Operational scenario where communication with ground is unavailable or severely limited; requires autonomous onboard decision-making.                                                                                                               |
| **Deterministic Latency** | Guaranteed maximum time from input to output; critical for real-time threat response.                                                                                                                                                               |
| **Downlink Bundle**       | Compact package of alert, evidence, and metadata transmitted from spacecraft to ground; optimized for bandwidth constraints.                                                                                                                        |
| **Threat Descriptor**     | Parametric representation of a threat (emitter, behavior, signature); enables compact storage and cross-modal comparison.                                                                                                                           |
| **Observation**           | Raw sensor data streams, frames, collects, or measurements directly from sensors (e.g., RF pulses, radar returns, imagery frames); unprocessed or minimally processed sensor output.                                                                |
| **Event**                 | Processed output resulting from fusion, AI/ML, and analytical algorithms applied to observations; represents detected threats, behaviors, anomalies, or significant activities (e.g., threat alerts, emitter classifications, maneuver detections). |


