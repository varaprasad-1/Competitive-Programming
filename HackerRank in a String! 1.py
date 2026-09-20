
for _ in range(int(input())):
    s = input()
    t = "hackerrank"
    j = 0 # pointer to traverse hackerrank
    for i in s:
        if j < 10:
            if t[j] == i:
                j += 1
    if j == 9:
        print("YES")
    else:
        print("NO")
