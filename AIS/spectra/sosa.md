## Sensor Open Systems Architecture (SOSA) — Overview

Last updated: 2025-10-16

### Executive summary
- The Sensor Open Systems Architecture (SOSA) is a standards-based, modular, and open systems approach for defense sensor platforms (radar, EW, EO/IR, SIGINT, C4ISR). It defines a common, vendor-neutral framework so that plug-in hardware and software components can be rapidly integrated, upgraded, and replaced.
- SOSA is developed by The Open Group SOSA Consortium and aligns with the DoD’s Modular Open Systems Approach (MOSA). It leverages existing open standards (especially VITA/OpenVPX for hardware) and focuses on well-defined interfaces, profiles, and data/management standards to ensure interoperability and competition.[1][2]

### Governance and scope
- Stewardship: The Open Group SOSA Consortium (government, industry, and academia).[1]
- Artifacts: SOSA Technical Standard (TS), SOSA Reference Architecture, Business/Acquisition guidance, and a developing Conformance Program.[1][3]
- Intent: Drive multi-vendor interoperability at module, card, backplane, chassis, and system levels; shorten upgrade cycles; reduce lifecycle cost; and avoid vendor lock-in.

### Relationship to MOSA, CMOSS, and related standards
- MOSA: SOSA is a concrete realization of MOSA goals for sensor systems (well-defined interfaces, open standards, and separable modules).[3]
- CMOSS (C5ISR/EW Modular Open Suite of Standards): SOSA and CMOSS are closely aligned. CMOSS defines an Army suite incorporating VICTORY (vehicle data buses), MORA (radio architecture, often with VITA 49 VRT), and OpenVPX hardware elements; SOSA provides detailed slot/module profiles and implementation guidance widely adopted across services.[4][5]
- FACE/OMS-UCI: SOSA is complementary. FACE focuses on avionics software portability, while OMS/UCI address mission system interoperability/data models. SOSA’s emphasis is on module-level hardware/software interfaces and integration patterns; programs may use SOSA alongside FACE or OMS/UCI depending on platform needs.[1]

### Technical building blocks
- Hardware form factor and backplanes
  - OpenVPX (VITA 65.x) is the primary hardware foundation. SOSA defines a curated set of OpenVPX-based slot/profile definitions (for SBCs, switches, payload, I/O, timing, and power) to ensure interoperability across vendors.[2]
  - Common related VITA standards: VITA 46 (VPX connectors), VITA 65 (OpenVPX profiles), VITA 48 (cooling), VITA 62 (power supplies), VITA 66 (optical I/O), VITA 67 (RF coax/RFSoC I/O), VITA 46.11 (system management/IPMC).[2]
- Data, control, and I/O
  - High-speed fabrics: Ethernet (including 10/40/100G), PCIe, and SERDES links; SOSA profiles constrain which options and topologies are used.
  - Waveform/data transport: VITA 49.2 VRT is commonly used for digitized RF transport; SOSA aligns with its use in relevant payloads (e.g., EW/SIGINT/RF sensors).[4]
  - Middleware-neutral: SOSA does not mandate a single app framework; it focuses on interface profiles so integrators can adopt appropriate middleware or data models (e.g., use FACE/OMS/UCI where applicable).
- Timing and synchronization
  - Distribution of precise time/clock references across the backplane and chassis (e.g., 1PPS, 10 MHz, PTP/IEEE 1588 profiles as applicable) and defined timing slot profiles to support coherent sensing/beamforming.
- System management and security
  - VPX management per VITA 46.11; chassis and module management for health/status, inventory, and control. Programs layer platform-specific cyber and safety requirements on top of SOSA profiles.

### Conformance and procurement
- Conformance Program: The SOSA Consortium is establishing a formal conformance program, including profiles, verification matrices, and guidance to verify modules/backplanes/chassis against SOSA-defined sets.[3]
- “SOSA-aligned” vs “SOSA-conformant”: Vendors often say “SOSA-aligned” to indicate design intent. “SOSA-conformant” implies meeting the formal conformance criteria once available (profile adherence, test artifacts, and verification evidence). Prefer conformance claims tied to The Open Group program and specific profile IDs.
- Acquisition: The Open Group provides business and acquisition guidance to help RFPs/RFIs specify SOSA-relevant requirements (e.g., mandated slot profiles, interfaces, and conformance evidence).[1][3]

### Versions and maturity
- SOSA Technical Standard 1.0 was the first formal release. Subsequent updates (e.g., 1.1) refine slot profiles, clarify requirements, and expand verification artifacts.[2][3]
- A SOSA Reference Architecture and Business Guide complement the TS. Many vendors and programs now publish “SOSA-aligned” 3U/6U OpenVPX modules, backplanes, timing cards, and chassis.[2][4]

### Benefits and trade-offs
- Benefits: Faster tech insertion and upgrades, broader supplier base, reduced integration risk through standardized profiles, better reuse across platforms and services.
- Trade-offs: Constraining profiles can limit exotic configurations; careful profile selection is needed for specialized performance (e.g., extreme bandwidth or unique RF I/O). Early lifecycle programs may need to track evolving conformance processes.

### Relevance to AIS/spectra work
- For RF/EW/SIGINT sensor payloads, SOSA’s curated OpenVPX slot profiles, VITA 49.2 transport, and timing distribution simplify multi-vendor integration of digitizers, FPGA/GPU accelerators, SBCs, and RF front-ends, enabling incremental capability insertion and rapid field upgrades.

### Key references (authoritative/public)
1) The Open Group SOSA Consortium overview: https://www.opengroup.org/sosa
2) Industry overview of SOSA and OpenVPX profiles (example vendor explainer): https://www.mrcy.com/innovation/capabilities/open-systems-architecture/sensor-open-systems-architecture-sosa and https://www.curtisswrightds.com/capabilities/open-architectures/mosa/sensor-open-systems-architecture
3) The Open Group SOSA working groups and conformance charter: https://www.opengroup.org/sosa/workinggroups and related SOSA resources
4) Army CMOSS background (relationship to VICTORY/MORA/OpenVPX): https://imlive.s3.amazonaws.com/Federal+Government/ID24026939598971879947296347642211598029/CMOSS-Overview-18Mar22-Dist-A-A758.pdf
5) Context on SOSA/CMOSS adoption and slot/backplane alignment: https://www.jedonline.com/2023/12/10/from-the-jed-archives-army-sosa-cmoss-standards-deliver-interoperable-and-upgradeable-systems-today/
