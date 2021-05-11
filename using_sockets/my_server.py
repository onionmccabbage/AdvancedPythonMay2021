import socket

# we can instantiate a socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# we may need some parameters - IP and port
param_tup = ('localhost', 9874)
# bind the prameters to the server
server.bind(param_tup)
# begin listening
server.listen(5) # max requests
print('the server is running on {} port {}'.format(param_tup[0], param_tup[1]))

# respond to requests in a run-loop
while True:
    # unpack the requests
    (client, addr) = server.accept()
    # read some data - in this case 1024 bytes from the client
    buf = client.recv(1024)
    print('server has received {}'.format(buf))
    # send a response back to the client
    client.send( buf.upper() ) # we choose to return in upper case
    client.close()
    # if the client sends 'quit' then stop the server
    if buf == b'quit': # a byte-encoded text saying 'quit'
        print('server is stopping')
        server.close()
        break
