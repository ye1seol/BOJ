import sys
input=sys.stdin.readline

N,M=map(int,input().split())
path=[]
for _ in range(M):
    path.append(list(map(int,input().split())))
path=sorted(path,key=lambda x:x[2])

parent=[i for i in range(N+1)]
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

ans=0
m=0
for p in path:
    if find(p[0])==find(p[1]):
        continue
    else:
        m=max(m,p[2])
        ans+=p[2]
        union(p[0],p[1])

print(ans-m)