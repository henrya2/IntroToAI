import argparse

def print_student_name_Anumber():
    """
    Method to print student name and Anumber
    Args: None
    Returns : None
    """
    ### TODO
    print("Student full name :", "XYS")  # replace XYS with your name
    print("Student A Number :", "A1234566")  # replace with your A Number

def under_attack(col, queens):
    """
    Method to check if the current queens assignment leads to a conflict
    Args:
        col: new assignment to check
        queens: current queens assignment
    Returns:
         (bool): True if conflict / attack. False if not
    """
    return col in queens or \
           any(abs(col - x) == len(queens) - i for i, x in enumerate(queens))

def rsolve_q2(queens, n):
    num_assignments = 0

    board_occupations = [ [0] * n for i in range(n) ]

    def check_under_attack(board_o, row, col):
        return board_o[row][col] != 0

    def add_occupation(board_o, n, row, col):
        if (row >= 0 and col >= 0 and row < n and col < n):
            board_o[row][col] += 1

    def remove_occupation(board_o, n, row, col):
        if (row >= 0 and col >= 0 and row < n and col < n):
            board_o[row][col] -= 1

    def queen_place_board_occupations(board_o, n, row, col, func):
        rd_start_row = row + col
        ld_start_row = row - col

        func(board_o, n, row, col)

        for i in range(n):

            # row
            if (i != col):
                func(board_o, n, row, i)

            # col
            if (i != row):
                func(board_o, n, i, col)

            # \ diag
            if rd_start_row > -1:
                if (rd_start_row != row or i != col):
                    func(board_o, n, rd_start_row, i)
                rd_start_row -= 1

            # / diag
            if ld_start_row < n:
                if (ld_start_row != row or i != col):
                    func(board_o, n, ld_start_row, i)
                ld_start_row += 1

    def add_or_remove_occupation(board_o, n, row, col, add_or_remove):
        if (add_or_remove):
            alt_func = add_occupation
        else:
            alt_func = remove_occupation

        queen_place_board_occupations(board_o, n, row, col, alt_func)
    
    def count_new_occupations(board_o, n, row, col):

        class CountObject:
            def __init__(self, n):
                self.n = n

            def add(self, i):
                self.n += i
        
        count_obj = CountObject(0)

        def iter_occupation(board_o, n, row, col):
            nonlocal count_obj
            if (row >= 0 and col >= 0 and row < n and col < n):
                if board_o[row][col] == 0:
                    count_obj.add(1)

        queen_place_board_occupations(board_o, n, row, col, iter_occupation)

        return count_obj.n

    def rsolve(queens,n):
        """
        Recursively find solution for NQueens problem
        Args:
            queens (list): List of integers. Each int gives the row assignment for the queen in a column
            n (int): Board size
        Returns:
            (list) : NQueens assignment as a list of integers. If no assignment is possible, returns empty list
        """
        nonlocal num_assignments
        nonlocal board_occupations

        row = len(queens)

        if n == len(queens):
            # complete assignment
            return queens
        else:
            candidate_list = []
            for i in range(n):
                if not check_under_attack(board_occupations, row, i):
                    candidate_list.append((i, count_new_occupations(board_occupations, n, row, i)))
            candidate_list = sorted(candidate_list, key = lambda v: v[1])

            for i, _ in  candidate_list:
                add_or_remove_occupation(board_occupations, n, row, i, True)

                newqueens = rsolve(queens+[i],n)  # recursive call with new assignment
                num_assignments += 1  # increment the num_assignments
                if newqueens != []:
                    return newqueens

                add_or_remove_occupation(board_occupations, n, row, i, False)
                    
            return []  # FAIL

    result = rsolve(queens, n)

    return (result, num_assignments)

def print_board(queens):
    """
    Method to print the board with NQueens assignment
    Args:
        queens (list): List of integers giving the row assignment for each queen
    Returns:
        None
    """
    n = len(queens)  # Assign board size
    for pos in queens:
        for i in range(pos):
            print('.', end=' ')
        print("Q", end = ' ')
        for i in range((n-pos)-1):
            print('.', end=' ')
        print()  # print new line for next row

def print_num_assign(n, num_assign):
    """
    Method to print answer for question 1
    Args:
        n (int): board size input
        num_assign (int): Number of assignments made
    Returns:
        None
    """
    print("Number of assignments for ", n, "queens =", num_assign)


def main():
    """
    Main function which calls other methods
    Args: None
    Returns : None
    """
    print_student_name_Anumber()
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", action="store", help="board size")
    args = parser.parse_args()
    n = int(args.size)
    ans, assignments_count = rsolve_q2([], n)  ### TODO : Feel free to change this to reflect the 3 algorithms for quest 1,2 and 3
    print_board(ans)
    ### TODO
    # Feel free to change the below code
    num_assign = assignments_count
    print_num_assign(n, num_assign)

if __name__ =='__main__':
    main()