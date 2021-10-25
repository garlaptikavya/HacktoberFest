s="10101010000001011110001011001111110001101100011011000101"
k=s[0:8]
l=s[8:16]
r=s[16:]
l1=int(l,2)
s1=""
for i in range(16,len(s),8):
    q=s[i:i+8]
    a= ""
    for i in range(8):
        if (q[i] == k[i]):
            a+= "0"
        else:
            a+= "1"
    b=int(a,2)
    print(b)
    c=chr(b)
    print(c)
    s1=s1+c
print(s1)
