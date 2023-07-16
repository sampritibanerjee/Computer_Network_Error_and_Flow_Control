import socket

# Client configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234
BUFFER_SIZE = 1024

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Data to be sent
data = ['0', '0', '1', '1', '1', '1']

# Send each frame to the server
for i in range(len(data)):
    frame_data = data[i]
    frame_packet = str(i) + '|' + frame_data

    # Send the frame to the server
    client_socket.sendto(frame_packet.encode(), (SERVER_HOST, SERVER_PORT))
    print('Sent frame --> pos:', i, 'data:', frame_data)

    # Receive the acknowledgment from the server
    ack_packet, server_address = client_socket.recvfrom(BUFFER_SIZE)
    ack_pos = ack_packet.decode()

    print('Received acknowledgment for frame', ack_pos)

# Send the end signal
end_packet = str(len(data)) + '|' + 'end'
client_socket.sendto(end_packet.encode(), (SERVER_HOST, SERVER_PORT))
print('Sent end signal')

# Close the socket
client_socket.close()
