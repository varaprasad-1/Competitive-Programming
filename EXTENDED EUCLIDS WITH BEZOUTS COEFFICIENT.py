A, B = map(int, input().split())

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


g, x0, y0 = extended_gcd(A, B)

kx = B // g
ky = A // g

candidates = set()

for k in range(-2, 3):
    x = x0 + k * kx
    y = y0 - k * ky
    candidates.add((x, y))

best = min(candidates, key=lambda p: (abs(p[0]) + abs(p[1]), p[0] > p[1], p[0]))

print(best[0], best[1], g)
