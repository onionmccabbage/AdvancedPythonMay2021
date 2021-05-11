import socket
import sys

# open a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
param_tup = ('localhost', 9874)
# try to connect to the server
sock.connect(param_tup)

# see any parameter message
# print(sys.argv[0:])
# send a message to the server
if len(sys.argv) > 1:
    msg = ' '.join(sys.argv[1:])
else: 
    msg = 'default message'
sock.send(msg.encode()) # needs to be encoded
# handle any response from the server
data = sock.recv(1024) # up to 1024 bytes
print(data)
sock.close()
