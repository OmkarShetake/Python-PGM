
server_ip = (192, 168, 1, 1)  
allowed_ips = ["192.168.1.10", "192.168.1.20"]

def update_allowed_ips(new_ip):
    """Add a new IP to the allowed list."""
    if new_ip not in allowed_ips:
        allowed_ips.append(new_ip)
        print(f"IP {new_ip} added to allowed list.")
    else:
        print(f"IP {new_ip} already exists in allowed list.")

def update_server_ip(new_ip):
    """Prevent updating server_ip."""
    print("Server IP cannot be changed during runtime.")

def display_config():
    """Display the current server configuration."""
    print("\nServer Configuration")
    print(f"Server IP: {'.'.join(map(str, server_ip))}")
    print("Allowed IPs:")
    for ip in allowed_ips:
        print(f" - {ip}")
    


display_config()
update_server_ip((10, 0, 0, 1))
update_allowed_ips("192.168.1.30")
update_allowed_ips("192.168.1.10")  

display_config()