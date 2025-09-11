from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        temp = []

        while (len(strs) > 0):
            word = strs[0]
            temp.append(word)
            for str in strs[1:]:
                if(len(word) == len(str)):
                    if(sorted(word) == sorted(str)):
                        temp.append(str)
                        strs.remove(str)
                        
            strs.remove(word)
            output.append(temp)
            temp = []