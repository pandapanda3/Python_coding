from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) -1 or flowerbed[i+1] == 0
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -=1
        return n <= 0
    
if __name__ == '__main__':
    # 创建Solution类的实例
    solution = Solution()
    
    # 定义一些测试用例
    test_cases = [
        ([1, 0, 0, 0, 1], 1),  # 可以种1朵花，预期返回True
        ([1, 0, 0, 0, 1], 2),  # 无法种2朵花，预期返回False
        ([0, 0, 1, 0, 0], 1),  # 可以种1朵花，预期返回True
        ([0, 0, 1, 0, 0], 2),  # 无法种2朵花，预期返回False
        ([0], 1),  # 可以种1朵花，预期返回True
        ([1], 1)  # 无法种1朵花，预期返回False
    ]
    
    # 遍历测试用例并打印结果
    for flowerbed, n in test_cases:
        result = solution.canPlaceFlowers(flowerbed, n)
        print(f"flowerbed: {flowerbed}, n: {n}, can place: {result}")