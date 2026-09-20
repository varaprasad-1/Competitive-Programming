s = input()
l = len(s)

for i in range(l):
    no_of_times = l // (i+1) 
# here no_of_times is that no of times the substring should be repeated to form the string, it is used to check whether it forms the string or not
    
    if s[:i+1] * no_of_times == s:
        print(i+1)
        break
