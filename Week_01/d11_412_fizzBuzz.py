class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        if n==0:return []
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                ans.append("Fizz")
            elif i%3!=0 and i%5==0:
                ans.append("Buzz")
            elif i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            else:
                ans.append(str(i))
        return ans