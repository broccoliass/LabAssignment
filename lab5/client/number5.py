import socket

host = '192.168.125.3'
port = 4455
ADDR = (host, port)
FORMAT = "utf-8"
SIZE = 1024

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    
    print("Connected to server")
    print("Ready to send file")

    file = open("mytext.txt", "r")
    data = file.read()

    client.send("mytext.txt".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"{msg}")

    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"{msg}")

    file.close()
    client.close()


if __name__ == "__main__":
    main()
