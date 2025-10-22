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


'''
238. Product of Array, Except Self
'''
def productExceptSelf(nums):
    n = len(nums)
    leftProduct = [1] * n
    rightProduct = [1] * n
    result = [0] * n

    for i in range(1, n-1):
        leftProduct[i] = leftProduct[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        rightProduct[i] = rightProduct[i+1] * nums[i+1]

    for i in range(n):
        result[i] = leftProduct[i] * rightProduct[i]
    return result

'''
344. Increasing Triplet Subsequence
'''
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