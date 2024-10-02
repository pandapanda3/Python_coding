# 1493. Longest Subarray of 1's After Deleting One Element
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        count = 0
        zero = 0

        for right in range(len(nums)):
            print(f'right is {right}')
            if nums[right] == 0:
                zero += 1
            while zero > 1:
                if nums[left] == 0:
                    zero-=1
                left += 1
                print(f'right is {right}, left is {left}')
            print(f'before calculate:{count}, right is {right}, left is {left}')
            count = max(count, right-left)
            print(f'after calculate:{count}')
        return count
    
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.longestSubarray([0,1,1,1,0,1,1,0,1])