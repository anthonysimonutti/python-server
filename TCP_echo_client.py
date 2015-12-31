# TCP Echo Client example
# based on https://pymotw.com/2/socket/tcp.html

import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# unlike the server, the client uses connect() to connect directly to the server
# connect the socket to the port where the server is listening
server_address = ('localhost', 8080)
print "Connection to %s on %s" % server_address
sock.connect(server_address)

# after the connection is established data is sent through the socket with sendall() and recieved with recv()
try:
    # send some data
    message = "This is some data that we will receive back. Echo!"
    print "Sending '%s'" % message
    sock.sendall(message)

    # look for a response and make sure we receive the expected amount
    received = 0
    expected = len(message)

    # Receive messages until the entire message is received
    while received < expected:
        data = sock.recv(16)
        received += len(data)
        print 'Received "%s"' % data

finally:
    # Close the socket if the entire message is received or if there is an error
    print "Closing socket"
    sock.close()
