'''
151. Reverse words in a string
'''
def reverseWords(self, s):
    s = s.split()
    l = 0
    r = len(s)-1
    
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return " ".join(s)