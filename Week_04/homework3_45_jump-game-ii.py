class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        maxPos,end,step=0,0,0
        for i in range(n-1):
            maxPos=max(maxPos,i+nums[i])
            if i==end:
                end=maxPos
                step+=1
        return step