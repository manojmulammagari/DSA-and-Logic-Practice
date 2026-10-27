class Solution:

  def createGrid(self, m: int, n: int) -> list[str]:
    # Initialize an m x n grid filled entirely with obstacles ('#')
    grid = [["#" for _ in range(n)] for _ in range(m)]

    # Make the top row free cells '.' (moving all the way right)
    for j in range(n):
      grid[0][j] = "."

    # Make the rightmost column free cells '.' (moving all the way down)
    for i in range(m):
      grid[i][n - 1] = "."

    # Convert lists of characters into strings as required by the return type
    return ["".join(row) for row in grid]
    print(7)