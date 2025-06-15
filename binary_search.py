nums = [-2,-1,-1,1,2,3]

l = 0
r = len(nums)-1
m = 0
countN = 0
countP = 0
while l <= r:
    mid = (l+r)//2
    if nums[mid] < 0:
        countN = mid + 1
        l = mid + 1
    else:
        r = mid-1
l,r = 0,len(nums)-1
while  l <= r:
    mid = (l+r)//2
    if nums[mid] <= 0:
        l = mid+1
    else:
        countP  = len(nums) - mid
        r = mid-1
print(max(countN,countP))




class Solution:   
    def peakElement(self,arr):
        l = 0
        h = len(arr)-1 
        while l <= h:
            mid = (h+l)//2 
            left = arr[mid-1] if mid > 0 else float ("-inf")
            right = arr[mid+1]if mid < len(arr) - 1 else float("-inf")
            if arr[mid] > left and arr[mid] > right:
                return mid 
            elif arr[mid] < right:
                l = mid + 1
            else:
                h = mid - 1
        return -1


if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



