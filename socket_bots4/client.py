import socket
import threading
import random
import sys
import re

# creating list of bots
bots = ["cecilie", "emma", "stefan", "vilde", "server"]

# creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock = s.connect((str(sys.argv[2]), int(sys.argv[3])))
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
    try:
        data = s.recv(1024).decode()
    except:
        print("server not responding")
    data_list = data.split('% ')
    msg = data_list[0]
    user = data_list[1]
    return msg, user


def input_for_host():
    sys.stdout.write('You: ')
    sys.stdout.flush()


def broadcast_host(username):
    msg = sys.stdin.readline().strip()
    if "/help" in msg:
        print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, "
              "see, look, "
              "sing, work")
        print("to kick a bot type /kick [bot name]")
        print("/check to check number of connected clients")
        input_for_host()
    else:
        data = msg + "% " + username
        s.send(data.encode())
        input_for_host()


def reciever_for_host():
    while True:
        try:
            data = s.recv(1024).decode()
        except:
            print("server not responding")
        data_list = data.split('% ')
        msg = data_list[0]
        user = data_list[1]
        print(msg)
        input_for_host()


def response(answer, username, b=None):
    data = answer + "% " + username
    print(username + ": " + answer)
    s.send(data.encode())


def cecilie():
    username = "cecilie"
    s.send(username.encode())
    while True:
        msg, user = receiver()
        print(user + ": " + msg)
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
        alt = str(random.choices(alternatives[0]))
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
                answer = "Idk about {}, could we instead do something else like {}?".format(filter_msg + "ing", alt)
            response(answer, username, alt)


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
    global sock
    username = input("username: ")
    s.send(username.encode())
    print("to chat with bot use any verb like: fight, fish, ski, walk, cry, eat, play, scare, see, look, "
          "sing, work")
    print("to kick a bot type /kick [bot name]")
    print("/check to check number of connected clients")
    print("write /help to see the information again")

    input_for_host()

    while True:
        thread1 = threading.Thread(target=reciever_for_host)
        thread2 = threading.Thread(target=broadcast_host, args=username)
        thread1.start()
        thread2.start()


if __name__ == '__main__':
    globals()[sys.argv[1]]()
