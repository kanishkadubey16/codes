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