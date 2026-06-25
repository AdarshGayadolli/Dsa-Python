A=[[1,2,3],
   [3,2,1],
   [1,2,3]]

B=[[1,2,3,4],
   [4,3,2,1],
   [4,4,2,2]]

result=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result [i][j]+=A[i][k]*B[k][j]
# print(result)

for i in result:
    print(i)