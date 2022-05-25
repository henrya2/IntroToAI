import argparse

from collections import deque
import copy

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

def rsolve_q3(queens, n):
    num_assignments = 0

    # Initialize the domain
    domain = [[j for j in range(n)] for i in range(n)]

    def check_two_queen_attack(q1, q2):
        return q1[0] == q2[0] or q1[1] == q2[1] or \
            abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

    def revise_domain(n, domain, x_i, x_j):
        revised = False
        d_i = domain[x_i]
        d_j = domain[x_j]

        d_i_op = copy.deepcopy(d_i)

        for x in d_i:
            all_violate = True
            for y in d_j:
                if not check_two_queen_attack((x_i, x), (x_j, y)):
                    all_violate = False
                    break
            if all_violate:
                revised = True
                d_i_op.remove(x)

        if revised:
            domain[x_i] = d_i_op

        return revised

    def inference_ac3(domain, n, new_row, new_col):
        cand_queue = deque()

        for i in range(new_row + 1, n):
            cand_queue.append((i, new_row))

        while len(cand_queue) > 0:
            (x_i, x_j) = cand_queue.popleft()
            if revise_domain(n, domain, x_i, x_j):
                if len(domain[x_i]) == 0:
                    return False
                # propragation
                for x_k in range(new_row + 1, n):
                    if x_k != x_i and x_k != x_j:
                        if not ((x_k, x_i) in cand_queue):
                            cand_queue.append((x_k, x_i))
        return True  

    def rsolve(queens,n,domain):
        """
        Recursively find solution for NQueens problem
        Args:
            queens (list): List of integers. Each int gives the row assignment for the queen in a column
            n (int): Board size
            domain (list): Each row's domain
        Returns:
            (list) : NQueens assignment as a list of integers. If no assignment is possible, returns empty list
        """
        nonlocal num_assignments

        row = len(queens)

        if n == len(queens):
            # complete assignment
            return queens
        else:
            row_domain = domain[row]
            for i in row_domain:
                    if not under_attack(i, queens):
                        num_assignments += 1  # increment the num_assignments

                        new_domain = copy.deepcopy(domain)
                        new_domain[row] = [i]

                        inference_result = inference_ac3(new_domain, n, row, i)
                        if inference_result:
                            newqueens = rsolve(queens + [i],n, new_domain)  # recursive call with new assignment
                            if newqueens != []:
                                return newqueens
                    
            return []  # FAIL

    result = rsolve(queens, n, domain)

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
    ans, assignments_count = rsolve_q3([], n)  ### TODO : Feel free to change this to reflect the 3 algorithms for quest 1,2 and 3
    print_board(ans)
    ### TODO
    # Feel free to change the below code
    num_assign = assignments_count
    print_num_assign(n, num_assign)

if __name__ =='__main__':
    main()