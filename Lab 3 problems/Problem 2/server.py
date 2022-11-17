import random

import time
import socket

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024
client_guessed = False
upperBound = 10
lowerBound = 1
number = random.randint(lowerBound,upperBound)
print("Server number:"+str(number))
winner_address=''

try:
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server.bind((localIP, localPort))
except Exception:
    print("Error on creating the socket")
    exit(-1)


print("UDP server up and listening")
while True:
    guess = server.recvfrom(bufferSize)
    message = int(guess[0].decode())
    address = guess[1]
    while not client_guessed:

        messageToSend=''
        print("Server receives: "+str(message)+" from"+str(address))
        if message > number:
            messageToSend='S'
            bytesToSend=str.encode(messageToSend)
            server.sendto(bytesToSend,address)
            guess = server.recvfrom(bufferSize)
            message = int(guess[0].decode())
            address = guess[1]
            #print("S- sent")
        if message < number:
            messageToSend='H'
            bytesToSend = str.encode(messageToSend)
            server.sendto(bytesToSend, address)
            guess = server.recvfrom(bufferSize)
            message = int(guess[0].decode())
            address = guess[1]
            #print("H- sent")
        if message == number:
            client_guessed = True
            winner_address=address
            #print("Guessed ")


    if address==winner_address:
        messageToSend = 'W'
        bytesToSend = str.encode(messageToSend)
        server.sendto(bytesToSend, address)
        #print("W- sent")
    else:
        messageToSend = 'L'
        bytesToSend = str.encode(messageToSend)
        server.sendto(bytesToSend, address)
        #print("L- sent")

    time.sleep(5)

