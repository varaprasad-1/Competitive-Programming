n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

for i in b:
    a.append(i)

for i in range(0,n+m-2):
    for j in range(i,n+m-1):
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]
print(*a)

