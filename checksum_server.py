import socket

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Set the socket to blocking mode
server_socket.setblocking(True)

print('Server is listening...')
k=8
def checksum_receiver(checksum, k):
    p1 = checksum[0:k]
    p2 = checksum[k:k*2]
    p3 = checksum[2*k:3*k]
    p4 = checksum[3*k:4*k]
    p5 = checksum[4*k:5*k]

    # Calculate the sum
    total_sum = int(p1, 2) + int(p2, 2) + int(p3, 2) + int(p4, 2) + int(p5, 2)
    sum_binary = bin(total_sum)[2:]

    if len(sum_binary) > k:
        a = len(sum_binary) - k
        sum_binary = bin(int(sum_binary[0:a], 2) + int(sum_binary[a:], 2))[2:]
    else:
        a = k-len(sum_binary) 
        sum_binary = a*'0'+sum_binary

    # Calculate the received checksum
    received_checksum = ''.join('0' if bit == '1' else '1' for bit in sum_binary)

    return received_checksum

while True:
    try:
        # Receive the data from the client
        packet, client_address = server_socket.recvfrom(1024)
        received_data = packet.decode()

        # Perform checksum validation
        received_checksum = checksum_receiver(received_data, k)
        print ("reciver_checksum-->",received_checksum )
        if int(received_checksum, 2) == 0:
            response = "No error"
        else:
            response = "Error present"

        # Send the response back to the client
        server_socket.sendto(response.encode(), client_address)

    except BlockingIOError:
        continue

# Close the socket
server_socket.close()
