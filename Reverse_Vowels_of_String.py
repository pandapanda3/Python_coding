# Leet Code 75： 345. Reverse Vowels of a String


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = 'aeiouAEIOU'
        result = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            while result[i] not in vowel_list and i < j:
                i += 1
            while result[j] not in vowel_list and i < j:
                j -= 1
            
            result[i], result[j] = result[j], result[i]
            i += 1
            j -= 1
        return "".join(result)
