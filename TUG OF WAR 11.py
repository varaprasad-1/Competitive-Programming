N = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
k = N // 2

L, R = arr[:N // 2], arr[N // 2:]

def gen(items):
    res = [[] for _ in range(len(items) + 1)]
    res[0].append(0)
    for x in items:
        for c in range(len(items) - 1, -1, -1):
            for s in res[c]:
                res[c + 1].append(s + x)
    return res

def lower_bound(a, target):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo

left = gen(L)
right = gen(R)
for lst in right:
    lst.sort()

best = total
for i in range(len(L) + 1):
    j = k - i
    if j < 0 or j > len(R):
        continue
    rs = right[j]
    for s in left[i]:
        idx = lower_bound(rs, (total + 1) // 2 - s)
        for t in (idx - 1, idx):
            if 0 <= t < len(rs):
                diff = abs(total - 2 * (s + rs[t]))
                if diff < best:
                    best = diff

print(best)
