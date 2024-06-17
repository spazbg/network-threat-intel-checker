import requests

def check_threat_intel(ips):
    print("Checking IPs against AbuseIPDB...\n")
    malicious_ips = []

    for ip in ips:
        try:
            url = f'https://api.abuseipdb.com/api/v2/check?ipAddress={ip}'
            headers = {'Key': 'API_KEY', 'Accept': 'application/json'}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                if data['data']['abuseConfidenceScore'] > 50:
                    malicious_ips.append({
                        'ipAddress': ip,
                        'countryCode': data['data']['countryCode'],
                        'domain': data['data']['domain'],
                        'usageType': data['data']['usageType'],
                        'totalReports': data['data']['totalReports']
                    })
                    print(f"\033[91m❌ IP {ip} is flagged as malicious!\033[0m")
                else:
                    print(f"\033[92m✅ IP {ip} is not flagged as malicious.\033[0m")
            else:
                print(f"Error checking IP {ip} against AbuseIPDB: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            print(f'Error checking IP {ip} against threat intelligence platform: {e}')

    print("\n===================\n")
    return malicious_ips
