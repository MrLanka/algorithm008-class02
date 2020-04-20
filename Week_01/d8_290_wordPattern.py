#方法一：使用map函数
#class Solution:
#    def wordPattern(self, pattern: str, str: str) -> bool:
#        s_l=str.split()
#        return list(map(pattern.index,pattern))==list(map(s_l.index,s_l))

#方法二：字典查找
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word_list = str.split(' ')
        if len(pattern) != len(word_list):
            return False
        else:
            d ={}
            for i in range(len(pattern)):
                key = pattern[i]
                if key in d:
                    if d[key] == word_list[i]:
                        continue
                    else:
                        return False
                else:
                    d_values = set(d.values())
                    d[key] = word_list[i]
                    if set(d.values()) == d_values:
                        return False
        return True