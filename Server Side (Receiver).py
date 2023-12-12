import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '127.0.0.1'  # localhost
port = 12345         # port to bind to

server_socket.bind((host, port))

# Listen for incoming connections (max 5 clients in the queue)
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

# Accept connection from client
client_socket, addr = server_socket.accept()
print(f"Got connection from {addr}")

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")

# Close the connection
client_socket.close()
server_socket.close()
# Write your code here :-)
