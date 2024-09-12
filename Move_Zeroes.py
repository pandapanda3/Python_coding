# leetcode 75: 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right],nums[left]
                left +=1
        print(f' The result is {nums}')
        return nums
    
    def second_method(self,nums: List[int]) -> None:
        ball = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ball += 1
            elif ball > 0:
                temp = nums[i]
                nums[i] = 0
                nums[i-ball] = temp
        print(f' The result is {nums}')
        return nums
if __name__ == '__main__':
    nums=[0,1,0,3,12]
    solution = Solution()
    result1 = solution.moveZeroes(nums)
    result2 = solution.second_method(nums)