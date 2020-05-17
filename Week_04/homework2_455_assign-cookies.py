class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n,m=len(g),len(s)
        i,j,count=0,0,0
        while i<n and j<m:
            if g[i]<=s[j]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        return count