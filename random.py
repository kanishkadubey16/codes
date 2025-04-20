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



# search pattern 
class Solution:
    def constructLps(self, pat, lps):
        l = 0
        m = len(pat)
        lps[0] = 0
        i = 1
        while i < m:
            if pat[i] == pat[l]:
                l+=1
                lps[i] = l 
                i+=1
            else:
                if l != 0:
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i+=1
    def search(self, pat, txt):
        n = len(txt)
        m = len(pat)
        lps = [0] * m
        result = []
        self.constructLps(pat,lps)
        i = 0
        j = 0
        while i < n:
            if txt[i] == pat[j]:
                i+=1
                j+=1
                if j == m:
                    result.append(i-j)
                    j = lps[j-1]
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i+=1
        return result


# string questions 
class Solution:
    def minChar(self, s):
        rev_s = s[::-1]
        ans = s+"#"+rev_s
        l = [0] * len(ans)
        length = 0
        i = 1
        while i <len(ans):
            if ans[i] == ans[length]:
                length += 1
                l[i] = length 
                i += 1
            else:
                if length != 0:
                    length = l[length -1 ]
                else:
                    l[i] = 0
                    i+=1
        return len(s) - l[-1]


def areRotations(self,s1,s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)


class Solution:
    def sort012(self, arr):
        # Count 0s, 1s, and 2s
        c0 = arr.count(0)
        c1 = arr.count(1)
        c2 = arr.count(2)

        # Overwrite the array directly using slicing
        arr[:c0] = [0] * c0
        arr[c0:c0 + c1] = [1] * c1
        arr[c0 + c1:] = [2] * c2
            
