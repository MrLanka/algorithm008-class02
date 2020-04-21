class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans=[]
        right,left=0,0
        while right<len(nums1) and left<len(nums2):
            if nums1[right]<nums2[left]:
                right += 1
            elif nums1[right]==nums2[left]:
                ans.append(nums1[right])
                right += 1
                left += 1
            else:
                left += 1
        return ans