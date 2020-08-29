#Monk and inversion of matrix

t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    for k in range(n):
        arr.append(list(map(int, input().strip().split())))
    index_mat1 = []
    index_mat2 = []
    count = 0
    for i in range(n):
        for j in range(n):
            index_mat1.append((i,j))
            index_mat2.append((i,j))

    for i,j in index_mat1:
        for p,q in index_mat2:
            if i <= p and j <= q:
                if arr[i][j] > arr[p][q]:
                    count += 1

    print(count)


