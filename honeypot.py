import socket
import logging
from datetime import datetime

def handle_client(client_socket, addr):
    print(f"[!] Connection attempt from {addr[0]}:{addr[1]}")

    # Send welcome message to client
    client_socket.send(b"Welcome to HoneySentinel!\n")

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[>] Received from {addr[0]}:{addr[1]}: {data.decode().strip()}")
            # Echo back the received data
            client_socket.send(b"You said: " + data)
    except Exception as e:
        print(f"[!] Client error: {e}")

    client_socket.close()

# Config
HOST = '0.0.0.0'  
PORT = 2222        

# Logging setup for  it
logging.basicConfig(
    filename='logs/connections.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def start_honeypot():
    print(f"[+] Honeypot listening on port {PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            print(f"[!] Connection attempt from {addr[0]}:{addr[1]}")
            logging.info(f"Connection from {addr[0]}:{addr[1]}")
            conn.close()

if __name__ == "__main__":
    try:
        start_honeypot()
    except KeyboardInterrupt:
        print("\n[!] Honeypot stopped by user.")
