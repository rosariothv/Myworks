import http.client

host = input("Host/IP: ").strip()
port = int(input("Porta (default 80): ") or 80)
path = input("Path (es. /): ").strip() or "/"

metodi = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS"]

for m in metodi:
    try:
        c = http.client.HTTPConnection(host, port, timeout=5)
        c.request(m, path)
        r = c.getresponse()
        ok = r.status not in (405, 501)
        print(f"{m}: {'ABILITATO' if ok else 'NON ABILITATO'} (status {r.status})")
        c.close()
    except Exception as e:
        print(f"{m}: errore ({e})")