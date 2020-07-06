class Solution:
    def firstUniqChar(self, s: str) -> int:
        #如果不记得系统函数，自己写一个字典进行统计
        count = {}
        for ch in s:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1
                        
        #count=collections.Counter(s)   直接用一个系统函数统计结果
        
        
        # for idx,ch in enumerate(s):
        #     if count[ch]==1:
        #         return idx 
        # return -1
        
        #如果不记得enumerate（）函数，可以自己写一次循环
        #方法一：通过下标，直接返回下标的形式
        # for i in range(len(s)):
        #     if count[s[i]] == 1:
        #         return i
        # return -1

        #方法二：使用index索引
        for ch in s:
            if count[ch] == 1:
                return s.index(ch)
        return -1

        #上面所有时空复杂度都是一样的