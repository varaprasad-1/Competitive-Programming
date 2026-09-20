s = input()

dup = 0
op = []
printed = 0

for c in s:
    shift = ord(c) - 97
    bit = 1 << shift
    
    if dup & bit :
        if not printed & bit:
            op.append(c)
            printed |= bit
    else:
        dup |= bit

if op == "":
    print("No duplicates")
else:
    print(" ".join(op))
