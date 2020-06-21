#自己想到的写法——————————但是超出了时间限制   O(N*N) 当然判断是否是有效字符串还需要乘一次时间，这个时间是当前字符串的长度
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def isValid(s):
            """
            :type s: str
            :rtype: bool
            """
            stack = []
            mapping = {")": "("}
            for char in s:
                if char in mapping:
                    top_element = stack.pop() if stack else '#'
                    if mapping[char] != top_element:
                        return False
                else:
                    stack.append(char)
            return not stack
        
        current_max = 0
        for i in range(len(s)):
            if s[i] == "(":
                for j in range(i,len(s)):
                    if isValid(s[i:j+1]):
                        current_max = max(current_max,j-i+1) 
        return current_max

#重新想了一下，有效长度一定是偶数，从小于等于s长度的时候算起，时间复杂度依旧不变
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def isValid(s):
            """
            :type s: str
            :rtype: bool
            """
            stack = []
            mapping = {")": "("}
            for char in s:
                if char in mapping:
                    top_element = stack.pop() if stack else '#'
                    if mapping[char] != top_element:
                        return False
                else:
                    stack.append(char)
            return not stack
        
        n = len(s)
        if n <= 1:return 0
        k = n if n % 2 == 0 else n-1
        for i in range(k,0,-2):             #最大可能长度，两个两个递减
            for j in range(n-i+1):
                if s[j] == "(" and isValid(s[j:j+i]):
                    return i
        return 0



 
#动态规划        时间复杂度为O（N）    注意状态转移方程最重要
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = ' '+s
        dp = [0 for _ in range(len(s))] 
        maxs = 0
        for i in range(1,len(s),1):
            if s[i] == ')':
                if i-1 >= 0 and s[i-1] == '(':       #情况1
                    if  i-1 == 0:
                        dp[i] = 2
                        maxs = max(maxs,dp[i])
                    else:
                        dp[i] = dp[i-2]+2
                        maxs = max(maxs,dp[i])
                if i-1 >= 0 and s[i-1] == ')':   #情况2
                    if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                        maxs = max(maxs,dp[i])
        return  maxs

#使用stack     时间复杂度为O（N）    每次放入栈中的为下标，注意下标的变化
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        results = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                #取出栈顶的值
                if len(stack) != 0:
                    results = max(results,i-stack[-1])
                else:
                    stack.append(i)
        return results