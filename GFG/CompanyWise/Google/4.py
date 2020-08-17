#Maximum array index difference
'''
#####Method 1 O(n^2)
def MaxDiff(arr):
    stk = []
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if(arr[i] <= arr[j]):
                diff = j-i
                stk.append(diff)
    return (max(stk))
'''
def MaxDiff(arr):
    lmin = [0]*len(arr)
    rmin = [0]*len(arr)
    lmin[0] = arr[0]
    rmin[n-1] = arr[n-1]
    for i in range(1,len(arr)):
        lmin[i] = min(arr[i], lmin[i-1])

    for j in range(len(arr)-2,-1,-1):
        rmin[j] = max(arr[j], rmin[j+1])

    diff = -1
    x = 0
    y = 0
    while(x < len(arr) and y < len(arr)):
        if(lmin[x] < rmin[y]):
            diff = max(diff, y-x)
            y = y+1
        else:
            x = x+1
    return diff

    

t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()][:n]
    print(MaxDiff(arr))
