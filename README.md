# DiameterCLI

DiameterCLI is a Python-based tool designed for simulating NB-IoT device communication with a Service Capability Exposure Function (SCEF) via the Diameter protocol over SCTP transport.
This application is especially useful for testing and debugging SCEF configurations without involving physical IoT devices.

## Features

* Automatic establishment and management of Diameter connections.

* Supports CER/CEA and DWR/DWA heartbeat exchange.

* Manual sending of:
    * Connection Management Requests (CMR);
    * Non-IP Data transmission (MO-Data);
    * Session termination with DPR.

* Terminal-based user interface for simple interaction.

## Architecture
```bash
.
├── diameterServer.py      # Handles SCTP transport and Diameter message exchange.
├── diameterCLI.py         # Terminal interface for sending test messages.
├── diaMessages.py         # Builds Diameter messages (CMR, MO-Data, DPR, etc.).
└── requirements.txt       # Python dependencies.
```
The project uses a virtual Python environment and is built on top of the pyDiameter library.
The library was extended to include custom AVPs such as Connection-Action and Non-IP-Data, allowing correct interaction with SCEF for NB-IoT scenarios.

## Requirements

* Python 3.10+

* SCTP support (libsctp-dev on Linux).

* Installed dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run ```diameterCLI.py``` for interactive console control:
```bash
==============================
      DiameterCLI
==============================

1. Send Connection-Management Request
2. Send Non-IP Data
3. Terminate Connection

Select an option:
```
Each sent and received message is logged to the console. You can also use Wireshark to capture and analyze the full Diameter exchange.

## Future Roadmap
* Support for MT-Data transmission.

* Support for Tracking Area Update (TAU) procedures.

* Simulation of energy-saving modes: eDRX and PSM.


