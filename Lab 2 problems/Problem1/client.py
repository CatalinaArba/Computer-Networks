import socket
import struct

def sendable_data(data):
    return str(data).encode("utf-8")


if __name__=="__main__":
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host='127.0.0.1'
    port=9999
    s.connect((host, port))

    #Read inputs
    cmd=input('Enter your command: ')


    #Send imputs
    s.sendall(sendable_data(cmd))
    print("Command was sent")

    #Receive outputs
    data=s.recv(1024)
    len_output=int(data.decode("utf-8").rjust(1024, " ").strip())
    outputs=""
    data = s.recv(1024)#outputs function from server sends b'the outputs' and i want to print the outputs without b' '
    data = s.recv(1024)
    for i in range(2,len_output-1):
        data = s.recv(1024)
        letter = str(data.decode("utf-8").rjust(1024, " ").strip())

        if letter=='n' and outputs[-1]=='\\':#output function sends \\n instead \n so it prints all in a line and i don't like it
            outputs = outputs[:-1]
            outputs+="\n"
        else :
            outputs+=letter
    data = s.recv(1024)
    print(outputs)
    s.close()
