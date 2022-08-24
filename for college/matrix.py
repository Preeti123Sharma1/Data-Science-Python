# multiplication of two matrix

A = [[3, 2, 1],
    [5, 4, 3],
    [1, 2, 3]]

B = [[1, 2, 1],
    [2, 0, 2],
    [1, 0, 1]]

C = [[0, 0, 0],
    [0, 0, 0], 
    [0, 0,0]]    

# loop for row
for i in range(0, len(C)):
    # loop for column 
    for j in range(0, len(C[0])):
        # loop for sum of i,j which is number of row in B
        for k in range (0, len(C)):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)