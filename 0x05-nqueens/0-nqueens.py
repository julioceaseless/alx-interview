#!/usr/bin/python3
"""Mock Interview: N queens puzzle"""
import sys


def print_usage_and_exit():
    """exit statement for wrong number of args"""
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    """print error message"""
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    """check if queen placement is valid"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N):
    """places queen on the board recursively"""
    if row == N:
        print_solution(board)
    else:
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1, N)


def print_solution(board):
    """
    Prints the board configuration as a
    list of [row, column] pairs
    """
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)


if __name__ == "__main__":
    """run when executed directly"""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    board = [-1] * N
    solve_nqueens(board, 0, N)
