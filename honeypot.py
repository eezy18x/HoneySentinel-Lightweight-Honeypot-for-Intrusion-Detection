import socket

HOST = '0.0.0.0'
PORT = 2222

def start_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Honeypot listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            print(f"[!] Connection attempt from {addr[0]}:{addr[1]}")
            with conn:
                try:
                    # Send the banner once at the start
                    conn.sendall(b"Fake SSH Banner: SSH-2.0-OpenSSH_7.9p1\r\n")

                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        # Print received input without extra banner
                        print(f"[>] Received from {addr[0]}: {data.decode(errors='ignore').strip()}")

                except Exception as e:
                    print(f"[!] Error handling connection: {e}")

if __name__ == "__main__":
    start_honeypot()
