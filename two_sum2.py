def twoSum(self, nums, target):
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in hash_table:
            hash_table[nums[i]] = i
        else:
            return [hash_table[complement], i]