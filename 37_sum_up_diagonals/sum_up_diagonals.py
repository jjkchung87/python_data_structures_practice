def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30

        >>> m3 = [
        ...    [1, 2, 3, 4],
        ...    [4, 5, 6, 7],
        ...    [7, 8, 9, 10],
        ...    [11, 12, 13, 14],
        ... ]
        >>> sum_up_diagonals(m3)
        58
    """
    total_TL_BR = 0
    total_BL_TR = 0

    for i in range(len(matrix)):
        total_TL_BR += matrix[i][i]
    
    reversed_matrix = [list(row) for row in matrix]
    reversed_matrix.reverse()

    for i in range(len(reversed_matrix)):
        total_BL_TR += reversed_matrix[i][i]
    
    total = total_BL_TR + total_TL_BR
    return total



