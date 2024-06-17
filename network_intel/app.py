from .network import get_active_connections, get_past_connections
from .threat_intel import check_threat_intel
from .utils import get_unique_ips, is_public_ip

def main():
    active_connections = get_active_connections()
    past_connections = get_past_connections()
    all_connections = active_connections + past_connections

    unique_ips = get_unique_ips(all_connections)
    
    public_ips = []
    private_ips = []

    for ip in unique_ips:
        if is_public_ip(ip):
            public_ips.append(ip)
        else:
            private_ips.append(ip)

    print("Sorting IPs...")
    print(f"{len(public_ips)} are public and {len(private_ips)} are private.")
    print("\n===================\n")

    malicious_ips = check_threat_intel(public_ips)

    print("\nSummary:")
    print(f"Checked {len(public_ips)} unique public IPs.\n")
    print(f"\033[91mFound {len(malicious_ips)} potentially malicious IPs:\033[0m")
    for ip_info in malicious_ips:
        print(f"- IP: {ip_info['ipAddress']}")
        print(f"  Country: {ip_info['countryCode']}")
        print(f"  Domain: {ip_info['domain']}")
        print(f"  Usage Type: {ip_info['usageType']}")
        print(f"  Total Reports: {ip_info['totalReports']}")
        print()

if __name__ == "__main__":
    main()
