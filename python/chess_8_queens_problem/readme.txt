The eight queens puzzle is a classic challenge to place eight chess queens on an 8×8 chessboard 
so that no two queens threaten each other. A valid layout requires that no two queens share the 
same row, column, or diagonal.

There is more than one solution.

This solution is written in Python.

Example solution
----------------

Q . . . . . . . 
. . . . Q . . . 
. . . . . . . Q 
. . . . . Q . . 
. . Q . . . . . 
. . . . . . Q . 
. Q . . . . . . 
. . . Q . . . . 


Note: A queen is represented by 'Q'


Algorithm:
----------

1. Place a queen in the first column of the first row.

2. Check if placing the queen in the current position conflicts with any previously placed queens.

3. If there is no conflict, proceed to the next column. If there is a conflict, 
   backtrack to the previous column and try placing the queen in the next row.

4. Repeat steps 2 and 3 for all columns.

5. If all queens are placed successfully without conflicts, a solution is found.

6. If no solution is found after exploring all possibilities, backtrack to the previous column 
   and try placing the queen in the next row.


Designed by Surjit Randhawa 2026
