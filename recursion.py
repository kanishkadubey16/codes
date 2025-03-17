class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(n%2==0 and n!=0):
            n=n/2
        return n==1
# Testing the function
solution = Solution()
print(solution.isPowerOfTwo(8))   # True
print(solution.isPowerOfTwo(10))  # False
print(solution.isPowerOfTwo(1))   # True
print(solution.isPowerOfTwo(16))  # True
print(solution.isPowerOfTwo(0))   # False
