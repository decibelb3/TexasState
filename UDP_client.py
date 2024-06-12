# Shannon Burns 6-10-24
# UDP_client.py

import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
server_address = ('192.168.86.86', 12345)

# Open the file to be sent
with open('input.txt', 'rb') as f:
    data = f.read(1024)  # Read data in chunks of 1024 bytes
    while data:
        client_socket.sendto(data, server_address)  # Send data to the server
        data = f.read(1024)  # Read next chunk

# Send empty packet to indicate the end of the transmission
client_socket.sendto(b'', server_address)
print("Sent end of transmission packet")

# Wait for the confirmation message from the server
confirmation, _ = client_socket.recvfrom(1024)
print(f"Server confirmation: {confirmation.decode()}")

client_socket.close()
