## 151. Reverse words in a string

##### Description:
 - Given an input string `s`, reverse the order of the **words**.
 - A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.
 - Return _a string of the words in reverse order concatenated by a single space._
 - **Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

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


## 238. Product of Array Except Self

##### Description:
- Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.
- You must write an algorithm that runs in `O(n)` time and without using the division operation.

##### Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

##### Solution (beats 100%):
```python
def productExceptSelf(nums):
	n = len(nums)
	leftProduct = [1] * n 
	rightProduct = [1] * n
	result = [0] * n
	# calculate product of everything to the left of the index
	for i in range(1, n-1):
		leftProduct[i] = leftProduct[i-1] * nums[i-1]
	# calculate the product of everything to the right of the index
	for i in range(n-2, -1, -1):
		rightProduct[i] = rightProduct[i+1] * nums[i+1]
	# calculate the product of the left and right
	for i in range(n):
		result[i] = leftProduct[i] * rightProduct[i]
	return result
```

## 334. Increasing Triplet Subsequence

##### Description:
- Given an integer array `nums`, return `true` _if there exists a triple of indices_ `(i, j, k)` _such that_ `i < j < k` _and_ `nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false` 
##### Example 1:
```
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```

##### Solution (beats 100%):
```python
def inscreasingTriplets(nums):
	first = second = float('inf')
	
	for n in nums:
		if n <= first:
			first = n
		elif n <= second:
			second = n
		else:
			return True
	return False
	