import socket


def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.0.111'
    port = 9999
    s.connect((host, port))

    # Reading inputs
    l1 = []
    nr1 = int(input("Enter the number of elements for the first list: "))
    for i in range(0, nr1):
        e = int(input('e='))
        l1.append(e)

    l2 = []
    nr2 = int(input("Enter the number of elements for the second list: "))
    for i in range(0, nr2):
        e = int(input('e='))
        l2.append(e)

    # Sending inputs
    s.sendall(sendable_data(nr1))
    for i in l1:
        s.sendall(sendable_data(i))
    print("First array sent: " + repr(l1))

    s.sendall(sendable_data(nr2))
    for i in l2:
        s.sendall(sendable_data(i))
    print("Second array sent: " + repr(l2))

    # Receiving outputs
    data = s.recv(1024)
    length = int(data.decode("utf-8").strip())
    resulted_list = []
    for i in range(0, length):
        data = s.recv(1024)
        letter = int(data.decode("utf-8").strip())
        resulted_list.append(letter)

    #Print results
    print("Result: "+repr(resulted_list))
    s.close()