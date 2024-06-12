# Shannon Burns 6-10-24
# TCP_server.py

import socket
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.86.86', 12345)  # Listen on all available interfaces on port 12345
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("TCP Server is waiting for a connection")

# Wait for a connection
conn, addr = server_socket.accept()
try:
    print(f"Connection from {addr}")

    # Open a file to write the received data
    with open('received_input.txt', 'wb') as f:
        while True:
            data = conn.recv(1024)  # Receive data in chunks of 1024 bytes
            if not data:
                break  # No more data from client, break the loop
            f.write(data)  # Write data to file

    # Send confirmation message back to the client
    conn.sendall(b"File received successfully")
    
finally:
    # Clean up the connection
    conn.close()
    server_socket.close()
