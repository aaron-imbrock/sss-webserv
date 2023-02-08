#!/usr/bin/env python3

import socket

PORT = 80
FQDN = "sizza.net"

def get_ip(url_str):
    return socket.gethostbyname(url_str)

def generate_http_get(fqdn, route='/'):
    return f"GET {route} HTTP/1.1\r\nHost: {fqdn}\r\n\r\n".encode()

# def generate_http_post(fqdn, route='/', data=None):
#     if data is None:
#         data = {}
#     data = "&".join([f"{k}={v}" for k, v in data.items()])
#     return f"POST {route} HTTP/1.1\r\nHost: {fqdn}\r\nContent-Length: {len(data)}\r\n\r\n{data}".encode()

if '__main__' == __name__:
    IP = get_ip(FQDN)
    s = socket.socket()
    s.connect((IP, PORT))  # tuple
    s.send(generate_http_get(FQDN, route='/'))
    print(str(s.recv(4096)))