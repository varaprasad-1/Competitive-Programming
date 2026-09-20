MEMO_SIZE = 1000001
memo = [0] * MEMO_SIZE
memo[1] = 1

def cycle_length(a):
    if a < MEMO_SIZE and memo[a] != 0:
        return memo[a]
    
    if a % 2 == 0:
        next_val = a // 2
    else:
        next_val = a * 3 + 1
        
    result = 1 + cycle_length(next_val)
    
    if a < MEMO_SIZE:
        memo[a] = result
        
    return result

n, m = map(int, input().split())
start = min(n, m)
end = max(n, m)
max_count = 0

for i in range(start, end + 1):
    count = cycle_length(i)
    if count > max_count:
        max_count = count

print(n, m, max_count)
