import socket
import threading
import random
import sys
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))



def get_response(response):
    split_message = re.split(r'\s+|[,;?!.-]\s*', response.lower())
    library = ["fight", "talk", "fish", "ski", "walk", "cry", "eat", "play", "scare", "see", "look", "sing", "work"]
    verb = set(split_message).intersection(library)
    isEmpty = (len(verb) == 0)
    if isEmpty:
        return "false"
    str_val = ' and '.join(list(map(str, verb)))
    return str_val


def reciever_for_bots():
    msg = s.recv(1024).decode()
    return msg


def cecilie():
    username = "cecilie"
    s.send(username.encode())
    while True:
        msg = reciever_for_bots()
        if msg == "kicked":
            s.send("Cecilie: I will remember this, I hope you sleep nice today because it will be you last...")
        filter_msg = get_response(msg)
        if filter_msg == "false":
            s.send("Cecilie: You goofhead, idk what you meeeean :)".encode())
        else:
            answer = "Cecilie: I guess we can {}, if there is nothing else to do".format(filter_msg + "ing")
            s.send(answer.encode())


def stefan():
    username = "stefan"
    s.send(username.encode())
    while True:
        alternatives = ["eating", "coding", "hiking", "sleeping", "walking"]
        b = random.choices(alternatives)
        msg = reciever_for_bots()
        if msg == "kicked":
            s.send("Stefan: this is why you will remain maidless...".encode())
        filter_msg = get_response(msg)
        if filter_msg == "false":
            s.send("Stefan: You should really be clearer, i cant understand you".encode())
        else:
            answer = "Stefan: Idk about {}, could we instead do something else like {}?".format(filter_msg + "ing", b)
            s.send(answer.encode())


def vilde():
    username = "vilde"
    s.send(username.encode())
    while True:
        msg = reciever_for_bots()
        if msg == "kicked":
            s.send("Vilde: Noooo... I thought we where friends :(")
        filter_msg = get_response(msg)
        if filter_msg == "false":
            s.send("Vilde: dummy!!! i dont know what you mean!".encode())
        else:
            answer = "Vilde: I would gladly {}, if its with you ;)".format(filter_msg)
            s.send(answer.encode())


def emma():
    username = "emma"
    s.send(username.encode())
    while True:
        msg = reciever_for_bots()
        if msg == "kicked":
            s.send("Emma: I accept my fate, rememeber me....".encode())
        filter_msg = get_response(msg)
        if filter_msg == "false":
            s.send("Emma: I did not understand what you said!".encode())
        else:
            answer = "Emma: I think {} sounds great! Let's do it!".format(filter_msg + "ing")
            s.send(answer.encode())


if __name__ == '__main__':
    globals()[sys.argv[1]]()
