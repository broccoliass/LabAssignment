import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = 8888
s.connect(('192.168.125.3', port))
data = s.recvfrom(1024)
s.sendto(b"Hi, saya client Terima kasih!");
print (data)
s.close()
