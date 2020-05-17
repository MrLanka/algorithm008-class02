#方法一：自己想的双指针解法  时间复杂度为O(max(n,m))  空间复杂度O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j,count=0,0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        return count==len(s)

