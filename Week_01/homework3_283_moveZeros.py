class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i=j=0
        while j<n:      #j用来控制循环，i用来讯息好遍历是否为零，只有当第i个为0，且j个不为0，才交换
            if nums[i]==0 and nums[j]!=0: nums[i],nums[j]=nums[j],nums[i]
            if nums[i]!=0:i += 1
            j += 1

#有没有可能j在后，i在前，从而把0换到前面去的情况？
#答：不会。因为始终有j>=i，i不会出现在j前面。