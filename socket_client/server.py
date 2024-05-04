import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1051
s.bind((host, port))

s.listen(5)

print("listning on {} {}".format(host, port)+ " ......")

while True:
    error = False
    socket_data, sender_address = s.accept()

    print("Established connection with: ", sender_address)

    value1 = float(socket_data.recv(port).decode('utf-8'))
    print("*",value1)

    value2 = float(socket_data.recv(port).decode('utf-8'))
    print("*", value2)

    operation = socket_data.recv(port).decode('utf-8')
    print("*", operation)

    match operation:
        case '+':
            response = value1 + value2
        case '-':
            response = value1 - value2
        case '*':
            response = value1 * value2
        case '/':
            response = value1 / value2
        case '%':
            response = value1 % value2
        case _:
            print("ERROR: Unknown operation.")
            error = True
            break

    print("=", response)

    response = str(response).encode('utf-8')

    socket_data.send(response)

    socket_data.close()

s.close()
print("socket connection closed.")
