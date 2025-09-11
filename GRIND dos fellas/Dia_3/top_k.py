from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        result = [item[0] for item in sorted_items[:k]]
        return result
    
