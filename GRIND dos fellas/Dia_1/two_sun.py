from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        verifier = 0
        for num in nums:
            possible_num = target - num
            if(possible_num == num):
                verifier = nums.count(num)

                if(possible_num in nums and verifier > 1):
                    return [index, nums.index(possible_num, index + 1)]
            
            elif(possible_num in nums):
                return [index, nums.index(possible_num)]
            index += 1