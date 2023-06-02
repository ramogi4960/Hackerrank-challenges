import socket
# we first define the IP and port which are necessary arguments while creating a server or client socket
HOST = "192.168.56.1"
PORT = 9090
# then we create the socket. This is done for both client and server sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# then we specify that the socket created is a client socket
client_socket.connect((HOST, PORT))
text = input("Enter text to send:\n") # message to send when I run the client.py
client_socket.send(f"{text}".encode("utf-8")) # sending the encoded message to the client
print(client_socket.recv(1024).decode("utf-8")) # printing any message received from the serve.py
