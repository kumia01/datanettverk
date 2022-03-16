import socket
import select
import random
import sys
import re


# creating list of bots
bots = ["cecilie", "emma", "stefan", "vilde"]

# creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((str(sys.argv[2]), int(sys.argv[3])))
except:
    print("Unable to connect to server")
    sys.exit()


# function that filters the msg coming from server to simple verbs
def msg_filter(response):
    split_message = re.split(r'\s+|[,;?!.-]\s*', response.lower())
    library = ["fight", "talk", "fish", "ski", "walk", "cry", "eat", "play", "scare", "see", "look", "sing", "work",
               "hello", "hi"]
    verb = set(split_message).intersection(library)
    isEmpty = (len(verb) == 0)
    if isEmpty:
        return "false"
    str_val = ' and '.join(list(map(str, verb)))
    return str_val


# function that listen for msg from server
def receiver_for_bots():
    user = s.recv(1024).decode()
    msg = s.recv(1024).decode()
    return msg, user


def input_for_host():
    sys.stdout.write('You: ')
    sys.stdout.flush()


def cecilie():
    username = "cecilie"
    s.send(username.encode())
    while True:
        msg, user = receiver_for_bots()
        if msg == "kicked":
            s.send("Noooo!".encode())
            s.close()
        if user in bots:
            continue
        else:
            filter_msg = msg_filter(msg)
            if filter_msg == "false":
                s.send("Cecilie: You goofhead, idk what you meeeean :)".encode())
            elif filter_msg == "hello":
             s.send("Cecilie: HI!".encode())
            elif filter_msg == "hi":
                s.send("Cecilie: HI!".encode())
            else:
                answer = "Cecilie: I guess we can {}, if there is nothing else to do".format(filter_msg + "ing")
                s.send(answer.encode())








def stefan():
    # username = "stefan"
    # s.send(username.encode())
    print(s.recv(1024).decode())
    while True:
        alternatives = ["eating", "coding", "hiking", "sleeping", "walking"]
        b = random.choices(alternatives)
        msg, user = receiver_for_bots()
        if msg == "kicked":
            s.send("Stefan: this is why you will remain maidless...".encode())
            s.close()
        if user in bots:
            continue
        else:
            filter_msg = msg_filter(msg)
            if filter_msg == "false":
                s.send("Stefan: You should really be clearer, i cant understand you".encode())
            elif filter_msg == "hello":
                s.send("Stefan: hello".encode())
            elif filter_msg == "hi":
                s.send("Stefan: Whats up!".encode())
            else:
                answer = "Stefan: Idk about {}, could we instead do something else like {}?".format(filter_msg + "ing", b)
                s.send(answer.encode())


def vilde():
    username = "vilde"
    s.send(username.encode())
    print(s.recv(1024).decode())
    while True:
        msg = receiver_for_bots()
        if msg == "kicked":
            s.send("Vilde: Noooo... I thought we where friends :(")
            s.close()
        filter_msg = msg_filter(msg)
        if filter_msg == "false":
            s.send("Vilde: dummy!!! i dont know what you mean!".encode())
        elif filter_msg == "hello":
            s.send("Vilde: hey hey :)".encode())
        elif filter_msg == "hi":
            s.send("Vilde: heyoooo!".encode())
        else:
            answer = "Vilde: I would gladly {}, if its with you ;)".format(filter_msg)
            s.send(answer.encode())


def emma():
    # username = "emma"
    # s.send(username.encode())
    print(s.recv(1024).decode())
    while True:
        msg = receiver_for_bots()
        if msg == "kicked":
            s.send("Emma: I accept my fate, rememeber me....".encode())
            s.close()
        filter_msg = msg_filter(msg)
        if filter_msg == "false":
            s.send("Emma: I did not understand what you said!".encode())
        elif filter_msg == "hello":
            s.send("Emma: heloooo".encode())
        elif filter_msg == "hi":
            s.send("Emma: hello".encode())
        else:
            answer = "Emma: I think {} sounds great! Let's do it!".format(filter_msg + "ing")
            s.send(answer.encode())


def host():
    #  username = input("Username: ")
    #  s.send(username.encode())
    print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, see, look, "
          "sing, work")
    print("to kick a bot type /kick [bot name]")
    print("/check to check number of connected clients")

    input_for_host()

    while True:
        socket_list = [sys.stdin, s]

        # getting the sockets readable inputs
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            if sock == s:
                msg = sock.recv(1024)

                if not msg:
                    print("Server not responding")
                    sys.exit()
                else:
                    sys.stdout.write(msg.decode())
                    input_for_host()

            else:
                msg = sys.stdin.readline()
                s.send(msg)
                input_for_host()


if __name__ == '__main__':
    globals()[sys.argv[1]]()
