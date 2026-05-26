class Solution(object):
    def maxSubArray(self, nums):
        maxsub = nums[0]
        cursum = 0
        for n in nums:
            if cursum < 0:
                cursum = 0
            cursum += n
            maxsub = max(maxsub, cursum)
        return maxsub

# test cases
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(sol.maxSubArray([1]))                        # 1
print(sol.maxSubArray([5,4,-1,7,8]))              # 23