# Leet Code 75： 238. Product of Array Except Self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length
        for i in range(1, length):
            products[i] = products[i - 1] * nums[i - 1]
            print(f'i is {i}, product[i] is {products[i]}')
            print(f'product[i-1] is {products[i-1]}, nums[i-1] is {nums[i-1]}')
        print(f'after the left side, the products is {products}')
        right = nums[-1]
        for i in range(length - 2, -1, -1):
            products[i] *= right
            right *= nums[i]
            print(f'the product is {products}')
            print(f'in the right side: i is {i}, product[i] is {products[i]}, right is {right}')
        print(f'after the right side, the products is {products}')
        return products
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.productExceptSelf([4,1,2,3,7])