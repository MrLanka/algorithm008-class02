class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        s=set(digits)
        if len(s)==1 and s=={9}:
            digits=[1]
            for i in range(n):
                digits.append(0)
            return digits
        else:
            for i in range(n):
                if digits[n-i-1] < 9:
                    digits[n-i-1]=digits[n-i-1]+1
                    return digits
                    break
                else:
                    digits[n-i-1]=0
                    i += 1

#自己的思路还未学习别人的，时间O(n),空间O(n)