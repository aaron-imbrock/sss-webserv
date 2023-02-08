import http.client

PORT = 80
FQDN = "ip.me"

def get_external_ip(fqdn=FQDN, port=PORT):
    conn = http.client.HTTPConnection(FQDN, PORT)
    payload = ''
    headers = {}
    conn.request("GET", "/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8").strip()