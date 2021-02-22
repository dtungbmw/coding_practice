#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num0 = 0
        num1 = 0
        num2 = 0

        for item in nums:
            if item == 0:
                num0 += 1
            elif item == 1:
                num1 += 1
            elif item == 2:
                num2 += 1

        for i in range(len(nums)):
            if num0 > 0:
                nums[i] = 0
                num0 -= 1
            elif num1 > 0:
                nums[i] = 1
                num1 -= 1
            elif num2 > 0:
                nums[i] = 2
                num2 -= 1


