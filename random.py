def even_odd_diff(arr):
    a = 0  
    b = 0  
    for i in range(len(arr)):
        if i % 2 == 0:
            a += arr[i]
        else:
            b += arr[i]

    return a - b


'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
def isPositive(head):
    negative_count = 0
    current = head

    while current:
        if current.data < 0:
            negative_count += 1
        current = current.next

    # Check if the count of negative numbers is even
    if negative_count % 2 == 0:
        return "Yes"
    else:
        return "No"




class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False 
        return sorted(s1) == sorted(s2)


def common(chars1, chars2):
            for c1, c2 in zip(chars1, chars2):
                if c1 and c2: return True
            return False
        chars, ans = [[False]*26 for i in range(len(words))], 0
        for i, word in enumerate(words):
            for ch in word:
                chars[i][ord(ch) - ord('a')] = True
            for j in range(i):
                if not common(chars[i], chars[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
                
