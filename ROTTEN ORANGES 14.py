def rottenOranges(grid, n, m):
    queue = []
    fresh = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    front = 0
    time = 0

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while front < len(queue):
        i, j, t = queue[front]
        front += 1

        time = max(time, t)

        for di, dj in directions:
            ni = i + di
            nj = j + dj

            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh -= 1
                queue.append((ni, nj, t + 1))

    if fresh > 0:
        return -1

    return time


n, m = map(int, input().split())

grid = []

for i in range(n):
    grid.append(list(map(int, input().split())))

print(rottenOranges(grid, n, m))
