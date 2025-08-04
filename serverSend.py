#!/usr/bin/env python3
import socket
import sys

def send_message(host: str, port: int, message: str):
    """Connect to host:port, send message, receive reply."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(message.encode())
        response = sock.recv(4096)
        return response.decode(errors="ignore")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <host> <port> <message>")
        sys.exit(1)
    host, port_str, message = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        port = int(port_str)
    except ValueError:
        print("Invalid port number.")
        sys.exit(1)
    reply = send_message(host, port, message)
    print("Server replied:", reply)
