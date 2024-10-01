# Leet Code 75：1431. Kids With the Greatest Number of Candies
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candie = max(candies)
        for candie in candies:
            result.append(candie+extraCandies >= max_candie)
        return result
