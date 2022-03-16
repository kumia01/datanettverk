import socket
import threading

# list of clients connected to the server
list_of_connections = []
list_names = []

# how many clients that can connect to the server
max_client = 4

print("[starting] server is starting")
# creating socket object with TCP protocol and
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# we bind the port so that server listen to request coming from other computers on the network
server.bind((socket.gethostname(), 1234))

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
            print(msg)
            client.close()
            remove(client)


def input_and_output():
    # a loop that listen for input and output
    while True:
        # starting input for conversation with the bots

        msg = input("You: ")

        # inputs from certain commands or sending message
        if msg == "/help":
            print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, see, look, "
                  "sing, work")
            print("to kick a bot type /kick [bot name]")
            print("/check to check number of connected clients")
        elif "/kick" in msg:
            kick(msg)
        elif msg == "/check":
            num_connections = len(list_of_connections)
            print(list_names)
            print(f"numbers of connections established: {num_connections}")
        else:
            broadcast(msg)


def connections():
    while True:
        # if server find a client it will establish a three-way
        # handshake and establishing a connection
        client, addr = server.accept()
        # adding connected client to a list
        name = client.recv(1024).decode()
        client.send("You are connected!".encode())
        list_names.append(name)
        list_of_connections.append(client)


def broadcast(msg):
    for clients in list_of_connections:
        try:
            # sending and receiving data from client
            clients.send(msg.encode())
            text = clients.recv(1024).decode()
            # printing out the decoded message from client
            print(text)
        except:
            # if client won't respond we close its connection
            remove(clients)
            clients.close()


# function to remove a client from connection list
def remove(client):
    if client in list_of_connections:
        list_of_connections.remove(client)
    num_connections = len(list_of_connections)
    print(f"numbers of connections: {num_connections}")



def main():
    print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, see, look, "
          "sing, work")
    print("type /help for other info")
    print("/check to check number of connected clients")

    # establishing threading for running parallel between accepting connections and listening for input and output
    thread1 = threading.Thread(target=connections)
    thread2 = threading.Thread(target=input_and_output)
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    main()
