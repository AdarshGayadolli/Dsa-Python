# prestoring the values into some datastructure like list/dictionary/sets and then fectching it
n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
for num in m:
    count=0
    for x in n:
        if num==x:
            count+=1
    print(count)