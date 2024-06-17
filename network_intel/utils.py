import ipaddress

def get_unique_ips(connections):
    print("Getting unique IPs...")
    unique_ips = list(set([conn[0] for conn in connections]))
    print(f"Found {len(unique_ips)} unique IPs.")
    print("\n===================\n")
    return unique_ips

def is_public_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return not ip_obj.is_private
    except ValueError:
        return False
