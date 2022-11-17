import socket
import struct


if __name__ == '__main__':
    serverAddressPort   = ("127.0.0.1", 20001)

    bufferSize          = 1024
    try:
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    except socket.error as err:
        print('Error', err.strerror)
        exit(-1)

    mess = s.recv(128).decode('ascii')
    print(mess)

    finished = False

    while not finished:
        n = int(input('Enter number: '))
        s.send(struct.pack("!I", n))

        if n != 0:
            for i in range(n):
                x = int(input('Enter elem: '))
                s.send(struct.pack("!I", x))

        if n == 0:
            finished = True

        arr_size = s.recv(4)
        arr_size = struct.unpack('!I', arr_size)[0]

        my_array = []

        for i in range(arr_size):
            x = s.recv(4)
            x = struct.unpack('!I', x)[0]
            my_array.append(x)

        print(arr_size)
        print(my_array)

    s.close()
