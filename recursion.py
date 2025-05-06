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


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
        


n = int(input().strip())  
nums = list(map(int, input().split()))
can_jump(nums)


n, k = map(int, input().split())
treasure = list(map(int, input().split()))
dp = [0] * n
dp[0] = treasure[0]

for i in range(1, n):
    option1 = dp[i - 1]
    option2 = treasure[i]
    if i - k - 1 >= 0:
        option2 += dp[i - k - 1]
    dp[i] = max(option1, option2)
print(dp[n - 1])
