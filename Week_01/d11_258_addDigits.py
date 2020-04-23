#模9取位
class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9+1 if num!=0 else 0

class Solution:
    def addDigits(self, num: int) -> int:
        if num%9==0 and num!=0:
            return 0
        else:
            return num%9

#模10取余，循环
class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            sum=0
            while num>0:
                sum += num%10
                num //=10
            num=sum
        return num


#递归