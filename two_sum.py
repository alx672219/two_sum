from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    h = {}   # hashmap
    for i, num in enumerate(nums):
        n = target - num

        if n not in h:
            h[num] = i
        else:
            return [h[n], i]