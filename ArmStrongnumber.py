n=153
num = n
nod=len(str(num))
total=0
while num>0:
    ld=num%10
    total=total+(ld*nod)
    num//=10
return total==n