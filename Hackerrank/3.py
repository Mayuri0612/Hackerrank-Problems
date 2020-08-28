#BST Shortest path reach

def BFS(ad_list,N,S):
    dist=[-1 for x in range(N)]
    visited=[False for x in range(N)]
    Q=[S]
    depth=1
    dist[S]=0
    while Q:
        if not visited[Q[0]]:
            for x in ad_list[Q[0]]:
                if dist[x] == -1: dist[x]=dist[Q[0]]+6
                else: dist[x]=min(dist[x],dist[Q[0]]+6)
                Q.append(x)
            visited[Q[0]]=True
        del Q[0]
    del dist[S]
    for x in dist: print(x,end=' ')
    print()

T=int(input())
for _ in range(T):
    N,M=(int(x) for x in input().split())
    ad_list =[set() for x in range(N)]
    for i in range(M):
        X,Y=(int(x)-1 for x in input().split())
        ad_list[X].add(Y)
        ad_list[Y].add(X)
    BFS(ad_list,N,int(input())-1)

    




