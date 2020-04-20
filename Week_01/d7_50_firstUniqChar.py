class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic={}
        for x in s:
            dic[x]=not x in dic
        for key,val in dic.items():
            if val:
                return key
        return " "