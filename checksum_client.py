import socket

# Client configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def checksum_sender(data, k):
    p1 = data[0:k]
    p2 = data[k:k*2]
    p3 = data[2*k:3*k]
    p4 = data[3*k:4*k]

    # Calculate the sum
    total_sum = int(p1, 2) + int(p2, 2) + int(p3, 2) + int(p4, 2)
    sum_binary = bin(total_sum)[2:]

    if len(sum_binary) > k:
        a = len(sum_binary) - k
        sum_binary = bin(int(sum_binary[0:a], 2) + int(sum_binary[a:], 2))
    else:
        a = k-len(sum_binary) 
        sum_binary = a*'0'+sum_binary

    # Calculate the checksum
    checksum = ''.join('0' if bit == '1' else '1' for bit in sum_binary)
    ans = checksum + data

    return ans

# the data and k value
data = "10011001111000100010010010000100"
k = 8
# Perform checksum calculation
checksum = checksum_sender(data, k)
print ("datasending-->",checksum )
# Send the checksum to the server
client_socket.sendto(checksum.encode(), (SERVER_HOST, SERVER_PORT))

# Receive the response from the server
response_packet, server_address = client_socket.recvfrom(1024)
response = response_packet.decode()

# Print the response
print("Server Response:", response)

# Close the socket
client_socket.close()
