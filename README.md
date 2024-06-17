# Network Threat Intelligence Checker

This is an application package library that gathers network connection information and checks the unique public IPs
against a threat intelligence platform (AbuseIPDB) to identify potentially malicious IPs.

## Features

- Retrieves active network connections using `psutil`
- Retrieves past network connections from the systemd journal (Linux only)
- Extracts unique public IPs from the collected network connections
- Checks the unique public IPs against the AbuseIPDB threat intelligence platform
- Provides a summary of the results, including the number of potentially malicious IPs found

## Requirements

- Python 3.x
- `psutil` library
- `requests` library

## Installation

1. Clone the repo
2. Install the required dependencies

```bash
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```bash
python -m network_intel.app
```

The application will gather network connection information, check the unique public IPs against AbuseIPDB, and provide a
summary of the results.

## Configuration

- The application uses the AbuseIPDB API for threat intelligence. Make sure to replace the `API_KEY` variable in
  the `threat_intel.py` file with your own AbuseIPDB API key.
- To run this application properly, user must have read access to the systemd journal logs. If you encounter
  permission issues, add your user to the systemd-journal group using `sudo usermod -aG systemd-journal $USER`, then log
  out and log back in for the changes to take effect, or use `newgrp systemd-journal` to switch to the group in the
  current shell session.