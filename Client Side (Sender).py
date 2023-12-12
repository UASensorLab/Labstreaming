import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # localhost
port = 12345         # port to connect to

client_socket.connect((host, port))

# Send data to the server
message = "yes! this code is work. nice."
client_socket.send(message.encode())

# Close the connection
client_socket.close()
