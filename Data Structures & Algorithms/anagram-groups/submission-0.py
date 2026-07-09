"""
Pseudocode

Algorithm GroupAnagrams(str)
    
    Create an empty dictionary called groups

    For each word in strs
        Key <- sorted version of word

        If key is not in groups
            Create an empty list for key
        End If

        Add word to groups[key]
    
    End For

    Return all the values in groups    
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = list()

            groups[key].append(word)

        return list(groups.values())



        