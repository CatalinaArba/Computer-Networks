#1.   The client takes a string from the command line and sends it to the server. The server interprets the string as a command with its parameters. It executes the command and returns the standard output and the exit code to the client.
import socket
import sys
import subprocess
import threading
def sendable_data(data):
    return str(data).encode("utf-8")
#1.   A client sends to the server an array of numbers. Server returns the sum of the numbers.
#Create a socket (connesct two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host="127.0.0.1"
        port=9999
        s=socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
        s.listen(5)#the number the bad connection that it will tollerate until it will call th error


    except socket.error as msg:
        print("Socket binding error: "+str(msg)+"\n"+"Retrying..")
        bind_socket((host,port))

#Establish connection with client (socket must be listening)
def socket_accept():
    conn,address=s.accept()
    print("Connection has been establish | "+"IP "+address[0]+ "| Port "+str(address[1]))

    thread = threading.Thread(target=handler, args=(conn, address))
    thread.start()


#Send commands to client/victim or a friend
def handler(conn,address):
    msg = conn.recv(1024).decode()
    print("Server received command: ", msg+'|')
    msg_list = msg.split(' ')
    try:
        list_files = subprocess.run(msg_list,stdout=subprocess.PIPE)
        output =str(list_files.stdout)
        len_output=len(output)
        print("The exit code was: " + output+"\n"+str(len_output))
        conn.send(str(len_output).rjust(1024, " ").encode("utf-8").strip())
        print("Sent the length!")
        for i in output:
            conn.send(str(i).rjust(1024, " ").encode("utf-8"))
        conn.close()
    except Exception:
        print("Couldn't execute the command")
        conn.send("Couldn't execute the command".encode())


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()