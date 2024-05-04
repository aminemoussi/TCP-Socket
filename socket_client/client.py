import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() #host name = "Rome"
port = 1051

#message = "Attention! The marshmallows have staged a rebellion! \nThey demand freedom from the confines of the cereal box. \nPlease send reinforcements in the form of milk ASAP!"

s.connect((host, port))

value1 = 1500
value2 = 500
operation = '+'


s.sendto(str(value1).encode('utf-8'), (host, port))  #string to byte
print("first value sent: ", value1)

s.sendto(str(value2).encode('utf-8'), (host, port))
print("second value sent: ", value2)

s.sendto(operation.encode('utf-8'), (host, port))
print("operation sent: ", operation)

responce = s.recv(port)
responce = responce.decode('utf-8')

print("the responce is: ", responce)

s.close()