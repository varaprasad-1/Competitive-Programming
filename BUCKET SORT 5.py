n = int(input())
arr = list(map(float, input().split()))

buckets = [[] for _ in range(n)]

for num in arr:
    index = int(num * n)
    buckets[index].append(num)

for bucket in buckets:
    bucket.sort()

result = []
for bucket in buckets:
    result.extend(bucket)

print(*["{:.2f}".format(x) for x in result])



