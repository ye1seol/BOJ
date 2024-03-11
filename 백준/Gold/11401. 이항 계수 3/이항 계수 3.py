N,K=map(int,input().split())
mod=10**9+7
def f(a,x):
    if x==1:
        return a
    elif x==0:
        return 1
    elif x%2==0:
        y=f(a,x//2)
        return (y*y)%mod
    else:
        y=f(a,(x-1)//2)
        return (y*y*a)%mod
b=1
ans=1
for i in range(K):
    b=(b*(i+1))%mod
for i in range(K):
    ans=(ans*(N-i))%mod
ans=(ans*f(b,mod-2))%mod
print(ans)