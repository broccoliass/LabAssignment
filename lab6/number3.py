import socket
import os
from _thread import *
import math
import sys

ServerSideSocket = socket.socket()
host = ''
port = 2004
ThreadCount = 0

FORMAT = 'utf-8'

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)


# This Logarithmic function
def log(x):
    return math.log(x)
   
# This Square Root function
def sqrt(x):
    return math.sqrt(x)

# This Exponential function
def exp(x):
    return math.exp(x)


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:

        menu = ( ("\nSelect operation.\n") +
            ("\n1.Logarithmic") +
            ("\n2.Square Root") +
            ("\n3.Exponential") +
            ("\n4.Exit") ) 
        connection.send(str.encode(menu)) #send 1

        print("Waiting for client's option...")
        op = connection.recv(2048) #recv 2
        op = op.decode(FORMAT)  
        choice = str(op)
        
        if choice in ('1', '2', '3'):

            first = "\nEnter a number: "
            connection.send(str.encode(first)) #send 3

            fnum = connection.recv(2048)
            num1 = float(fnum.decode(FORMAT))

            if choice == '1':
                myfloat = log(num1)
                mystring = "Log value:"
                ans = mystring + str(myfloat)
                connection.send(str.encode(ans))
                print("Done")

            elif choice == '2':
                myfloat = sqrt(num1)
                mystring = "The square root: "
                ans = mystring + str(myfloat)
                connection.send(str.encode(ans))
                print("Done")
            
            elif choice == '3':
                myfloat = exp(num1)
                mystring = "Exponential: "
                ans = mystring + str(myfloat)
                connection.send(str.encode(ans))      
                print("Done")        
        
        else:
            exit = 'Thank you'
            connection.send(str.encode(exit))
            print(f'[+] {address} Client Disconnected')
            sys.exit()
            

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

ServerSideSocket.close()
