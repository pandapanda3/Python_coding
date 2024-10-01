# Leet Code 75： 1768. Merge Strings
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_list=[]
        for a,b in zip(word1, word2):
           merge_list.append(a)
           merge_list.append(b)
           print(f'merge_list is {merge_list}')
        
        merge_list.append(word1[len(word2):])
        print(f'append the rest of word1:{merge_list}')
        merge_list.append(word2[len(word1):])
        print(f'append the rest of word2:{merge_list}')
        return "".join(merge_list)
    
if __name__ == '__main__':
    solution = Solution()
    word1 = 'abcd'
    word2 = 'pqidnee'
    result = solution.mergeAlternately(word1,word2)
    print(f'the result is {result}')