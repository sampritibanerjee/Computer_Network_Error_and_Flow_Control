import socket

# Client configuration
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
def sender(data, key):
    l = len(key)
    append_data = data + '0' * (l-1)
    remainder = mod2div(append_data, key)
    final_data = data + remainder
    return final_data

# Data and key
data = "11010110110000"
key = "10011"
print("data-->",data)
print("key-->",key)
t_data=sender(data,key)
print("data send by client-->",t_data)
# Concatenate data and key
data_with_key = t_data + ',' + key

# Send the data with key to the server
client_socket.sendto(data_with_key.encode(), (SERVER_HOST, SERVER_PORT))

# Receive the response from the server
response_packet, server_address = client_socket.recvfrom(1024)
response = response_packet.decode()

# Print the response
print("Server Response:", response)

# Close the socket
client_socket.close()
