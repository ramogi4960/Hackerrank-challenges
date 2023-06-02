import socket
# we first define the IP and port which are necessary arguments while creating a server or client socket
HOST = "192.168.56.1"
PORT = 9090
# then we create the socket. This is done for both client and server sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# then we specify that the socket is a server socket using the following
server_socket.bind((HOST, PORT))
# we can/should also specify the number of queued messages that can be kept waiting
server_socket.listen(5)
# we have now successfully created a server socket above that's binded to a specific HOST and PORT
# we can now proceed to make it available to accept messages from clients

while True:
    connection_socket, address = server_socket.accept()
    # the accept() method produces a socket for accepting client messages and the address of the client
    print(f"We have successfully connected to {address}")  # just to show that the connection took place
    # now we need to make the connection_socket receive messages a message from the client using the recv() method
    message = connection_socket.recv(1024).decode("utf-8")
    # we have now created a message variable that stores the received message that comes with a maximum of 1024bytes,
    # and the bytes received are further decoded to readable string as a utf-8
    print(f"The message received by the client is: \n {message}")
    # after receiving the message from the client, we would like to send a confirmation message to the client
    reply = input("Enter the reply message:\n")
    connection_socket.send(f"{reply}".encode("utf-8"))
    print("The connection has ended after sending a confirmation message")
    connection_socket.close()
