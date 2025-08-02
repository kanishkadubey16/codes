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
