class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def isAnagram(s: str, t: str) -> bool:
            if len(s)!=len(t):return False
            se=set(s)
            for x in se:    
                if s.count(x)!=t.count(x):
                    return False
            return not False
        
        res=[]                 #时间复杂度为O（(n-m)*m）
        n,m=len(s),len(p)
        for i in range(n-m+1):
            if isAnagram(s[i:i+m],p):
                res.append(i)
        return res