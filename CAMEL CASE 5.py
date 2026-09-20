n = int(input())
words = input().strip().split(',')
pattern = input().strip()

matches = []

for word in words:
    abbr = ''.join(c for c in word if c.isupper())
    if abbr.startswith(pattern):
        matches.append((abbr, word))

matches.sort()

if matches:
    for _, word in matches:
        print(word)
else:
    print("No match found")
