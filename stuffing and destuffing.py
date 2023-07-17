
# stuffing and destuffing---------------------------------->>
input_sig=input ('enter your data')
def stuffing_and_destuffing(sig):
    onecount=0
    index=0
    k=0
    one=[]
    flag=['1','1','1','1','1','1']
    destuf_data=[]
    data=list(sig)
    #1st flag 
    for i in range(6):
        data.insert(0,flag[i])
    #at last
    for i in range (6):
        data.insert(len(data),flag[i])
    for i in data [6:len(data)-6]:
        index=index+1
        if i=='1':
            onecount=onecount+1
        else:
            onecount=0
        if onecount==5:
            one.append(index)
            onecount=0
    for i in one :
        data.insert(i+k+6,'0')
        k=k+1
    print ("stuffed data = ","".join(data))
    print ("pos of stuffing =" ,one)
    for i in one:
        data.pop(i+6)
    print ("destuffed data= ","".join(data))
    
    
stuffing_and_destuffing(input_sig)