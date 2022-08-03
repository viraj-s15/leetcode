class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        [nums.remove(x) for x in nums[0:] if x == val]
        return len(nums)