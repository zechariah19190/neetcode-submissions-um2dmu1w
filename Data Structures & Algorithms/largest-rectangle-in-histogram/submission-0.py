class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
                            #      0 , 2   1
            while stack and stack[-1][1] > h:
                index, height = stack.pop()  # 0 2
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h)) # 0 1 

        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea