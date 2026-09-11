import socket
import time

SERVER_PORT = 2003

def run_receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", SERVER_PORT))
    sessions = {}

    print("\n--- RECEIVER MODE ACTIVE ---")
    print(f"Listening for connections on port {SERVER_PORT}...")
    print("Keep this terminal open. Press Ctrl+C to stop.\n")

    while True:
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8').strip()
        
        if ":" in message:
            action, device = message.split(":", 1)
            
            if action == "LOGIN":
                sessions[device] = time.time()
                print(f"[{device}] Session started.")
                
            elif action == "LOGOUT":
                if device in sessions:
                    start_time = sessions.pop(device)
                    duration = time.time() - start_time
                    print(f"[{device}] Session ended. Duration: {duration:.2f} seconds.")