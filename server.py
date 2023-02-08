#!/usr/bin/env python3

import socket

s = socket.socket()
s.bind(("0.0.0.0", 8080))
s.listen(10) # queue depth, a required param set to an arbitrary value of 10

# wait for a connection
conn, address = s.accept()
print(str(conn.recv(4096)))
# conn.send ...