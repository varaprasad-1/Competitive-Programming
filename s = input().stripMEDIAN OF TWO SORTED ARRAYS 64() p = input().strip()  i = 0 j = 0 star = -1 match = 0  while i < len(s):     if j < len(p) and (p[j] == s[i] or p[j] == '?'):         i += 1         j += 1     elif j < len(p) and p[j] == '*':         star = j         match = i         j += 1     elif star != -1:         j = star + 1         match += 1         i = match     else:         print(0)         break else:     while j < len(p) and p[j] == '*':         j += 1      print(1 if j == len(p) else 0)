n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.extend(b)
l=len(a)
for i in range(0,l-1):
    for j in range(i+1,l):
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]
median = (a[l//2]+a[l//2-1])/2 if l%2==0 else a[l//2]
if median == int(median):
    print(int(median))
else:
    print(median)
