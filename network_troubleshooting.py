import os
import socket
import speedtest

# Function to get user input with a default value
def get_user_input(prompt, default_value):
    user_input = input(f"{prompt} (Press enter for default: {default_value}): ")
    return user_input.strip() or default_value

# Function to perform a ping test on the given host
def ping_test(host="8.8.8.8"):
    response = os.system("ping -c 1 " + host)
    return response == 0

# Function to test DNS resolution for a given domain
def dns_resolution_test(domain="www.google.com"):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False

# Function to perform a speed test and return download and upload speeds
def speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    return download_speed, upload_speed

# Function to test connectivity to a specific port
def port_test(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        sock.connect(("8.8.8.8", port))
        return True
    except socket.error:
        return False

# Function to perform a firewall test on a list of ports
def firewall_test(ports=(21, 22, 23, 25, 53, 80, 110, 443, 445, 3389)):
    results = {}
    for port in ports:
        results[port] = port_test(port)
    return results

# Function to generate a report based on the results of the tests
def generate_report(ip_address, domain):
    report = "# Network Troubleshooting Report\n\n"
    
    ping_result = ping_test(ip_address)
    report += f"**Ping Test ({ip_address})**: {'Pass' if ping_result else 'Fail'}\n\n"

    dns_result = dns_resolution_test(domain)
    report += f"**DNS Resolution Test ({domain})**: {'Pass' if dns_result else 'Fail'}\n\n"

    download_speed, upload_speed = speed_test()
    report += f"**Download Speed**: {download_speed:.2f} Mbps\n\n"
    report += f"**Upload Speed**: {upload_speed:.2f} Mbps\n\n"

    firewall_results = firewall_test()
    report += "## Firewall Test:\n\n"
    for port, result in firewall_results.items():
        report += f"- Port {port}: {'Open' if result else 'Closed'}\n"
    
    return report

# Function to save the generated report to a file
def save_report(report, filename):
    with open(filename, 'w') as file:
        file.write(report)

if __name__ == "__main__":
    # Prompt the user for an IP address and domain
    ip_address = get_user_input("Enter an IP address for the Ping Test", "8.8.8.8")
    domain = get_user_input("Enter a domain for the DNS Resolution Test", "www.google.com")

    # Run the tests and generate the report
    print("Running network troubleshooting tests...")
    report = generate_report(ip_address, domain)
    print(report)
    
        # Save the report to a file on the user's Desktop
    desktop_path = os.path.expanduser("~/Desktop")
    report_filename = os.path.join(desktop_path, "network_troubleshooting_report.md")
    save_report(report, report_filename)
    print(f"Report saved as {report_filename}")
    
