"""
Pseudocode

Algorithm ContainDuplicate(nums):
    Create an empty set called seen

    for each number in nums:
        If number is already in seen
            Return true
        End If

        Add number to seen
    End for
    Return false
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            
            seen.add(num)
        
        return False
        