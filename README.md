[![CIA Vault Security Tests](https://github.com/Surajdhage31/cia-triad-simulator/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Surajdhage31/cia-triad-simulator/actions/workflows/python-tests.yml)

this is result of this cia tied simulation
<img width="1612" height="264" alt="image" src="https://github.com/user-attachments/assets/d97b91f6-680d-494e-9ec2-0ed9f2114c8d" />

**Log Parser** (log_parser.py)
A lightweight Python script designed for security analysts to quickly parse system logs, identify malicious behavior, and flag potential cyber threats.

🚀 **Features** 

- **Automated Log Analysis:** Scans auth logs for malicious patterns.
- **Brute-Force Detection:** Flags rapid, repetitive failed login attempts.
- **IP Tracking:** Extracts and groups suspicious activity by source IP.
- **Real-Time Alerts:** Outputs formatted warnings and critical alerts to the console.

<img width="702" height="222" alt="image" src="https://github.com/user-attachments/assets/a826a972-559d-4663-bc02-f9623602da8f" />

### Honeypot in Action
<img width="578" height="117" alt="image" src="https://github.com/user-attachments/assets/8ceaf3fd-a26e-495f-9af9-3f02765516ce" />
<img width="396" height="117" alt="image" src="https://github.com/user-attachments/assets/bff0bebd-a181-4d5f-be7f-60cd709acf29" />

* **Status:** Listens on `127.0.0.1:2222` for unauthorized connection attempts.
* **Alert Logging:** Captures and displays the exact timestamp and source IP/port (`127.0.0.1:56940`) upon detection.
### Port Scanner
<img width="505" height="119" alt="image" src="https://github.com/user-attachments/assets/415932a1-d417-4f7e-9ea9-29d6c60a54b6" />

- **Targeted IP Scanning**: Scans local or specified IP addresses (127.0.0.1).
- **Common Port Checking**: Automatically checks standard service ports, including FTP (21), SSH (22), HTTP (80), HTTPS (443), and HTTP-Proxy (8080).
- **Clear Output Status**: Displays real-time port status results directly in the terminal interface.


