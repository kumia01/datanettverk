import socket
import threading

list_of_connections = []
list_names = []
max_client = 4


print("[starting] server is starting")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1234))
server.listen(max_client)
print(f"[listening] Server is listening")

def kick(msg):
    for names in list_names:
        if names in msg:
            client = list_of_connections[list_names.index(names)]
            client.send("kicked".encode())
            msg = client.recv(1024).decode()
            print(msg)
            client.close()
            remove(client)




def connections():
    for x in range(0, max_client):
        # if server find a client it will establish a three-way
        # handshake and establishing a connection
        client, addr = server.accept()

        # adding connected client to a list
        name = client.recv(1024).decode()
        list_names.append(name)
        print(list_names)
        list_of_connections.append(client)
        print(f"Connection with {addr} established")

def broadcast(msg):
    for clients in list_of_connections:
        try:
            clients.send(msg.encode())
            text = clients.recv(1024).decode()
            print(text)
        except:
            remove(clients)
            clients.close()


# function to remove a client
def remove(client):
    if client in list_of_connections:
        client.close()
        list_of_connections.remove(client)
    num_connections = len(list_of_connections)
    print(f"numbers of connections: {num_connections}")


# establishing what type of protocol is going to be used
# AF_INET is the TCP protocol
# establishing a server on the ip address with port 1234
# listening for connection for max 5 clients
def main():
    print("waiting for all clients are connected")
    connections()
    num_connections = len(list_of_connections)
    print(f"numbers of connections established: {num_connections}")
    print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, see, look, "
          "sing, work")
    print("type /help for other info")
    # a loop that listen for input and output
    while True:
        # starting input for conversation with the bots
        msg = input("You: ")
        if msg == "/help":
            print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, see, look, "
                  "sing, work")
            print("to kick a bot type /kick [bot name]")
        elif "/kick" in msg:
            kick(msg)
        else:
            broadcast(msg)


if __name__ == '__main__':
    main()
