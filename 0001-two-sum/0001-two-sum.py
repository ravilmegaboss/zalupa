class Solution(object):
    def twoSum(self, nums, target):
        size = len(nums)
        minim = min(nums, key=abs)
        for i in range(size):
            for j in range(size):
                if((nums[i] + nums[j] == target) & (i != j)):
                    return (i, j)
            """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        