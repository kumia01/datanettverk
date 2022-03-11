import socket
import threading


list_of_connections = []
threadcount = 0
def handle_client():
    while True:
            msg = input()
            if msg == "--help":
                print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, see, look, sing, work")
            else:
                broadcast(msg)

def broadcast(msg):
    for clients in list_of_connections:
            try:
                clients.send(msg.encode())
                text = clients.recv(1024).decode()
                print(text)
            except:
                continue


def remove(client):
    global threadcount

    if client in list_of_connections:
        print(client)
        list_of_connections.remove(client)

    num_connections = len(list_of_connections)

    print(f"numbers of connections: {num_connections}")
    print(f"numbers of threads: {threadcount}")


def main():
    print("[starting] server is starting")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    print(f"[listening] Server is listening")
    print("for additional commands type --help")

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






if __name__ == '__main__':
    main()
