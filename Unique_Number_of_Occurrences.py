from typing import List

# leetcode 75: 1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # amazing !
        # return len(set(Counter(arr).values()))==len(Counter(arr).values())

        frequency = {}

        for num in arr: # Store element and its frequency
            # The method to compute the frequency of dict key
            print(f'The result : {frequency.get(num,0)}')
            frequency[num] = frequency.get(num,0) + 1

        # True if we get n different frequency for n different numbers
        return len(frequency) == len(set(frequency.values()))
if __name__ == '__main__':
    arr = [1,2,2,1,1,3]
    solution = Solution()
    result = solution.uniqueOccurrences(arr)