t = int(input())
for test in range(t):
    n = int(input())
    arr = [int(n) for n in input().split()]
    pairs = {}
    for i in arr:
        if i not in pairs:
            pairs[i] = 1
        else:
            del pairs[i]
    nums = [n for n in pairs.keys()]
    nums.sort()
    print('\n'.join(nums))
