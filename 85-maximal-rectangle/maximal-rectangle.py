class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        cols = len(matrix[0])
        heights = [0] * (cols + 1) # Extra '0' at the end to flush the stack
        max_area = 0
        
        for row in matrix:
            # Update heights based on the current row
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            # Solve 'Largest Rectangle in Histogram' for the current row
            stack = [-1] # Use -1 to handle the width of the first element
            for i in range(cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area





        