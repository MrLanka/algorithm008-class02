class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums,prod=0,1
        while n>=1:
            sums=sums+(n%10)
            prod=prod*(n%10)
            n=n//10
        return prod-sums