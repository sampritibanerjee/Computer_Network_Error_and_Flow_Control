
def xor (a,b):
    result=[]
    for i in range (1,len(b)):
        if a[i]==b[i] :
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
#mod2div 
#  Modulo-2 division
def mod2div(dividend, divisor):
    n = len(divisor)
    #slicing first's bits ofthe dividend into divisor size
    tmp = dividend[0 : n]
    while n < len(dividend):
        #if the first bit of dividend for each time is one the xor and add the next bit 
        #else xor the dividend part with same length '0's string ansd then add the net bit
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[n]
        else: 
            tmp = xor('0'*n, tmp) + dividend[n]
        n += 1
    #this part is when the last xoring left and no next bit for adding
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*n, tmp)
    return tmp
    
def sender(data,key):
    l=len(key)
    append_data=data+'0'*(l-1)
    remainder=mod2div(append_data,key)
    final_data=data+remainder
    return final_data

def receiver(data,key):
    l=len(key)
    remainder=mod2div(data,key)  
    c=0
    for i in range (len(remainder)):
        if remainder[i]=='0':
            c=c+1
    if(c==len(remainder)):
        print("no error")
    else:
        print("error found")
        
data ="11010110110000"
key = "10011"
print("data---->",data)
print("key--->",key)
t_data=sender(data,key)
receiver(t_data,key)