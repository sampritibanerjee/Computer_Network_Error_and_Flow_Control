import socket
import random
import time

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234
BUFFER_SIZE = 1024

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

print('Server is listening...')

# Randomly simulate receiver's response
def receiver_response(data):
    if random.randint(0, 1) == int(data):
        return True
    else:
        return False

while True:
    # Receive the packet from the client
    packet, client_address = server_socket.recvfrom(BUFFER_SIZE)
    packet = packet.decode()

    # Split the packet into position and data
    pos, data = packet.split('|')

    # Print the received frame details
    print('Received frame --> pos:', pos, 'data:', data)

    if receiver_response(pos):
        # Receiver acknowledged the frame
        if data == 'end':
            print('Received all frames. Process complete.')
        else:
            ack_packet = str(int(pos) + 1).encode()
            server_socket.sendto(ack_packet, client_address)
            print('Acknowledgment sent for frame', int(pos) + 1)
    else:
        # Receiver didn't acknowledge the frame
        max_retries = 3
        retries = 0

        while retries <= max_retries:
            retries += 1
            print('Acknowledgment not received for frame', pos)
            print('Resending frame --> pos:', pos, 'data:', data)
            print('Waiting...')
            time.sleep(2)
            if retries==3:
                print('max time exit.')
                break
            if receiver_response(pos):
                # Receiver acknowledged the frame
                if data == 'end':
                    print('Received all frames. Process complete.')
                else:
                    ack_packet = str(int(pos) + 1).encode()
                    server_socket.sendto(ack_packet, client_address)
                    print('Acknowledgment sent for frame', int(pos) + 1)
                break

# Close the socket
server_socket.close()
