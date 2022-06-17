import socket
import sys
FORMAT = "utf-8"

ClientMultiSocket = socket.socket()
host = '192.168.125.3'
port = 2004
print('Waiting for connection response')

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(2048)

while True:
    try:
        mainmenu=ClientMultiSocket.recv(2048)   #recv 1
        print(mainmenu.decode(FORMAT))

        Input = input('\nChoose mathematical function: ') #option
        ClientMultiSocket.send(str.encode(Input)) #send 2
        
        first = ClientMultiSocket.recv(2048) #recv 3
        print(first.decode(FORMAT))
        fnum = input()
        ClientMultiSocket.send(str.encode(fnum))

        if Input == '1':
            ans = ClientMultiSocket.recv(2048)
            print(ans.decode(FORMAT))

        if Input == '2':
            ans = ClientMultiSocket.recv(2048)
            print(ans.decode(FORMAT))

        if Input == '3':
            ans = ClientMultiSocket.recv(2048)
            print(ans.decode(FORMAT))            

        if Input == '4':
            exit = ClientMultiSocket.recv(2048).decode(FORMAT)
            print(exit)
            sys.exit()

    except KeyboardInterrupt:
        print('\nCtrl + C is pressed, Lost Connection')
        sys.exit()

ClientMultiSocket.close()
