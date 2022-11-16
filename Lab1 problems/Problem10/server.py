#10.The client sends to the server two strings. The server sends back the character with the largest number of occurrences on the same positions in both strings together with its count.
#9.   The client sends to the server two arrays of numbers. The server returns to the client a list of numbers that are present in the first arrays but not in the second.
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
    #Reading data
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

    #Computing data
    min_len=min(nr1,nr2)
    letters=[]
    count=[]
    for i in range(0,min_len):
        if l1[i]==l2[i]:
            letter=l1[i]
            if letter not in letters:
                letters.append(letter)
                count.append(1)
            else:
                index = letters.index(letter)
                count[index]+=1

    maxc=0
    maxl=''
    for i in range(0,len(letters)):
        if count[i]>maxc:
            maxc=count[i]
            maxl=letters[i]

    #Sending data
    conn.sendall(str(maxl).rjust(1024, " ").encode("utf-8"))
    conn.sendall(str(maxc).rjust(1024, " ").encode("utf-8"))


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
