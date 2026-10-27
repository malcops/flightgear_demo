import socket

UDP_IP = "0.0.0.0"  # Listen on all local interfaces inside the container
UDP_PORT = 1138

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP Receiver is online! Listening on port {UDP_PORT}...", flush=True)

try:
    while True:
        raw_data, addr = sock.recvfrom(1024)
        clean_string = raw_data.decode("utf-8").strip()
        print(f"[{addr[0]}] Received: {clean_string}", flush=True)
except KeyboardInterrupt:
    print("\nShutting down UDP receiver.")
finally:
    sock.close()

