# target = 9
# i = 0
# num=[2,7,11,15]
# j = i+1
# for i in range(len(num)) :
#     for j in range (i+1,len(num)):
#         if num[i] + num[j] == target:
#             print(f"the sum numbers are {num[i]} and {num[j]}")
#             break
        
class Solution:
    def twoSum(self, num, target):
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                if num[i] + num[j] == target:
                    print(num[i], num[j])  
sol = Solution()
print(sol.twoSum([0,1,2,3,4,5], 6))