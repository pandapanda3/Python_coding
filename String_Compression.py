# Leet Code 75:  443. String Compression
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        num = 0
        i = 0
        while i < len(chars):
            letter = chars[i]
            count =0
            while i < len(chars) and chars[i] == letter:
                count+=1
                i += 1
            chars[num] = letter
            num += 1
            if count > 1:
                for digit in str(count):
                    chars[num] = digit
                    num +=1
        return num
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.compress(["a","a","b","b","c","c","c"])