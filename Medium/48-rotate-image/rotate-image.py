class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def roro(i, k):
            for j in range(0, k):
                t = matrix[i][i + j]
                matrix[i][i + j] = matrix[n - i - 1 - j][i]
                matrix[n - i - 1 - j][i] = matrix[n - i - 1][n - i - 1 - j]
                matrix[n - i - 1][n - i - 1 - j] = matrix[i + j][n - i - 1]
                matrix[i + j][n - i - 1] = t

        i = 0
        n = len(matrix)
        k = n - 1
        while k > 0:
            roro(i, k)
            i += 1
            k -= 2
        return
