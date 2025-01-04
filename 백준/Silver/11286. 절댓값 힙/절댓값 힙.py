import sys, heapq
input=sys.stdin.readline

n=int(input())
heap=[]

for _ in range(n):
    a=int(input())
    if a>0:
        heapq.heappush(heap, (a,a))
    elif a<0:
        heapq.heappush(heap, (a*(-1),a))
   
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)