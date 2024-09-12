from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result_list=[0]
        start=0
        for i in range(len(gain)):
            start += gain[i]
            result_list.append(start)
            print(f'start is {start}, result_list is {result_list}')
        max_result = max(result_list)
        return max_result

if __name__ == '__main__':
    gain = [-4,-3,-2,-1,4,3,2]
    solution = Solution()
    result = solution.largestAltitude(gain)