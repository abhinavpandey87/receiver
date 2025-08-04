#!/usr/bin/env python3
import socket
import threading
import logging

def handle_client(conn, addr):
    """Receive messages from a client and echo them back."""
    logging.info(f"Connection from {addr!r}")
    while True:
        data = conn.recv(4096)
        if not data:
            break
        text = data.decode(errors="ignore").rstrip()
        logging.info(f"Received: {text}")
        response = f"Echo: {text}".encode()
        conn.sendall(response)
    conn.close()
    logging.info(f"Disconnected {addr!r}")

def start_server(host="0.0.0.0", port=5000):
    """Listen for incoming connections and spawn handlers."""
    logging.basicConfig(format="%(asctime)s [SERVER] %(message)s", level=logging.INFO)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        logging.info(f"Listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()

if __name__ == "__main__":
    start_server()







<! Listens on TCP port 5000.

Logs all incoming messages and echoes them back.

Uses a thread per client.>