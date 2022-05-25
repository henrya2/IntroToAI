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

def rsolve_q1(queens, n):
    num_assignments = 0

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

        if n == len(queens):
            # complete assignment
            return queens
        else:
            for i in range(n):
                if not under_attack(i,queens):
                    newqueens = rsolve(queens+[i],n)  # recursive call with new assignment
                    num_assignments += 1  # increment the num_assignments
                    if newqueens != []:
                        return newqueens
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
    ans, assignments_count = rsolve_q1([], n)  ### TODO : Feel free to change this to reflect the 3 algorithms for quest 1,2 and 3
    print_board(ans)
    ### TODO
    # Feel free to change the below code
    num_assign = assignments_count
    print_num_assign(n, num_assign)

if __name__ =='__main__':
    main()