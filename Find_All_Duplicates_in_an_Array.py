# Given an integer array nums of length n where all the integers of nums are in the range [1, n]
# and each integer appears once or twice, return an array of all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:
#
# Input: nums = [1,1,2]
# Output: [1]
# Example 3:
#
# Input: nums = [1]
# Output: []

class Solution:
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            nums[abs(num) - 1] *= -1

        return res