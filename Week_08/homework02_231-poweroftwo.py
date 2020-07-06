#时间复杂度为 O（logN）
#class Solution:
#    def isPowerOfTwo(self, n: int) -> bool:
#        if n==0:return False
#        while n%2==0:
#            n=n/2
#        return n==1

#位运算，最右边的1 时间复杂度O（1）
#class Solution:
#    def isPowerOfTwo(self, n: int) -> bool:
#        return n & (-n) == n if n != 0 else False


#位运算，去除最右边的1 时间复杂度O（1）
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n-1) == 0 if n != 0 else False