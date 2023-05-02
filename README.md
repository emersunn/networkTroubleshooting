# Network Troubleshooting Script

This Python script helps diagnose and troubleshoot network issues, such as DNS resolution problems, slow network speeds, or firewall issues. The script runs a series of tests and generates a report that helps pinpoint the source of the problem. The generated report is saved as a Markdown file on the user's Desktop.

## Features

- Ping test
- DNS resolution test
- Speed test (download and upload)
- Firewall test (10 most used ports)

## Requirements

- Python 3.6 or higher
- [speedtest-cli](https://github.com/sivel/speedtest-cli) library

## Installation

1. Clone the repository or download the `network_troubleshooting.py` script.
2. Install the required `speedtest-cli` library:

```pip install speedtest-cli```

## Customization

(Optional) You can customize the following variables in the script:

- host: Default IP address for the ping test (default: "8.8.8.8")
- domain: Default domain for the DNS resolution test (default: "www.google.com")
- ports: List of ports to test in the firewall test (default: (21, 22, 23, 25, 53, 80, 110, 443, 445, 3389))

To customize these variables, simply edit their values in the ```network_troubleshooting.py``` script before running it.

## Usage

Run the script from the command line:

```python network_troubleshooting.py```

The script will prompt you to enter an IP address for the ping test and a domain for the DNS resolution test. If you don't provide any input and press enter, the default values will be used (8.8.8.8 for IP address and www.google.com for domain).

After running the tests, the script will display the report in the console and save it as a Markdown file on your Desktop (```network_troubleshooting_report.md```).



