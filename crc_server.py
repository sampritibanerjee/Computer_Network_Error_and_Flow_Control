import socket

# Server configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

print('Server is listening...')

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    n = len(divisor)
    tmp = dividend[0 : n]
    while n < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[n]
        else:
            tmp = xor('0'*n, tmp) + dividend[n]
        n += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*n, tmp)
    return tmp
    
def receiver(data, key):
    l = len(key)
    remainder = mod2div(data, key)
    c = 0
    for i in range(len(remainder)):
        if remainder[i] == '0':
            c += 1
    if c == len(remainder):
        return "No error"
    else:
        return "Error found"

while True:
    # Receive the data from the client
    packet, client_address = server_socket.recvfrom(1024)
    received_data = packet.decode()

    # Split the received data into data and key
    data, key = received_data.split(',')

    # Perform error checking
    response = receiver(data, key)

    # Send the response back to the client
    server_socket.sendto(response.encode(), client_address)

# Close the socket
server_socket.close()
