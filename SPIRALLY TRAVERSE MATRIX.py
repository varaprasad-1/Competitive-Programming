N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

top, bottom = 0, N - 1
left, right = 0, M - 1
res = []

while top <= bottom and left <= right:
    for j in range(left, right + 1):
        res.append(mat[top][j])
    top += 1

    for i in range(top, bottom + 1):
        res.append(mat[i][right])
    right -= 1

    if top <= bottom:
        for j in range(right, left - 1, -1):
            res.append(mat[bottom][j])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            res.append(mat[i][left])
        left += 1

print(" ".join(map(str, res)))
