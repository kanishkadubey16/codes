class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(n%2==0 and n!=0):
            n=n/2
        return n==1
# Testing the function
solution = Solution()
print(solution.isPowerOfTwo(8))   
print(solution.isPowerOfTwo(10))  
print(solution.isPowerOfTwo(1))   
print(solution.isPowerOfTwo(16))  
print(solution.isPowerOfTwo(0))   



# new code -cimbing stairs
MOD = 10**9 + 7

def climbStairs(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    a, b = 1, 1  
    for i in range(2, n + 1):
        a, b = b, (a + b) % MOD
    
    return b
n = int(input())
print(climbStairs(n))


# new code 
def can_jump(nums):
    max_reachable = 0
    n = len(nums)
    
    for i in range(n):
        if i > max_reachable:
            print("false")
            return
        max_reachable = max(max_reachable, i + nums[i])
    
    print("true")


n = int(input().strip())  
nums = list(map(int, input().split()))
can_jump(nums)
