# Leet Code 75： 338. Counting Bits
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return functools.reduce(lambda x, y: x ^ y, nums, 0)
        result = 0
        for num in nums:
            result ^=num
            print(f'the result is {result}')
        return result
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.singleNumber([4,1,2,1,2])