#Runtime: 889ms
#Memory: 18.14MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            if ((target - nums[i]) in nums):
                index = nums.index(target - nums[i])
                if i != index : 
                    return [i, index]
        