'''
1768. Merge two strings alternatley
'''
def mergeAlternately(word1, word2):
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

'''
1431. Kids with the Greatest Number of Candies
'''
def kidsWithCandies(candies, extraCandies):
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

'''
605. Can place flowers
'''
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

'''
345. Reverse Vowels in a string
'''
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


'''
283. Move Zeros
'''
def moveZeroes(self, nums):
    l = 0
    r = 1

    while r <= len(nums)-1:
        if (nums[l] == 0 and nums[r] != 0):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
        elif (nums[l] != 0 and nums[r] == 0):
            l += 1
            r += 1
        elif nums[l] == 0 and nums[r] == 0:
            r += 1
        else:
            r += 1
            l += 1
    return nums