n,t=map(int,input().split(" "))
arr=list(map(int,input().split(" ")))
lst=[]
for i in arr:
    if(i%9!=0):
        lst.append((i%9))
    else:
        lst.append(9)
lst=sorted(lst)
l1=lst[:]
l2=lst[:]
for i in range(1,n):
    l1[i]+=l1[i-1]
for i in range(n-2,-1,-1):
    l2[i]+=l2[i+1]
for _ in range(t):
    q,k=map(int,input().split(" "))
    if(q==1):
        print(l2[-k])
    else:
        print(l1[(k-1)])