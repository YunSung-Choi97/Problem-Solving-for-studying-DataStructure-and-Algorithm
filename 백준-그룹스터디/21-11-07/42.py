from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left, right = [0] * n, [0] * n
        min_l, min_r = 0, 0
        for i in range(n):
            if min_l < height[i]:
                min_l = height[i]
            left[i] = min_l

            if min_r < height[n - 1 - i]:
                min_r = height[n - 1 - i]
            right[n - 1 - i] = min_r
        
        block = 0
        for i in range(n):
            block += min(left[i], right[i])
        
        return block - sum(height)