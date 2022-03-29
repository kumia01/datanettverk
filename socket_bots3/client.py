import socket
import random
import sys
import re

# creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[2], int(sys.argv[3])))

# creating list of bots
bots = ["cecilie", "emma", "stefan", "vilde", "server"]


# function that filters the msg coming from server to simple verbs
def get_response(response):
    library = ["fight", "talk", "fish", "ski", "walk", "cry", "eat", "play", "scare", "see", "look", "sing", "work",
               "hello", "hi"]
    for verb in library:
        if verb in response:
            return verb


# function that listen for msg from server
def receiver_for_bots():
    try:
        data = s.recv(1024).decode()
    except:
        print("server not responding")
    data_list = data.split('% ')
    msg = data_list[0]
    user = data_list[1]
    return msg, user


def response(data, username):
    msg = data + "% " + username
    s.send(msg.encode())


def cecilie():
    username = "cecilie"
    s.send(username.encode())
    print(s.recv(1024).decode())
    while True:
        msg, user = receiver_for_bots()
        print(user + ": " + msg)
        if user in bots:
            continue
        else:
            if msg == "kicked":
                answer = "I will remember this, I hope you sleep nice today because it will be you last..."
                s.send(answer.encode())
                s.close()
            filter_msg = get_response(msg)
            if filter_msg is None:
                answer = "You goofhead, idk what you meeeean :)"
            elif filter_msg == "hello":
                answer = "HI!"
            elif filter_msg == "hi":
                answer = "HI!"
            else:
                answer = "I guess we can {}, if there is nothing else to do".format(filter_msg + "ing")
        response(answer, username)


def stefan():
    username = "stefan"
    s.send(username.encode())
    print(s.recv(1024).decode())
    while True:
        msg, user = receiver_for_bots()
        print(user + ": " + msg)
        if user in bots:
            continue
        else:
            alternatives = ["eating", "coding", "hiking", "sleeping", "walking"]
            b = random.choice(tuple(alternatives))
            if msg == "kicked":
                answer = "this is why you will remain maidless..."
                s.send(answer.encode())
                s.close()
            filter_msg = get_response(msg)
            if filter_msg is None:
                answer = "You should really be clearer, i cant understand you"
            elif filter_msg == "hello":
                answer = "hello"
            elif filter_msg == "hi":
                answer = "Whats up!"
            else:
                answer = "Idk about {}, could we instead do something else like {}?".format(filter_msg + "ing", b)
        response(answer, username)


def vilde():
    username = "vilde"
    s.send(username.encode())
    print(s.recv(1024).decode())
    while True:
        msg, user = receiver_for_bots()
        print(user + ": " + msg)
        if user in bots:
            continue
        else:
            if msg == "kicked":
                answer = "Noooo... I thought we where friends :("
                s.send(answer.encode())
                s.close()
            filter_msg = get_response(msg)
            if filter_msg is None:
                answer = "dummy!!! i dont know what you mean!"
            elif filter_msg == "hello":
                answer = "hey hey :)"
            elif filter_msg == "hi":
                answer = "heyoooo!"
            else:
                answer = "I would gladly {}, if its with you ;)".format(filter_msg)
        response(answer, username)


def emma():
    username = "emma"
    s.send(username.encode())
    print(s.recv(1024).decode())
    while True:
        msg, user = receiver_for_bots()
        print(user + ": " + msg)
        if user in bots:
            continue
        else:
            if msg == "kicked":
                answer = "I accept my fate, rememeber me...."
                s.send(answer.encode())
                s.close()
            filter_msg = get_response(msg)
            if filter_msg is None:
                answer = "I did not understand what you said!"
            elif filter_msg == "hello":
                answer = "heloooo"
            elif filter_msg == "hi":
                answer = "hello"
            else:
                answer = "I think {} sounds great! Let's do it!".format(filter_msg + "ing")
        response(answer, username)


if __name__ == '__main__':
    globals()[sys.argv[1]]()
