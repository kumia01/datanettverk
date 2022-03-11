import socket
import threading


list_of_connections = []
threadcount = 0

if __name__ == '__main__':
    main()

def main():
    print("[starting] server is starting")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    print(f"[listening] Server is listening")
    print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, see, look, sing, work")
    print("for additional commands type /help")
    while True:
        global threadcount


        clientSocket, address = s.accept()
        list_of_connections.append(clientSocket)
        threadcount += 1
        num_connections = len(list_of_connections)

        print(f"num_connections: {num_connections}")
        print(f"numbers of threads: {threadcount}")
        print(f"Connection with {address} established!")
        print("------ you can now write ------")


        thread1 = threading.Thread(target=handle_client)
        thread1.start()

def handle_client():
    while True:
            msg = input()
            if msg == "/help":
                print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, see, look, sing, work")
                print("to kick you have to write: /kick [person]")
                print("to close down the chat room type /close")
            elif msg == "/close":
                server.close()
            else:
                broadcast(msg)

def broadcast(msg):
    for clients in list_of_connections:
        print("passing")
        try:
            clients.send(msg.encode())
            text = clients.recv(1024).decode()
            print(text)
        except:
            clients.close()
            remove(clients)

def remove(client):
    global threadcount

    if client in list_of_connections:
        list_of_connections.remove(client)

    num_connections = len(list_of_connections)
    threadcount -= 1
    print(f"numbers of connections: {num_connections}")
    print(f"numbers of threads: {threadcount}")


