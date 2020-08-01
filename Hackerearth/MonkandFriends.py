t = int(input())
for _ in range(t):
    # M= no. of students already N = number of students more to come
    m,n = map(int, input().split())
    # to give m + n spaced integers
    arr1 = list(input().split())
    # keep first m values in a separate set
    arr2 = set(arr1[:m])
    ls = []
    for num in arr1[m:]:
        if num in arr2:
            ls.append('YES')
        else:
            ls.append('NO')
            arr2.add(num)
    print('\n'.join(ls))