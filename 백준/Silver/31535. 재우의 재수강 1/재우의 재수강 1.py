import sys
input=sys.stdin.readline

w,h=map(int,input().split())
n,d=map(int,input().split())
a=[0]+list(map(int,input().split()))
p=list(map(float,input().split()))

def find(x):
    start=0
    end=len(a)-1
    while start<=end:
        mid=(start+end)//2
        if x==a[mid]:
            return mid
        elif x>a[mid]:
            start=mid+1
        else:
            end=mid-1
    return end

if n==1:
    print(int(p[0]*(w+d)))
elif a[-2]<=d:
    row=p[-1]*w
    l=0
    for i in range(1,n):
        l+=(a[i]-a[i-1])*p[i-1]
    l+=(d-a[n-1])*p[n-1]
    print(int(row+l))
else:
    x=find(d)
    under=p[x]*(w+d-a[x])
    for i in range(1,x+1):
        under+=(a[i]-a[i-1])*p[i-1]
    ans=under
    up=under+(a[x+1]-a[x])*p[x]-p[x]*(w+d-a[x])+p[x+1]*(w)+p[x]*(a[x+1]-d)
    ans=min(up,ans)
    x+=1
    while x+1<n:
        up+=w*(p[x+1]-p[x])+2*(a[x+1]-a[x])*p[x]
        ans=min(up,ans)
        x+=1
    print(int(ans))
