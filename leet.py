s = "  hello world  "

s = s.split()
print(s)
for l in range(len(s)):
    r = len(s)-1
    s[l], s[r] = s[r], s[l]
    r -= 1

print(s)


