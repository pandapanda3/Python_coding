from typing import List

# leetcode 75: 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # result_list=[[],[]]
        # nums1 = list(dict.fromkeys(nums1))
        # nums2 = list(dict.fromkeys(nums2))
        # for i in range(len(nums1)):
        #     if nums1[i] not in nums2:
        #         result_list[0].append(nums1[i])
        # for j in range(len(nums2)):
        #     if nums2[j] not in nums1:
        #         result_list[1].append(nums2[j])
        # return result_list
        print(f'The set(nums1) is {set(nums1)}, set(nums1) - set(nums2) is {set(nums1) - set(nums2)}')
        print(f'the type of set(nums1) is {type(set(nums1))}')
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
    
if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    solution = Solution()
    result = solution.findDifference(nums1,nums2)