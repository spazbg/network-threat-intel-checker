import psutil
import subprocess

def get_active_connections():
    print("\n===================\n")
    print("Getting active connections...")
    connections = psutil.net_connections()
    active_connections = [(conn.raddr.ip, conn.raddr.port) for conn in connections if conn.raddr]
    print(f"Found {len(active_connections)} active connections.")
    print("\n===================\n")
    return active_connections

def get_past_connections():
    print("Getting past connections...")
    connections = []

    try:
        journal_cmd = "journalctl | grep -oE '\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b'"
        result = subprocess.run(journal_cmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            output = result.stdout
            for line in output.splitlines():
                ip = line.strip()
                connections.append((ip, 0))  # Assuming port 0 for simplicity
            print(f"Found {len(connections)} past connections in the systemd journal.")
        else:
            print(f"Error retrieving past connections: {result.stderr}")

    except subprocess.CalledProcessError as e:
        print(f"Error retrieving past connections: {e}")

    print("\n===================\n")
    return connections
