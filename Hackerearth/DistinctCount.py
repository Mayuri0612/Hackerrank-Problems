t = int(input() )
for _ in range(t):
    n,x = map(int, input().strip().split())
    arr = set(input().strip().split())
    if(len(arr) == x):
        print('Good')
    elif(len(arr) < x):
        print('Bad')
    else:
        print('Average')
