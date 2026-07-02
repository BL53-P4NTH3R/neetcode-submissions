"""
Pseudocode

Algorithm isAnagram(s, t):
    If length of s is not equal to length of t
        Return false
    End If

    Create an empty dictionary called count

    For each character in s:
        If character exists in count
            Increase its count by 1
        Else
            Add character to count with value 1
        End If
    End For

    For each character in t:
        If character does not exist in count
            Return false
        End If

        Decrease its count by 1

        If count becomes less than 0
            Return false
        End If
    End For

    Return true
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = dict()

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for char in t:
            if char not in count:
                return False

            count[char] -= 1

            if count[char] < 0:
                return False

        return True 
        