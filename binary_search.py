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










if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root




