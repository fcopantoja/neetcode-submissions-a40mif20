class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        max_left[0] = height[0]
        max_right[-1] = height[-1]

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i])
        
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
        
        water = 0

        print(height)
        print(max_left)
        print(max_right)

        for i in range(len(height)):
            h = min(max_left[i], max_right[i])
            print(i, 'h', h)
            water += h - height[i]

        return water


        
        