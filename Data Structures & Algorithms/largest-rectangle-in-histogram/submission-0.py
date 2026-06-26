class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack_pair = []

        stack_pair.append((0, heights[0]))
        
        for i in range(1, len(heights)):

            start = i
            h = heights[i]

            while stack_pair and stack_pair[-1][1] > h:
                index, height = stack_pair.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            
            stack_pair.append((start,h))


        for i,h in stack_pair:
            maxArea = max(maxArea, h*(len(heights)-i))

        return maxArea

