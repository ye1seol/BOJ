import sys
input=sys.stdin.readline

N=int(input())

xp=[]
yp=[]
zp=[]
for i in range(N):
    x,y,z=map(int,input().split())
    xp.append([x,i])
    yp.append([y,i])
    zp.append([z,i])
xp.sort()
yp.sort()
zp.sort()

cost=[]
for l in xp,yp,zp:
    for i in range(1,N):
        p1,c1=l[i-1]
        p2,c2=l[i]
        cost.append([abs(p1-p2),c1,c2])
cost.sort()

parent=[i for i in range(N)]
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
for p in cost:
    if find(p[1])==find(p[2]):
        continue
    else:
        ans+=p[0]
        union(p[1],p[2])

print(ans)