import socket
import tkinter as tk

SERVER_PORT = 2003

def run_sender():
    device_name = socket.gethostname()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    is_logged_in = False

    def toggle_session():
        nonlocal is_logged_in
        
        if not is_logged_in:
            msg = f"LOGIN:{device_name}"
            sock.sendto(msg.encode('utf-8'), ("<broadcast>", SERVER_PORT))
            button.config(text="End Session (LOGOUT)", bg="red", fg="white")
            label.config(text="Session is ACTIVE")
            is_logged_in = True
        else:
            msg = f"LOGOUT:{device_name}"
            sock.sendto(msg.encode('utf-8'), ("<broadcast>", SERVER_PORT))
            button.config(text="Start Session (LOGIN)", bg="green", fg="black")
            label.config(text="Session is INACTIVE")
            is_logged_in = False

    # Build the Sender's window
    window = tk.Tk()
    window.title(f"Sender: {device_name}")
    window.geometry("300x150")

    label = tk.Label(window, text="Session is INACTIVE", font=("Arial", 12))
    label.pack(pady=15)

    button = tk.Button(window, text="Start Session (LOGIN)", font=("Arial", 14), bg="green", fg="black", command=toggle_session)
    button.pack(pady=10)

    window.mainloop()