from collections import defaultdict
def matching(arr):
    Map = defaultdict(lambda:0)
    result = 0
    for i in range(len(arr)):
        Map[arr[i]] += 1
    for i in Map.values():
        if(i >= 2):
            result += i // 2
    return result

n = int(input())
arr = [int(x) for x in input().split()][:n]
print(matching(arr))