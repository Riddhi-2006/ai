# class Solution(object):
#     def containsDuplicate(self, nums):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False  

class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False  