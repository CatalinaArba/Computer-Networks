import socket
import struct
import random
import time
import sys
import threading
def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")

#def TCP_sending_numbers(client):


#def UDP_receiving_data():


if __name__ == '__main__':
    #TCP Socket
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

    #UDP socket
    # try:
    #     UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    #     UDPclient.bind(('127.0.0.1', 1234))
    # except Exception:
    #     print("Error on creating the socket")
    #     exit(-1)

    upperBound = 100
    lowerBound = -100
    for i in range(0, 100):
        print("ROUND " + str(i))
        x = random.randint(lowerBound, upperBound)
        y = random.randint(lowerBound, upperBound)
        try:
            client.send(sendable_data(x))
            client.send(sendable_data(y))
            time.sleep(2)

            print("Sending number ", str(x) + " " + str(y))
            answer = client.recv(1024).decode()
            print("Client received: " + answer)

            # data = client.recvfrom(1024)
            # answer = data[0].decode()
            # print("Client received from UDP ", str(answer))
        except Exception:
            print("Error while processing data")
            client.close()
            exit(-1)

    client.close()


    #client.send(struct.pack('!I', client_port))
    #TCP_thread = threading.Thread(target=TCP_sending_numbers, args=(client))
    #TCP_thread.start()
    #UDP_thread = threading.Thread(target=read_user_msg, args=(peer_socket,))



