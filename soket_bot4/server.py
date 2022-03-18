import socket
import select
import time

# list of clients connected to the Server
list_of_connections = []
list_names = []

# How many clients that can connect to the server
max_client = 5

print("[starting] server is starting")
print(f"ip address: 192.168.39.137")
# creating socket object with TCP protocol and
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# we bind the port so that server listen to request coming from other computers on the network
server.bind(("192.168.39.137", 1234))

# listening for connection for max 5 clients
server.listen(max_client)
print(f"[listening] Server is listening")


# function for kicking certain clients and closing off connections from both end
def kick(msg):
    for names in list_names:
        if names in msg:
            client = list_of_connections[list_names.index(names) + 1]
            client.close()
            print(client)
            remove(client)
            num_connections = len(list_of_connections) - 1
            broadcast(server, f"\r{names} has been kicked!% server")
            broadcast(server, f"\rnumbers of connections: {num_connections}% server")
# function for checking conneciton status only
def check():
    num_connections = len(list_of_connections) - 1
    broadcast(server, f"\rnumbers of connections: {num_connections}% server")


def connections():
    # if server find a client it will establish a three-way
    # handshake and establishing a connection
    client, addr = server.accept()
    # adding connected client to a list
    # name = client.recv(1024).decode()
    # list_names.append(name)
    list_of_connections.append(client)
    username = client.recv(2024).decode()
    print(username)
    list_names.append(username)
    num_connections = len(list_of_connections) - 1
    print(f"new connection established: {client}")
    print(f"numbers of connections: {num_connections}")

# function to broadcast a message to all the clients except the one where the message came from
def broadcast(client, msg):
    for clients in list_of_connections:
        if clients != server and clients != client:
            try:
                print(msg)
                time.sleep(0.2)
                clients.send(msg.encode())
            except:
                # if the socket connection is broken, we close it off
                client.close()
                remove(client)


def data_splitting(data):
    data_list = data.split('% ')
    print(data_list)
    msg = data_list[0]
    user = data_list[1]
    return msg, user


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
                    if msg:
                        msg, user= data_splitting(msg)
                        if "/kick" in msg:
                            kick(msg)
                        if "/check" in msg:
                            check()
                        else:
                            broadcast(sock, "\r" + user + ": " + msg + "% " + user)

                except:
                    remove(sock)
                    continue


if __name__ == '__main__':
    main()
