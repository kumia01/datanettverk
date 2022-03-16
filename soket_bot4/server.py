import socket
import select

# list of clients connected to the Server
list_of_connections = []
list_names = []

# How many clients that can connect to the server
max_client = 4

print("[starting] server is starting")
print(f"ip address: 192.168.39.137")
# creating socket object with TCP protocol and
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# we bind the port so that server listen to request coming from other computers on the network
server.bind(("192.168.39.137", 1234))

# listening for connection for max 5 clients
server.listen(max_client)
print(f"[listening] Server is listening")


# function for kicking certain clients and closing off connetions from both end
def kick(msg):
    for names in list_names:
        if names in msg:
            client = list_of_connections[list_names.index(names)]
            client.send("kicked".encode())
            msg = client.recv(1024).decode()
            broadcast(client, msg)
            client.close()
            remove(client)


def connections():
    # if server find a client it will establish a three-way
    # handshake and establishing a connection
    client, addr = server.accept()
    # adding connected client to a list
    # name = client.recv(1024).decode()
    # list_names.append(name)
    list_of_connections.append(client)
    num_connections = len(list_of_connections) - 1
    print(f"new connection established: {client}")
    print(f"numbers of connections: {num_connections}")


def broadcast(client, msg):
    for clients in list_of_connections:
        if clients != server and clients != client:
            try:
                clients.send(msg.encode())
            except:
                # if the socket connection is broken, we close it off
                client.close()
                remove(client)


def remove(client):
    if client in list_of_connections:
        list_of_connections.remove(client)
    num_connections = len(list_of_connections) - 1
    print(f"numbers of connections: {num_connections}")


def main():
    list_of_connections.append(server)

    while True:
        # here we get the list of socket that is ready for read through select
        read_sockets, write_sockets, error_sockets = select.select(list_of_connections, [], [])
        for sock in read_sockets:
            # a new connection established
            if sock == server:
                connections()
            else:
                try:
                    msg = sock.recv(1024).decode()

                    if "/kick" in msg:
                        kick(msg)
                    if msg:
                        broadcast(sock, "\n" + msg)
                except:
                    remove(sock)
                    continue


if __name__ == '__main__':
    main()
