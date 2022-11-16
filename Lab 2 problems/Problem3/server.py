#3.   The server chooses a random float number <SRF>. Run multiple clients. Each client chooses a random float number <CRF> and send it to the server. When the server does not receive any incoming connection for at least 10 seconds it chooses the client that has guessed the best approximation (is closest) for its own number and sends it back the message “You have the best guess with an error of <SRV>-<CRF>”. It also sends to each other client the string “You lost !”. The server closes all connections after this.
import copy
import struct
import time
import socket
import threading
import random
import os
my_num= random.randint(0,10)
print('Server number: ',my_num)



client_count = 0
client_finishes=0
numbers_list = []
my_lock = threading.Lock()
threads = []
found=False

def min_val():
    mini=numbers_list[0]
    for i in numbers_list:
        mini=min(mini,i)
    return mini

def worker(cs):
    global client_count, numbers_list,client_finishes,found
    client=copy.deepcopy(client_count)#client count will be inceased after every client connection so we keep the value of the current client in variable client
    print('Client nr', client, 'has entered the game!')

    n = int(cs.recv(1024).decode("utf-8"))
    print(str(client)+" "+str(n))
    val=abs(my_num-n)

    my_lock.acquire()
    numbers_list.append(val)
    my_lock.release()
    time.sleep(10)
    client_finishes+=1
    while(client_finishes!=client_count):
        time.sleep(1)
    mini=min_val()
    my_lock.acquire()
    if mini==val and  not found:
        print('Client nr', client, ' won!')
        message='You won!'
        found=True
    else:
        print('Client nr', client, 'lost !')
        message = 'You lost!'
    my_lock.release()

    cs.send(str(message).rjust(1024, " ").encode("utf-8"))


    cs.close()
    time.sleep(1)
    print('Thread ', client, 'ended!')
    exit(0)

if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 5555))
        s.listen(5)

    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    while True:  # for each client we have a thread
        client_socket, addr = s.accept()
        t = threading.Thread(target=worker, args=(client_socket))
        threads.append(t)
        client_count += 1
        t.start()