#!/usr/bin/env python3

import socket

# create a socket object of address type IPv4 and TCP (defaults)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8080))
s.listen(10) # queue depth, a required param set to an arbitrary value of 10

http_response = b"""HTTP/1.1 200 OK\r
CONTENT-Length: 8\r

HOLA!\n\r\n"""

while True:
    # wait for a connection
    clientsocket, address = s.accept()
    print(f"Connection from {address}")
    clientsocket.send(http_response)
    clientsocket.shutdown(socket.SHUT_WR)
    clientsocket.close()

s.close()
# conn.send ...