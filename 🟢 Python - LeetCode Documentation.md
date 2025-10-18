## 1768. Merge Strings Alternately 

#### Description:
- You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.
- Return _the merged string._

##### Example 1:
```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:

word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

##### Solution (beats 10%):
```python
class Solution(object):
	def mergeAlternately(self, word1, word2):
		result = ""
		for i in range(min(len(word1), len(word2))):
			result += ''.join(word1[i] + word2[i])
		
		if len(word1) < len(word2):
			result += ''.join(word2[len(word1):])
		elif len(word2) < len(word1):
			result += ''.join(word1[len(word2):])
		else:
			return result
	return result
```

## 1431. Kids with the Greatest Number of Candies

##### Description:
- There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `ith` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.
- Return _a boolean array_ `result` _of length_ `n`_, where_ `result[i]` _is_ `true` _if, after giving the_ `ith` _kid all the_ `extraCandies`_, they will have the **greatest** number of candies among all the kids__, or_ `false` _otherwise_.
- ***Note***:  **multiple** kids can have the **greatest** number of candies.

##### Example:
```
Input: candies = [2,3,5,1,3], extraCandies = 3
Output:[true,true,true,false,true] 
Explanation: If you give all extraCandies to:
	- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
	- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
	- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
	- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
	- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
```

##### Solution (Beats 100%):
```python
class Solution(object):

	def kidsWithCandies(self, candies, extraCandies):
		max_candies = 0
		# check for max number of candies in the list
		for i in range(len(candies)):
			if max_candies <= candies[i]:
				max_candies = candies[i]
			else:
				continue
		
		result = []
		# check to see if adding candies makes them have the max
		# append to result 'True' if they do, 'False' otherwise
		for j in range(len(candies)):
			if max_candies <= (candies[j] + extraCandies):
				result.append(True)
			else:
				result.append(False)
		
		return result
```

## 605. Can Place Flowers

##### Description:
- You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in **adjacent** plots.
- Given an integer array `flowerbed` containing `0`'s and `1`'s, where `0` means empty and `1` means not empty, and an integer `n`, return `true` _if_ `n` _new flowers can be planted in the_ `flowerbed` _without violating the no-adjacent-flowers rule and_ `false` _otherwise_.

##### Example:
```
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

##### Solution (Beats 51%):
```python
class Solution(object):
	def canPlaceFlowers(self, flowerbed, n):
		planted = 0
		
		# check all the flowerbeds, if 1, continue
		# if 0, check neighbours (account for end caces)
		for i in range(len(flowerbed)):
			if flowerbed[i] == 1:
				continue
			else:
				left = (i == 0) or (flowerbed[i-1] == 0)
				right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
				
		# if left and right are both free, "plant" a flower + account for it	 
		if left and right:
			flowerbed[i] = 1
			planted += 1
			if planted == n: # auto stop if planted equal to n
				return True 
	# if the number planted is greater or equal to n, return true			 
	return planted >= n
```
## 345. Reverse Vowels in a string
##### Description: 
- Given a string s, reverse only all the vowels in the string and return it.
-  The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

##### Example 1:
```
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
```

##### Solution (beats 60%):
```python
class Solution(object):

	def reverseVowels(self, s):
		vowels="aeiouAEIOU" # list of values
		s = list(s) # string s turned into a list (STRUGGLE)
		
		i = 0 # pointer 1 (start)
		j = len(s)-1  # pointer 2 (end)
		
		# if the pointers meet, whole word is searched
		while i < j:
			# if they are both vowels, swap them
			if s[i] in vowels and s[j] in vowels:
				s[i], s[j] = s[j], s[i]
				i += 1
				j -= 1
			# if first pointer is a vowel, but second pointer isnt, 
			# move the second pointer -1 positions
			elif s[i] in vowels:
				j -= 1
			# if the second pointer is a vowel, but not first, move first pointer
			# +1 positions
			elif s[j] in vowels:
				i += 1
			# both not vowels, move both pointers
			else:
				i += 1
				j -= 1
		return "".join(s) # add the list of s to an empty string using join
```

