# when input is given and add two matrix

A = [[1, 2, 3],
    [2, 1, 3],
    [2, 0, 0]]

B = [[0, 2, 1],
    [8, 9, 5],
    [0, 5, 0]]    

C = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

for i in range(0,len(C)):
    for j in range(0, len(C[0])):
        C[i][j] = A[i][j] + B[i][j]

for row in C:
    print(row)        

print(C.ndim)    
