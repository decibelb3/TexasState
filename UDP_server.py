# Shannon Burns 6-10-24
# UDP_server.py

import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.86.86', 12345)  # Listen on all available interfaces on port 12345
server_socket.bind(server_address)

# Print waiting message to screen
print("UDP Server is waiting for data")

# Open a file to write the received data
with open('received_input.txt', 'wb') as f:
    while True:
        data, addr = server_socket.recvfrom(1024)  # Receive data in chunks of 1024 bytes
        if not data:
            break  # No more data, break the loop
        f.write(data)  # Write data to file

# Send confirmation message back to the client
server_socket.sendto(b"File received successfully", addr)
server_socket.close()
