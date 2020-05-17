#单调栈法
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans,st = 0,[]
        heights.insert(0,0)
        heights.append(0)
        for i in range(len(heights)):
            while len(st) != 0 and heights[st[-1]] > heights[i]:
                cur = st[-1]
                st.pop()
                left = st[-1] + 1
                right = i - 1
                ans = max(ans, (right - left + 1) *heights[cur])
            st.append(i)
        return ans