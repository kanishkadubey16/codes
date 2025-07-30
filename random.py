

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



        return len(set(c.values())) == 1


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








