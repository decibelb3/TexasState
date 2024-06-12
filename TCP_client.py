#Shannon Burns
#6-10-2024
import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's port
server_address = ('192.168.86.86', 12345)
client_socket.connect(server_address)

try:
    # Open the file to be sent
    with open('input.txt', 'rb') as f:
        # Send file data to the server in chunks
        chunk = f.read(1024)
        while chunk:
            client_socket.send(chunk)
            chunk = f.read(1024)

    # Wait for the confirmation message from the server
    confirmation = client_socket.recv(1024)
    print(f"Server confirmation: {confirmation.decode()}")

finally:
    # Close the socket
    client_socket.close()
