#This code is created by Chat GPT
while(1): #for continuous
    def is_valid(board, row, col, num):
        # Check if the number is already in the row or column
        if num in board[row] or num in [board[i][col] for i in range(9)]:
            return False
        
        # Check if the number is in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True

    def find_empty_location(board):
        # Find the first empty location (value 0) in the board
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None
    
    def solve_sudoku(board):
        # Find an empty location
        empty_loc = find_empty_location(board)
        
        # If there are no empty locations, the Sudoku is solved
        if not empty_loc:
            return True
        
        row, col = empty_loc
        
        # Try placing numbers from 1 to 9
        for num in range(1, 10):
            if is_valid(board, row, col, num):
                # Place the number if it's valid
                board[row][col] = num
                
                # Recursively try to solve the remaining Sudoku
                if solve_sudoku(board):
                    return True
                
                # If placing the current number doesn't lead to a solution, backtrack
                board[row][col] = 0
        
        # If no number from 1 to 9 can be placed, backtrack
        return False

    # Example Sudoku puzzle (0 represents empty cells)
    R=[0,1,2,3,4,5,6,7,8]
    C=[0,1,2,3,4,5,6,7,8]

    print("Enter the sudoku question Row wise and use '0' for blank cell")
# edit this part for my convenient to enter the question as input
    R[0]=list(str(input("enter row_1- ")))
    R[1]=list(str(input("enter row_2- ")))
    R[2]=list(str(input("enter row_3- ")))
    R[3]=list(str(input("enter row_4- ")))
    R[4]=list(str(input("enter row_5- ")))
    R[5]=list(str(input("enter row_6- ")))
    R[6]=list(str(input("enter row_7- ")))
    R[7]=list(str(input("enter row_8- ")))
    R[8]=list(str(input("enter row_9- ")))

    for n in range(0,9):
        C[n]=[int(value) for value in R[n]]

    sudoku_board=C

    # Solve the Sudoku puzzle
    if solve_sudoku(sudoku_board):
        # Print the solved Sudoku
        for row in sudoku_board:
            print(row)
    else:
        print("No solution exists.")