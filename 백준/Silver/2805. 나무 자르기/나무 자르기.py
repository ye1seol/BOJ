N,M=map(int,input().split())
H=list(map(int,input().split()))
H.sort(reverse=True)
ans=[]

def sum(x):
    ans=0
    for i in H:
        if i > x:
            ans+=i-x
        else:
            break
    return ans

s=0
e=H[0]
while s<e:
    mid=(s+e)//2
    if sum(mid)>M:
        ans.append(mid)
        s=mid+1
    elif sum(mid)<M:
        e=mid
    else:
        ans.append(mid)
        break

ans.sort()
print(ans[-1])