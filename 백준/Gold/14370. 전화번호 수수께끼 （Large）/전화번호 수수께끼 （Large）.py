n=int(input())
def f(x):
    if x=='Z':
        num[0]+=1
    elif x=='W':
        num[2]+=1
    elif x=='U':
        num[4]+=1
    elif x=='X':
        num[6]+=1
    elif x=='G':
        num[8]+=1

    elif x=='O':
        num[1]+=1
    elif x=='H':
        num[3]+=1
    elif x=='F':
        num[5]+=1
    elif x=='S':
        num[7]+=1
    elif x=='I':
        num[9]+=1
    return

for t in range(n):
    e=list(input())
    num=[0]*(10)
    for i in e:
        f(i)
    num[1]=num[1]-num[0]-num[2]-num[4]
    num[3]-=num[8]
    num[5]-=num[4]
    num[7]-=num[6]
    num[9]=num[9]-num[5]-num[6]-num[8]

    print('Case #{0}: '.format(t+1),end='')
    for i in range(10):
        a=num[i]
        if a!=0:
            for _ in range(a):
                print(i,end='')
    print()