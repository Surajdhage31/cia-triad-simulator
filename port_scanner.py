import socket

# Target host (we will scan localhost / your own Kali machine for safety)
target = "127.0.0.1"

print(f"Scanning target: {target}")

# Let's scan a few common ports (e.g., 21 for FTP, 22 for SSH, 80 for HTTP)
ports_to_scan = [21, 22, 80, 443, 8080]

for port in ports_to_scan:
    # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout so the script doesn't hang forever if a port is closed
    s.settimeout(1.0)
    
    # Try to connect to the target IP and port
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")
        
    # Close the socket connection
    s.close()
