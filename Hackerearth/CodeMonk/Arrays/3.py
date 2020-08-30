#Minimum xor of AND and OR
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()][:n]
    new = []
    arr.sort()
    for i in range(0,len(arr)-1):
        res = ((arr[i] ^ arr[i+1]))
        new.append(res)
    print(min(new))

