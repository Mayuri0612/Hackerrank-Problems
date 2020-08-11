arr = []
size = input()
for i in range(int(size)):
    n = input()
    arr.append(int(n))

for i in range(len(arr)-1, -1, -1):
    print(arr[i])
