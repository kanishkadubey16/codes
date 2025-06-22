def even_odd_diff(arr):
    a = 0  
    b = 0  
    for i in range(len(arr)):
        if i % 2 == 0:
            a += arr[i]
        else:
            b += arr[i]

    return a - b




class Solution:
    def maxWater(self, arr):
        a = len(arr)
        if a <= 2:
            return 0 
        b = [0] * a 
        c = [0] * a 
        b[0] = arr[0]
        for d in range(1,a):
            b[d] = max(b[d-1],arr[d])
        c[a-1] = arr[a-1]
        for d in range(a-2,-1,-1):
            c[d] = max(c[d+1],arr[d])
        e = 0 
        for d in range(a):
            f = min(b[d],c[d]) - arr[d]
            if f > 0:
                e += f 
        return e



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


# trees question 
'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def is_identical(root1, root2):
    #base case 
    if root1 == None and root2 == None:
        return True 
    
    #false cases 
    if root1 != None and root2 == None:
        return False 

    if root1 == None and root2 != None:
        return False 

    if root1.val != root2.val:
        return False 

    left = is_identical(root1.left,root2.left)
    right = is_identical(root1.right,root2.right)

    return left and right




class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        inserted = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                    inserted = True 
                result.append(interval)
            else:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
        if not inserted:
            result.append(newInterval)
        return result


class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        inserted = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                    inserted = True 
                result.append(interval)
            else:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
        if not inserted:
            result.append(newInterval)
        return result

sorted_nums = sorted(nums)
        res = 0
        n = len(nums)

        for idx in range(0, n, 2):
            res += sorted_nums[idx]
        
        return res



c = Counter(s)
        return len(set(c.values())) == 1

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



def even_sum(arr):
    e = 0
    for i in range(len(arr)):
        if i % 2 == 0:  
            e += arr[i] 
    return e


class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        def canplace(d):
            cows,last = 1,stalls[0]
            for pos in stalls[1:]:
                if pos-last >= d:
                    cows += 1 
                    last = pos 
                    if cows == k:
                        return True
            return False 
        l,h = 1,stalls[-1]-stalls[0]
        res = 0
        while l <= h:
            mid = (l+h)//2 
            if canplace(mid):
                res = mid 
                l = mid+1 
            else:
                h = mid-1
        return res



def odd_sum(arr):
    odd = 0
    for i in range(len(arr)):
        if i % 2 == 1:
            odd += arr[i]
    return odd

def maxSubArray(nums):
    # Initialize both res and current sum (ans) to the first element
    res = nums[0]
    ans = nums[0]

    # Start from the second element and go through the list
    for i in range(1, len(nums)):
        # Either start a new subarray from current element or extend the previous subarray
        ans = max(nums[i], ans + nums[i])
        # Update the maximum sum found so far
        res = max(res, ans)

    return res

# Input handling
N = int(input())  # Size of the array
arr = list(map(int, input().split()))  # Array elements

# Call the function and print the result
print(maxSubArray(arr))



'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def swap_values(root, num1, num2):
    node1 = None
    node2 = None
    def dfs(node):
        nonlocal node1, node2  
        if not node:
            return
        if node.val == num1:
            node1 = node
        if node.val == num2:
            node2 = node
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    if node1 and node2:
        node1.val, node2.val = node2.val, node1.val

    return root



stack = []  
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)



class Solution:
	def twoSum(self, arr, target):
	    seen = set()
	    for i in arr:
	        if target - i in seen:
	            return True 
            seen.add(i)
        return False


class Solution:
    def findTriplets(self, arr):
        size = len(arr)
        triplets = []

        # Step 1: Map each value to all its positions (indexes)
        value_to_indexes = {}
        for pos in range(size):
            value = arr[pos]
            if value not in value_to_indexes:
                value_to_indexes[value] = []
            value_to_indexes[value].append(pos)

        # Step 2: Try every pair of elements (first and second)
        for first in range(size - 2):
            for second in range(first + 1, size - 1):
                # Calculate the third value needed to make the sum 0
                third_value = -(arr[first] + arr[second])

                # Check if this third_value exists in the array
                if third_value in value_to_indexes:
                    for third in value_to_indexes[third_value]:
                        # Make sure index order is correct: first < second < third
                        if third > second:
                            triplets.append([first, second, third])

        return triplets

n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))


top = 0
bottom = n - 1
left = 0
right = m - 1


result = []


while top <= bottom and left <= right:


    for i in range(left, right + 1):
        result.append(mat[top][i])
    top += 1


    for i in range(top, bottom + 1):
        result.append(mat[i][right])
    right -= 1


    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(mat[bottom][i])
        bottom -= 1


    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(mat[i][left])
        left += 1


print(*result)


class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        d = set()
        for i in a:
            d.add(i)
        for i in b:
            d.add(i)
        return len(d)


def longestConsecutive(self,arr):
        num = set(arr)
        longest = 0
        for i in arr:
            if i-1 not in num:
                current = i
                c= 1
                while current + 1 in num:
                    current += 1
                    c += 1
                longest = max(longest,c)
        return longest

class Solution:

    def anagrams(self, arr):
        from collections import defaultdict
        anagram_map = defaultdict(list)
        for word in arr:
            key = "".join(sorted(word))
            anagram_map[key].append(word)
        return list(anagram_map.values())

class Solution:
    def countSubarrays(self, arr, k):
        p = {0:1}
        curr = 0
        c= 0
        for i in arr:
            curr += i
            if (curr - k) in p:
                c += p[curr - k]
            if curr in p:
                p[curr] += 1
            else:
                p[curr] = 1
        return c


n = input().strip()

reversed_n = n[::-1]
reversed_number = int(reversed_n) 
print(reversed_number)


def countTriangles(self, arr):
        n = len(arr)
        arr.sort()
        c = 0
        for k in range(n-1,1,-1):
            i = 0
            j = k - 1 
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    c += (j - i)
                    j -= 1 
                else:
                    i += 1
        return c


#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        start = 0
        cur = 0
        for i in range(n):
            cur += arr[i]
            while cur > target and start <= i:
                cur -= arr[start]
                start += 1
            if cur == target:
                return [start+1,i+1]
        return [-1]








