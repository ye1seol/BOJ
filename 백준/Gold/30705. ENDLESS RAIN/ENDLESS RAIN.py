import sys
input=sys.stdin.readline
N,M=map(int,input().split())
cnt=0
ans=0

parent = [i for i in range(N+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

for _ in range(M):
    cnt+=1
    need=0
    a,b=map(int,input().split())
    A=find(a)
    B=find(b)
    while A<B:
        need+=1
        parent[B]=A
        B=find(B-1)

    if need>cnt:
        ans+=need-cnt
        cnt=0
    else:
        cnt-=need

print(ans)