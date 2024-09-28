# Leet Code 75： 338. Counting Bits
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # ans = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     ans[i] = ans[i >> 1] + (i & 1)
        # return ans

        counter = [0]
        for i in range(1, n+1):
            print(f'the i is {i}')
            counter.append(counter[i >> 1] + i % 2)
            print(f'counter is {counter}')
        return counter
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.countBits(12)