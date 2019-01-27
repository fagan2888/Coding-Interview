class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Fabonacci
        x, y = 1, 1
        for _ in range(1, n):
            x, y = y, x + y
        return y