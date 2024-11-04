
"""
TRICK #1: ITERATE THROUGH "ROWS" IN A FOR LOOP. HENCE IT'S IMPOSSIBLE TO DUPLICATE A ROW. SO DON'T NEED TO EXPLICITLY CHECK FOR ROWS. ONLY NEED TO CHECK FOR COLUMNS AND DIAGONALS.

TRICK #2: BASE CASE - IF ROW == N. I.E. IF GONE BEYOND THE NUMBER OF ROWS ON THE BOARD WITHOUT ANY ERROR, THEN ADD THIS RESULT TO YOUR OVERALL RESULTS.

TRICK #3: RECURSION OCCURS INSIDE A FOR LOOP. THE LOOP CORRESPONDS TO EACH "COLUMN". THIS LOOP IS NAIVE, COZ DOESN'T CONSIDER THE COLUMNS ALREADY USED BY A PREVIOUS ROW OF THE BOARD.

TRICK #4: USE "ALL" TO CHECK THAT A NEW QUEEN PLACEMENT DOESN'T CONFLICT WITH ANY OF THE PREVIOUS QUEENS. 2 PARTS TO THIS: 1: ENSURE AS(C-COL) != 0 ... I.E. ENSURE COLUMN NOT ALREADY IN USE .... AND 2: ENSURE (C-COL) != (ROW-I), THIS ENSURES NOT ON THE SAME DIAGONAL. I.E. (ROW-i) IS THE NUMBER OF ROWS YOU INCREASED. AND (C-COL) IS THE NUMBER OF COLUMNS YOU CLIMBED UP. IF THESE NUMBERS ARE THE SAME, YOU'RE ON THE SAME DIAG AS ANOTHER QUEEN, SO FAIL.

TRICK #5: IF THE "ALL" IS OK FOR THIS COLUMN, THEN DO RECURSION FOR THE NEXT ROW I.E. ROW+1.

TRICK #6: EMPTY PLACEHOLDER FOR RESULTS IS JUST A LIST OF ZEROES OF LENGTH 'N'. 

"""

from typing import List

def n_queens(n: int) -> List[List[int]]:
    def solve_n_queens(row):
        if row == n:
            # All queens are legally placed.
            result.append(col_placement.copy())
            return
        for col in range(n):
            # Test if a newly placed queen will conflict any earlier queens
            # placed before.
            if all(
                    abs(c - col) not in (0, row - i)
                    for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row + 1)

    result: List[List[int]] = []
    col_placement = [0] * n
    solve_n_queens(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)

