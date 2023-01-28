# 217 - array and hashing

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        listLen = len(nums)
        setLen = len(set(nums))

        return setLen != listLen