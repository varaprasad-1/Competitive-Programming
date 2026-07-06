n=int(input())
a=list(map(int,input().split()))

 # this loop is to check whether there are any negative numbers in the starting of the list, so we can skip them
i=0
for i in range(0,len(a)):
    if a[i]>0:
        break
sum=0
for j in range(i,len(a)):
    if j==len(a)-1: 
        if a[j]<0:  #if the last element is negative, we can skip it
            break
        else:
            sum+=a[j] #if the last element is positive, we can add it
            break
    else:
        if a[j]<0:   #if any element is negative and
            if a[j+1]>(-a[j]): # if the next element is larger than the positive value of that negative element we can add it
                sum+=a[j]
            else:
                break #else we can stop adding and stop checking the list
        else:
            sum+=a[j]
print(sum)
