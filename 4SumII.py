class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        lookup = {}
        for i in range(n):
            for j in range(n):
                sum = nums1[i] + nums2[j]
                if sum not in lookup:
                    lookup[sum] = 0
                lookup[sum] += 1
        
        ans = 0
        for i in range(n):
            for j in range(n):
                sum = nums3[i] + nums4[j]
                if -sum in lookup:
                    ans += lookup[-sum]
        return ans
