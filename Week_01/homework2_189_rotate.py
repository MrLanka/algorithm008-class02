#使用三次旋转数组
class Solution:
    def rotate(self, nums: List[int], k: int)->None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n          #k对n取余，确定最终旋转的长度
        def reverse_nums(list,start,end):      #定义一个反转数组的函数
            while start<end:
                list[start],list[end]=list[end],list[start]
                start += 1
                end -=1

        reverse_nums(nums,0,n-1)              #整个数组旋转一次
        reverse_nums(nums,0,k-1)              #前k个旋转一次
        reverse_nums(nums,k,n-1)              #后n-k个再旋转一次

#时间复杂度O(n) 空间复杂度O(1)