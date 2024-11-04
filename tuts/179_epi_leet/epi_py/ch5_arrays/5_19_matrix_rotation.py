"""
TRICK
DOUBLE PASS
OUTER LOOP: FOR LAYERS OF MATRIX. SO ONLY NEED N//2 COZ OTHERWISE WOULD GO BEYOND THE MIDDLE 
	STOP AT THE MIDDLE OF MATRIX OBVIOUSLY COZ APPROACHING FROM 2 SIDES.
INNER LOOP: 4-WAY EXCHANGE.
	[i][j] INVERT EACH TIME ... I.E. FIRST AND THIRD WILL BE [i][j] BUT 2ND AND 3RD WILL BE [j][i] 
	THIS ALTERNATING IS BECAUSE YOU FLIP 90 DEGREES EACH STEP.
	YOU ALSO ALTERNATE WITH THE SIGNS AS FOLLOWS:
		[i][j] ... [~j][i] ... [~i~][j] ... [j][~i] 
	THEN JUST ASSIGN THESE WITH THE ORDER SHIFTED BY 1 POSITION.
"""

from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:

    matrix_size = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, matrix_size - i):
            # Perform a 4-way exchange. Note that A[~i] for i in [0, len(A) - 1]
            # is A[-(i + 1)].
            (square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j],
             square_matrix[j][~i]) = (square_matrix[~j][i],
                                      square_matrix[~i][~j],
                                      square_matrix[j][~i],
                                      square_matrix[i][j])


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
