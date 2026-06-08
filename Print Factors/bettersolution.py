def adarsh(num):
    result=[]
    for i in range(1,(num//2)+1):
        if num%i==0:
            result.append(i)
    result.append(num)
    return result

print(adarsh(67)) 