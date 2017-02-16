class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        l = len(grid[0])
        c = 0
        for i in range(h):
            for j in range(l):
                if grid[i][j]==1:
                    c += self.Cal(grid, i, j)
                    
        return c
    def Cal(self, grid, i, j):
        c = 4
        if i-1>=0 and grid[i-1][j]==1:
            c -= 1
        if j-1>=0 and grid[i][j-1]==1:
            c -= 1
        if i+1<len(grid) and grid[i+1][j]==1:
            c -= 1
        if j+1<len(grid[0]) and grid[i][j+1]==1:
            c -= 1
        return c