#FAR PARTIRE IL COMANDO CON "SUDO"

import socket

host = input("IP da monitorare (premere invio per tutti): ").strip()
port = input("Porta da filtrare (premere invio per tutte): ").strip()
port = int(port) if port else None

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
print("Sniffer avviato... Ctrl+C per terminare.\n")

while True:
    pkt, _ = s.recvfrom(65535)
    if len(pkt) < 34:  # header Ethernet (14) + header IP min (20)
        continue

    src_ip = ".".join(str(b) for b in pkt[26:30])
    dst_ip = ".".join(str(b) for b in pkt[30:34])
    proto = pkt[23]

    if host and host not in (src_ip, dst_ip):
        continue

    if proto == 6 and len(pkt) >= 54:  # 6 = TCP
        sport = int.from_bytes(pkt[34:36], 'big')
        dport = int.from_bytes(pkt[36:38], 'big')
        if port and port not in (sport, dport):
            continue
        print(f"TCP {src_ip}:{sport} → {dst_ip}:{dport}")

    elif proto == 17 and len(pkt) >= 42:  # 17 = UDP
        sport = int.from_bytes(pkt[34:36], 'big')
        dport = int.from_bytes(pkt[36:38], 'big')
        if port and port not in (sport, dport):
            continue
        print(f"UDP {src_ip}:{sport} → {dst_ip}:{dport}")