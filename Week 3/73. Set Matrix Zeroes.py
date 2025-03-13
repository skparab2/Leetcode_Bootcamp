def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        setToZeroRow = {}
        setToZeroCol = {}

        i = 0
        while (i < len(matrix)):
            j = 0
            while (j < len(matrix[i])):
                if (matrix[i][j] == 0):
                    setToZeroRow[i] = 0
                    setToZeroCol[j] = 0
                j += 1
            i += 1
        
        # print(setToZeroRow)

        for k in setToZeroRow:
            p = 0
            while (p < len(matrix[k])):
                matrix[k][p] = 0
                p += 1

        for k in setToZeroCol:
            p = 0
            while (p < len(matrix)):
                matrix[p][k] = 0
                p += 1

        # print(setToZeroCol)
