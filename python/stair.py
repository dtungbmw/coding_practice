class Solution:
    def climbStairs(self, n: int) -> int:
        path = {1: 1, 2: 2, 3: 3, 4: 5}

        for i in range(4, n + 1):
            path[i] = path[i - 1] + path[i - 2]

        return path[n]

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n == 3:
#             return 3
#
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)

s = Solution()

res = s.climbStairs(38)

print(str(res))