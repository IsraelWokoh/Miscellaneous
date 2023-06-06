def deleteColumn(matrix): # WORKS
    for row in matrix:
        row[0].remove(row[0][0])

def swapRows(matrix, columnIndex=1): # WORKS
    if columnIndex != 0:
        print(f'Swapping row 1 and row {columnIndex+1}.')
        matrix[columnIndex], matrix[0] = matrix[0], matrix[columnIndex] # Dual reassignment
    return matrix

def reduce(matrix):
    return matrix

def leadingOne(matrix):
    return matrix

def Gauss(matrix):
    if all(row[0][index] == 0 for row in matrix for index in range(len(row))): # If main matrix all 0s
        return matrix
    else:
        columnIndex = 0
        nonZeroFound = False

        while not nonZeroFound: # Finding column with first non-zero entry
            column = [row[0][0] for row in matrix] # Create column
            if all(index == 0 for index in column): # If column all 0s - WORKS
                print('Deleting column.')
                deleteColumn(matrix) # Reduce matrix
            else: # Non-zero entry in column
                if column[columnIndex] != 0:
                    swapRows(matrix, columnIndex) # Move row to top - WORKS
                    nonZeroFound = True # Stop looking for it
                columnIndex += 1

        divisor = matrix[0][0][0]
        print(divisor)
        # for row in matrix: # Creating leading 1 in top row
        #     print('Dividing rows')
        #     for section in row:
        #         for index in range(len(section)):
        #             section[index] /= divisor
        #             if section[index] % 1 == 0: # Present integers normally
        #                 section[index] = int(section[index])

        leadingOne(matrix)

        for row in matrix:
            print(row)
    return matrix

def GaussJordan(matrix):
    Gauss(matrix)
    reduce(matrix)
    return matrix

augMatrix = [
    [[0,1,-5],[6]], # [row] = [[main], [aug]]
    [[0,1,4],[-5]],
    [[-4,8,6],[7]]
]

Gauss(augMatrix)