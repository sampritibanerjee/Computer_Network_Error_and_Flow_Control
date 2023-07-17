data = "10011001111000100010010010000100"
k = 8
def checksum_sender(data,k):
    p1=data[0:k]
    p2=data[k:k*2]
    p3=data[2*k:3*k]
    p4=data[3*k:4*k]
    
    sum= bin(int(p1,2)+int(p2,2)+int(p3,2)+int(p4,2))
    if(len(sum)>k):
        a= len(sum)-k
        # print(a)
        sum=bin(int(sum[0:a],2) +int(sum[a:],2))
        # print('sum',sum)
    
    else:
        sum= k-len(sum)*'0' + sum
    Checksum = ''
    for i in sum:
        if(i == '1'):
            Checksum += '0'
        else:
            Checksum += '1'
    
    print ("checksum",Checksum )
    ans=Checksum+data
    return ans
checksum=checksum_sender(data,k)
print ("check sum ------->", checksum)
def checksum_reciver(checksum,k):
    p1=checksum[0:k]
    p2=checksum[k:k*2]
    p3=checksum[2*k:3*k]
    p4=checksum[3*k:4*k]
    p5=checksum[4*k:5*k]
    sum2= bin(int(p1,2)+int(p2,2)+int(p3,2)+int(p4,2) + int (p5,2))[2:]
    if(len(sum2)>k):
        a = len(sum2)-k
        # print(a)
        sum2=bin(int(sum2[0:a],2) +int(sum2[a:],2))[2:]
        # print(sum2)
    
    else:
        a=k-len(sum2)
        sum2= a*"0"+sum2
    recive_sum = ''
    for i in sum2:
        if(i == '1'):
            recive_sum += '0'
        else:
            recive_sum += '1'
    
    return recive_sum
    
reciver_data=checksum_reciver(checksum,k)
print("reciver data with out error--------->",reciver_data)
if (int(reciver_data,2)==0):
    print("no error")

else:
    print("error present")
with_error_checksum='1101101010011001111000100010011111111100'
error_reciver_data=checksum_reciver(with_error_checksum,k)
print("reciver data with  error--------->",error_reciver_data)
if (int(error_reciver_data,2)==0):
    print("no error")

else:
    print("error present")