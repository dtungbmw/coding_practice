class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = x
        if x <= 0:
            return False

        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x = int(x / 10)

        return org == rev

s = Solution()

print ( s.isPalindrome(12331))