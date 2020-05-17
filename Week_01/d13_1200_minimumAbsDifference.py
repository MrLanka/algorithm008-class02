#方法一
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        if len(arr)<3:return arr
        diff=[]
        for m in range(1,len(arr)):
            diff.append(arr[m]-arr[m-1])
        mindiff=min(diff)
        ans=[]
        for i in range(len(diff)):
            if diff[i]==mindiff:
                ans.append([arr[i],arr[i+1]])
        return ans

#方法二：先排序，再逐一遍历数组元素。
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        if len(arr)<3:
            return [arr]
        mindiff=arr[1]-arr[0]
        res=[[arr[0],arr[1]]]
        for i in range(2,len(arr)):
            curdiff=arr[i]-arr[i-1]
            if curdiff<mindiff:
                res=[[arr[i-1],arr[i]]]
                mindiff=curdiff
            elif curdiff==mindiff:
                res.append([arr[i-1],arr[i]])
        return res

#作者：VS1UynRVZc
#链接：https://leetcode-cn.com/problems/minimum-absolute-difference/solution/python3zui-xiao-jue-dui-chai-by-vs1uynrvzc/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。