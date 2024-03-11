import sys, math
input=sys.stdin.readline

N,M=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
b=[]
s=0
    
for i in range(N):
    num=a[i]
    if num==M:
        break
    b.append(M-num)
    s+=M-num

mod=10**9+7
def f(n,x):
    if x==1:
        return n
    elif x==0:
        return 1
    elif x%2==0:
        y=f(n,x//2)
        return (y*y)%mod
    else:
        y=f(n,(x-1)//2)
        return (y*y*n)%mod

if s>M:
    print(0)
else:
    ans=1
    while b:
        z=b.pop()
        c=1
        for i in range(z):
            c=(c*(i+1))%mod
        for i in range(z):
            ans=(ans*(M-i))%mod
        ans=(ans*f(c,mod-2))%mod
        M-=z
    print(ans)                

