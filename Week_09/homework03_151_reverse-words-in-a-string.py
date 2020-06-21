#双指针法
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': 
                i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': 
                i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回


# 将每一部分单词划出，reverse
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s):
            n = len(s)
            i,j = 0,n-1
            while i<j:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1
        
        s = s.strip()
        s = s.split()
        
        reverse(s)
        return " ".join(s)