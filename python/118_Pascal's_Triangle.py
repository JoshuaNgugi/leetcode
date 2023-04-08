class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[0] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                result[i][j] = 1 if j in [0, i] else result[i - 1][j - 1] + result[i - 1][j]
        return result
