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
    #cmd=input('Enter your file path: ')
    cmd="/home/arba/Documents/Labs/Lab2/Problem2/Problem2_textFilee"
    new_name = cmd + "-copy"

    #Send imputs
    s.sendall(sendable_data(cmd))
    print("Command was sent")

    #Receive outputs
    data=s.recv(1024)
    len_output=int(data.decode("utf-8").rjust(1024, " ").strip())
    if (len_output!=-1):
        outputs=""
        for i in range(0,len_output):
            data = s.recv(1024)
            letter = data.decode("utf-8").rjust(1024, " ").strip()
            if letter=='':#strip deletes the spaces and we add back them, I tried send data without strip and it doesn't work idk why
                outputs+=' '
            else:
                outputs+=letter
        # Print results
        print(str(len_output) + '\n' + outputs)

        with open(new_name, 'w') as f:
            f.write(str(len_output)+"\n"+outputs)
    else:
        print("The file doesn't exist!")
        with open(new_name, 'w') as f:
            f.write(str(len_output))

    s.close()