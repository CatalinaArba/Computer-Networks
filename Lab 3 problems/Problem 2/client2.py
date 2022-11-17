import socket
import struct
import random
import time

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024
try:
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
except Exception:
    print("Error on creating the socket")
    exit(-1)

playing = True
upperBound = 10
lowerBound = 1
while playing:
    number = random.randint(lowerBound,upperBound)
    try:
        client.sendto(str.encode(str(number)),serverAddressPort)
        print("Sending number ", str(number))
        data = client.recvfrom(bufferSize)
        answer=data[0].decode()
        #print("Receiving number ", str(answer))
    except Exception:
        print("Error while processing data")
        client.close()
        exit(-1)

    print("Client received answer: ", answer)
    if answer == 'H':
        lowerBound = number+1
    if answer == 'S':
        upperBound = number-1
    if answer == 'W' or answer == 'L':
        playing = False
        print("Exit while")
    time.sleep(5)
client.close()
if answer == 'W':
    print("I am the winner")
elif answer == 'L':
    print("I lost")
