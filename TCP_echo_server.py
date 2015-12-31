# TCP Echo Server example
# based on https://pymotw.com/2/socket/tcp.html

import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind() associates a socket with a server address
# bind the socket to a port (port 8080)
server_address = ('localhost', 8080)
print "Starting server on %s port %s" % server_address
sock.bind(server_address)
# listen puts the socket in server mode, accept waits for incoming connection
sock.listen(1)

while True:
    # wait for a connection
    print "Waiting for a connection..."
    # accept returns an open connection between the server and client as well as the address of the client
    # the connection is on a different port assigned by the kernel
    connection, client_address = sock.accept()
    # data is read from the connection with recv() and transmitted with sendall()
    try: # Try, Finally is used so that the connection.close() is always called, even in error
        print "Connection from %s on %s" % client_address
        # Receive the data in small chuncks and send it back
        while True:
            data = connection.recv(16)
            print "Received data: '%s'" % data
            if data:
                print "Sending data back to client..."
                connection.sendall(data)
            else:
                print "No more data from", client_address
                break
    finally:
        # Clean up the connection
        connection.close()
