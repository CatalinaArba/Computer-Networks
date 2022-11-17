import socket
import threading
import random
import struct
import time

threads = []
client_guessed = False
upperBound = 2**17-1
lowerBound = 1
number = random.randint(lowerBound,upperBound)
my_lock = threading.Lock()
winner_thread = 0


def handler(client,addr):
    global my_lock, client_guessed, number, winner_thread

    print("Client connected ", addr)
    while not client_guessed:
        guess = struct.unpack("!I",client.recv(4))[0]
        if guess > number:
            client.send('S'.encode())
        if guess < number:
            client.send('H'.encode())
        if guess == number:
            my_lock.acquire()
            client_guessed = True
            winner_thread = threading.get_ident()
            my_lock.release()
            break

    if client_guessed:
        if threading.get_ident() == winner_thread:
            client.send('W'.encode())
        else:
            client.send('L'.encode())

    time.sleep(1)
    client.close()


if __name__ == '__main__':
    try:
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind(("127.0.0.1",1234))
        server.listen(5)
    except Exception:
        print("Error on creating the socket")
        exit(-1)

    print("Number chosen ", str(number))
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handler,args=(client,addr))
        threads.append(thread)
        thread.start()