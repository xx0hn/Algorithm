# 200. Number of Islands
# Medium

# 12079

# 307

# Add to List

# Share
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(h: str, w: str):
            grid[h][w]='0'
            dh=[0, 0, 1, -1]
            dw=[1, -1, 0, 0]
            for i in range(4):
                nh=h+dh[i]
                nw=w+dw[i]
                if nh>=0 and nw>=0 and nh<len(grid) and nw<len(grid[0]) and grid[nh][nw]=='1':
                    dfs(nh, nw)
        answer=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    answer+=1
                    dfs(i, j)
        return answer
