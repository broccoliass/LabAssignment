import socket

host = ''
port = 4455
ADDR = (host, port)
SIZE = 1024
FORMAT = "utf-8"

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    
    print("Waiting for client")

    while True:
        conn, addr = server.accept()
        print(f"{addr} connected.")

        filename = conn.recv(SIZE).decode(FORMAT)
        file = open(filename, "w")
        conn.send("Server ready to receive the file".encode(FORMAT))

        data = conn.recv(SIZE).decode(FORMAT)
        file.write(data)
        print("File received")
        conn.send("Server received the file".encode(FORMAT))

        file.close()

        conn.close()
        print(f"{addr} disconnected.")

if __name__ == "__main__":
    main()
