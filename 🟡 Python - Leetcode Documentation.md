## 151. Reverse words in a string

##### Description:
Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return _a string of the words in reverse order concatenated by a single space._

**Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

##### Example 1:
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

##### Solution (beats 100%):
```python
class Solution(object):
	def reverseWords(self, s):
		s = s.split()
		l = 0
		r = len(s)-1
		
		while l < r:
			s[l], s[r] = s[r], s[l]
			l += 1
			r -= 1
		return " ".join(s)
```