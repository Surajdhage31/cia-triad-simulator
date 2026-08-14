import socket
import datetime

# Define the local IP and a high-numbered port to act as our "fake" service (honeypot)
HOST = "127.0.0.1"
PORT = 2222  # Mimicking an alternative SSH or custom service port

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow reuse of the address so we don't get "Address already in use" errors if restarted quickly
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to our local host and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections (max 1 queued connection)
server_socket.listen(1)
print(f"[*] Honeypot active! Listening for unauthorized connections on {HOST}:{PORT}...")

try:
    while True:
        # Accept an incoming connection
        client_socket, client_address = server_socket.accept()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"\n[!] ALERT: Connection attempt detected!")
        print(f"[!] Timestamp: {current_time}")
        print(f"[!] Attacker IP & Port: {client_address[0]}:{client_address[1]}") 
         # Send a fake banner/warning message back to whoever connected
        banner = b"Unauthorized access is monitored and logged.\n"
        client_socket.sendall(banner)
        
        # Close the connection with them
        client_socket.close()

except KeyboardInterrupt:
    print("\n[*] Shutting down honeypot.")
    server_socket.close()
        
 
