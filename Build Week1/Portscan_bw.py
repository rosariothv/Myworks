import socket

host = input("host/IP: ").strip()
pr = input("inserisci range usando '-' (es. 20-80): ").strip()

if host == "":
    print("inserisci un indirizzo IP corretto")
    raise SystemExit(1)

try:
    low, high = map(int, pr.split("-"))
except Exception:
    print("Range non valido")
    raise SystemExit(1)
if high < low:
    low, high = high, low

try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Inserito un indirizzo IP errato")
    raise SystemExit(1)
except Exception:
    ip = host

for port in range(low, high + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    ok = s.connect_ex((ip, port)) == 0
    print(f"{port}: {'OPEN' if ok else 'CLOSED'}")
    s.close()


