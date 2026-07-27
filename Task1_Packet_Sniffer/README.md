# Network Packet Sniffer

## Objective
This project is developed as part of the CODSOFT Cyber Security Internship.

The application captures network packets using Python and Scapy and displays important information such as:
- Source IP Address
- Destination IP Address
- Protocol Type (TCP, UDP, ICMP)
- Packet Summary
- Packet Payload (if available)

## Technologies Used
- Python
- Scapy

## Installation

1. Install Python.
2. Install Scapy:

```bash
pip install scapy
```

## Run the Program

```bash
python packet_sniffer.py
```

## Sample Output

```
======================================================================
Source IP      : 192.168.1.5
Destination IP : 142.250.182.14
Protocol       : TCP
Packet Summary : IP / TCP 192.168.1.5:52142 > google.com:https
```

## Screenshots

Add your screenshots inside the `screenshots` folder.

## Author
Nivetha