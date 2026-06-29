a=int(input())
l = list(map(int,input().split()))
n=min(l)
m=max(l)
i=l.index(n)
j=l.index(m)
l[i], l[j]=l[j], l[i]
for i in l:
    print(i,end=" ")
#print(*l)

