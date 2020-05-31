#法一：空间复杂度为O(N*2))的解法，使用二维数组
#class Solution:
#    def rob(self, nums: List[int]) -> int:
#        if len(nums)==0:return 0

#        n=len(nums)
#        a=[[0,1] for _ in range(n)]
#        a[0][0]=0
#        a[0][1]=nums[0]
#
#        for i in range(1,n):
#            a[i][0]=max(a[i-1][0],a[i-1][1])
#            a[i][1]=a[i-1][0]+nums[i]
        
#        return max(a[n-1][0],a[n-1][1])

#法二：空间复杂度为O(N)的解法，使用一维数组
#    def rob(self, nums: List[int]) -> int:
#        if len(nums)==0:return 0
#        if len(nums)==1:return nums[0]

#        n=len(nums)
#        a=[0]*n 
#        a[0]=nums[0]
#        a[1]=res=max(nums[0],nums[1])

#        for i in range(2,n):
#            a[i]=max(a[i-1],a[i-2]+nums[i])
#            res=max(res,a[i])

#        return res

#法三：空间复杂度为O(1)的解法——自己写的
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]
        nums=nums+[0]
        n=len(nums) 
        x=nums[0]
        y=res=max(nums[0],nums[1])

        for i in range(2,n):
            z=max(y,x+nums[i])
            res=max(res,z)
            x=y
            y=z
        
        return res



#法三：空间复杂度为O(1)的解法——别人的
# class Solution:
    # def rob(self, nums: List[int]) -> int:
        # premax=0
    #    curmax=0
        # for i in nums:
            # temp=curmax
            # curmax=max(premax+i,curmax)
            # premax=temp
        # return curmax