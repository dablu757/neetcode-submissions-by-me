class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)-1

        def helper(idx):
            if idx>=n:
                return True

            for jump in range(1,nums[idx]+1):
                if helper(idx+jump):
                    return True

            return False

        return helper(0)
        