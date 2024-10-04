# Leetcode 75: 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_number = 0
        voewel_letter = set('aeiou')
        count = 0
        right = k
        left = 1
        
        for i in range(k):
            if s[i] in voewel_letter:
                count += 1
        max_number = max(max_number, count)
        
        while right < len(s):
            if s[left - 1] in voewel_letter:
                count -= 1
            
            if s[right] in voewel_letter:
                count += 1
            max_number = max(max_number, count)
            left += 1
            right += 1
        return max_number