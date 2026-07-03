class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = 0
        leftRow = 0
        rightRow = len(matrix) - 1
        while leftRow <= rightRow:
            centerRow = int((leftRow + rightRow) / 2)
            if matrix[centerRow][0] > target:
                rightRow = centerRow - 1
            elif matrix[centerRow][-1] < target: 
                leftRow = centerRow + 1
            else: 
                targetRow = centerRow
                break
        
        leftCol = 0
        rightCol = len(matrix[targetRow]) - 1
        while leftCol <= rightCol:
            centerCol = int((leftCol + rightCol) / 2)
            if matrix[targetRow][centerCol] == target:
                return True
            elif matrix[targetRow][centerCol] > target:
                rightCol = centerCol - 1
            else:
                leftCol = centerCol + 1

        return False


