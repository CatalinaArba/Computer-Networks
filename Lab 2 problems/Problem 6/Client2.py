import socket
import struct
import random
import time

try:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except Exception:
    print("Error on creating the socket")
    exit(-1)

try:
    client.connect(("127.0.0.1",1234))
except Exception:
    print("Error on connecting to server")
    exit(-1)

playing = True
upperBound = 2**17-1
lowerBound = 1
while playing:
    number = random.randint(lowerBound,upperBound)
    try:
        client.send(struct.pack("!I",number))
        print("Sending number ", str(number))
        answer = client.recv(1).decode()
    except Exception:
        print("Error while processing data")
        client.close()
        exit(-1)

    print("Client received answer: ", answer)
    if answer == 'H':
        lowerBound = number
    if answer == 'S':
        upperBound = number
    if answer == 'W' or answer == 'L':
        playing = False
    time.sleep(0.25)

client.close()
if answer == 'W':
    print("I am the winner")
elif answer == 'L':
    print("I lost")