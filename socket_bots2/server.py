import socket
import threading

list_of_connections = []

if __name__ == '__main__':
    main()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #establishing what type of protocol is going to be used
                                                                # AF_INET is the TCP protocol
    server.bind((socket.gethostname(), 1234))                   #establishing a server on the ip adress with port 1234
    server.listen(5)                                            #listening for connection for max 5 clients

    while True:
        client, addr = server.accept()                          #if server find a client it will establish a three way
                                                                #handshake and establising a connetion
        list_of_connections.append(client)
        print()
