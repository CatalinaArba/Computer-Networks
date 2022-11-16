#4.   The client send to the server two sorted array of chars. The server will merge sort the two arrays and return the result to the client.

def mergeArrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0

    # Traverse both array
    while i < n1 and j < n2:

        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1

    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = arr1[i];
        k = k + 1
        i = i + 1

    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = arr2[j];
        k = k + 1
        j = j + 1
    print("Array after merging")
    for i in range(n1 + n2):
        print(str(arr3[i]), end=" ")
    return arr3



import socket
import sys

#3.   A client sends to the server a string. The server returns the reversed string to the client (characters from the end to begging)
def create_socket():
    try:
        global host
        global port
        global s
        host="192.168.0.111"
        port=9999
        s=socket.socket()
    except socket.error as msg:
        print ("Socket creation error: "+str(msg))

#Binding the socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port "+str(port))

        s.bind((host,port))
        s.listen(100)#the number the bad connection that it will tollerate until it will call th error

    except socket.error as msg:
        print("Socket binding error: "+str(msg)+"\n"+"Retrying..")
        bind_socket()

#Establish connection with client (socket must be listening)
def socket_accept():
    conn,address=s.accept()
    print("Connection has been establish | "+"IP "+address[0]+ "| Port "+str(address[1]))
    send_commands(conn)
    conn.close()



#Send commands to client/victim or a friend
def send_commands(conn):
    data=conn.recv(1024)
    nr1= int(data.decode("utf-8").rjust(1024, " ").strip())
    l1=[]
    for i in range(0,nr1):
        data = conn.recv(1024)
        e= data.decode("utf-8").rjust(1024, " ").strip()
        l1.append(e)
    print("Server received l1")

    data = conn.recv(1024)
    nr2 = int(data.decode("utf-8").rjust(1024, " ").strip())
    l2 = []
    for i in range(0, nr2):
        data = conn.recv(1024)
        e = data.decode("utf-8").rjust(1024, " ").strip()
        l2.append(e)
    print("Server received l2")

    r=mergeArrays(l1,l2,nr1,nr2)
    for i in r:
       conn.sendall(str(i).rjust(1024, " ").encode("utf-8"))


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()