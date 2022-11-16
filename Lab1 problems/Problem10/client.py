import socket


def sendable_data(data):
    return str(data).rjust(1024, " ").encode("utf-8")


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.0.111'
    port = 9999
    s.connect((host, port))

    # Reading inputs
    l1 = ""
    l1 = input("Enter the first string:")

    l2=""
    l2 = input("Enter the second string:")

    # Sending inputs
    s.sendall(sendable_data(len(l1)))
    for i in l1:
        s.sendall(sendable_data(i))
    print("First array sent: " + repr(l1))

    s.sendall(sendable_data(len(l2)))
    for i in l2:
        s.sendall(sendable_data(i))
    print("Second array sent: " + repr(l2))

    # Receiving outputs
    data = s.recv(1024)
    letter = data.decode("utf-8").strip()
    data = s.recv(1024)
    count = int(data.decode("utf-8").strip())

    #Print results
    print("Result: letter="+str(letter)+" count="+str(count))
    s.close()