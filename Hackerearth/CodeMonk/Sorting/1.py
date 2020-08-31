#monk and nice string

n = int(input())
arr = []
count = 0
for i in range(0,n):
    arr.append(input())

for i in range(0,n):
    for j in range(i):
        if (i is not j and arr[j].lower() < arr[i].lower()):
            count += 1
    print(count)
    count = 0
