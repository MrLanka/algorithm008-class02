#自己的题解：时间复杂度和空间复杂度都是O(1)
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        total_jumbo=int((tomatoSlices-2*cheeseSlices)/2) 
        total_small=int((4*cheeseSlices-tomatoSlices)/2)
        if 4*total_jumbo+2*total_small==tomatoSlices and total_jumbo>=0 and total_small>=0:
            return [total_jumbo,total_small]
        else:
            return []



#官方题解
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0 or tomatoSlices < cheeseSlices * 2 or cheeseSlices * 4 < tomatoSlices:
            return []
        return [tomatoSlices // 2 - cheeseSlices, cheeseSlices * 2 - tomatoSlices // 2]