# 1657. Determine if Two Strings Are Close

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # return set(word1)==set(word2) and sorted(Counter(word1).values())==sorted(Counter(word2).values())
        def alpha(word):
            Alpha = [False] * 26
            freq = [0] * 26
            
            for each in word:
                i = ord(each) - ord('a')
                Alpha[i] = True
                freq[i] += 1
            
            return Alpha, freq
        
        Alpha1, freq1 = alpha(word1)
        Alpha2, freq2 = alpha(word2)
        if Alpha1 != Alpha2:
            return False
        return sorted(freq1) == sorted(freq2)