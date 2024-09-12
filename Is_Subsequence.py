# leetcode 75: 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp =0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp +=1
            tp +=1
        return sp == len(s)
        
if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    solution = Solution()
    solution.isSubsequence(s,t)