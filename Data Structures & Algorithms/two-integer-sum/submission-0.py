"""
Pseudocode

Algorithm TwoSum(nums, target):
    Create an empty dictionary called seen

    for each index i from 0 to length(nums) - 1:
        complement = target - nums[i]

        if complement exists in seen
            Return [seen[complement], i]
        End if

        Store nums[i] and it index in seen
    
    End for
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i
        