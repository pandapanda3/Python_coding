from typing import List

# leetcode 75: 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for index, element in enumerate(nums):
            
            right_sum -= element
            if left_sum == right_sum:
                return index
            
            left_sum += element
        return -1
    
if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    solution = Solution()
    result = solution.pivotIndex(nums)