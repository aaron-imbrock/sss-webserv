#!/usr/bin/env python3

import signal, socket

from modules.get_external_ip import get_external_ip

EXTERNAL_IP = get_external_ip()
PORT = 8080
FQDN = "sizza.net"

# If ctrl-c is pressed, exit gracefully
signal.signal(signal.SIGINT, signal_handler)

# create a socket object of address type IPv4 and TCP (defaults)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8080))
s.listen(10) # queue depth, a required param set to an arbitrary value of 10

http_response = b"""HTTP/1.1 200 OK\r
CONTENT-Length: 6\r

HOLA!\n\r\n"""

def signal_handler(signal, frame):
    print("Ctrl-c was pressed. Exiting... ")
    socket_clean_up()
    exit(0)

def socket_clean_up():
    s.close()

print(f"Listening on {EXTERNAL_IP}:{PORT}... (Ctrl-C to exit)")

while True:
    # wait for a connection
    clientsocket, address = s.accept()
    print(f"Connection from {address}")
    clientsocket.send(http_response)
    clientsocket.shutdown(socket.SHUT_WR)
    clientsocket.close()

# conn.send ...