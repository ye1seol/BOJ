import sys

input = sys.stdin.readline
INF=10**10
N,M=map(int,input().split())
road=[]

for _ in range(M):
    a,b,c=map(int,input().split())
    road.append((a,b,c))

dis=[INF]*(N+1)
dis[1]=0
ans=0

for i in range(1, N + 1):
    for j in range(M):
        start, end, cost = road[j]
        if dis[start]!=INF and dis[end]>dis[start]+cost:
            dis[end]=dis[start]+cost
            if i==N:
                ans=1
                break


if ans==1:
    print(-1)
else:
    for i in range(2,N+1):
        if dis[i]==INF:
            print(-1)
        else:
            print(dis[i])
