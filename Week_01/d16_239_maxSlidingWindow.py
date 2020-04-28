#自己的题解，时间复杂度O(N)   空间复杂度:O(n-k)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(nums)-k+1):
            ans.append(max(nums[i:i+k]))
        return ans