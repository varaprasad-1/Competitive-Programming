n=int(input())
a=list(map(int,input().split()))

s=a[0]
maxsum=a[0]
for i in range(1,n):
    if a[i]>a[i-1]:
        s+=a[i]
    else:
        if maxsum < s:
            maxsum=s
        s=a[i]
if s>maxsum:
    maxsum=s
print(maxsum)
