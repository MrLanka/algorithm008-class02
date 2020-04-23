#以窗口的左端点开始遍历，使用切片寻找最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        if len(nums)==0:return []
        for i in range(len(nums)-k+1):
            ans.append(max(nums[i:i+k]))
        return ans

