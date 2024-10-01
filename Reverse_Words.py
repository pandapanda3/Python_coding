# Leet Code 75： 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        result = s_list[::-1]
        return ' '.join(result)