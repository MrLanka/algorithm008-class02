#方法一：直接排序，时间复杂度为O(nlogn)
#class Solution:
#   def isAnagram(self, s: str, t: str) -> bool:
#        return sorted(s)==sorted(t)



#方法二：统计每个字符的个数进行比较,时间复杂度O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        se=set(s)
        for x in se:    
            if s.count(x)!=t.count(x):
                return False
        return not False