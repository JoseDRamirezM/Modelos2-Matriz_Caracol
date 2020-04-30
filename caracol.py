n = 3
posi = 0
matriz = [[1,2,3],[4,5,6], [7,8,9]]

for i in range (0,n):
    if(posi == 0):
        for j in range (0, n):
            print (str(matriz[i][j]))
        posi = 1
    elif(posi == 1):
        for j in range (1, n):
           print (str(matriz[j][i+1]))
        posi = 2
    elif(posi == 2):
        for k in range (n-1, 0, -1):
            print (str(matriz[j][k-1]))
        print (str(matriz[k][k-1]))
        print (str(matriz[k][k]))

