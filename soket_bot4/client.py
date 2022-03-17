import socket
import select
import random
import time
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
def receiver():
    data = s.recv(2024).decode()
    data_list = data.split('% ')
    msg = data_list[0]
    user = data_list[1]
    return msg, user


def input_for_host():
    sys.stdout.write('You: ')
    sys.stdout.flush()


def response(answer, username):
    data = answer + "% " + username
    print(username + ": " + answer)
    s.send(data.encode())


def cecilie():
    username = "cecilie"
    s.send(username.encode())
    while True:
        msg, user = receiver()
        print(msg)
        if user in bots:
            continue
        else:
            filter_msg = msg_filter(msg)
            if filter_msg == "false":
                answer = "You goofhead, idk what you meeeean :)"
            elif filter_msg == "hello":
                answer = "hello"
            elif filter_msg == "hi":
                answer = "Whats up!"
            else:
                answer = "I guess we can {}, if there is nothing else to do".format(filter_msg + "ing")
        response(answer, username)


def stefan():
    username = "stefan"
    s.send(username.encode())
    while True:
        alternatives = ["eating", "coding", "hiking", "sleeping", "walking"]
        b = random.choices(alternatives)
        msg, user = receiver()
        print(user + ": " + msg)
        if user in bots:
            continue
        else:
            filter_msg = msg_filter(msg)
            if filter_msg == "false":
                answer = "You should really be clearer, i cant understand you"
            elif filter_msg == "hello":
                answer = "sup"
            elif filter_msg == "hi":
                answer = "Whats up!"
            else:
                answer = "Idk about {}, could we instead do something else like {}?".format(filter_msg + "ing", b)
        response(answer, username)


def vilde():
    username = "vilde"
    s.send(username.encode())
    while True:
        msg, user = receiver()
        print(user + ": " + msg)
        if user in bots:
            continue
        else:
            filter_msg = msg_filter(msg)
            if filter_msg == "false":
                answer = "dummy!!! i dont know what you mean!"
            elif filter_msg == "hello":
                answer = "hey hey :)"
            elif filter_msg == "hi":
                answer = "heyoooo!"
            else:
                answer = " would gladly {}, if its with you ;)".format(filter_msg)
        response(answer, username)


def emma():
    username = "emma"
    s.send(username.encode())
    while True:
        msg, user = receiver()
        print(user + ": " + msg)
        if user in bots:
            continue
        else:
            filter_msg = msg_filter(msg)
            if filter_msg == "false":
                answer = "I did not understand what you said!"
            elif filter_msg == "hello":
                answer = "heloooo"
            elif filter_msg == "hi":
                answer = "hello"
            else:
                answer = "I think {} sounds great! Let's do it!".format(filter_msg + "ing")
        response(answer, username)


def host():
    username = "user"
    s.send(username.encode())
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
                msg, name = receiver()

                if not msg:
                    print("Server not responding")
                    sys.exit()
                else:
                    print(msg)
                    input_for_host()
            else:
                try:
                    msg = sys.stdin.readline()
                    data = msg + "% " + username
                    s.send(data.encode())
                    input_for_host()
                except:
                    print("server not responding")
                    sys.exit()


if __name__ == '__main__':
    globals()[sys.argv[1]]()
