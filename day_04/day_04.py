from tools.read_file import read_file
import sys


def find_bingo_boards(data: list) -> list:
    boards = []
    board = []

    for line in data:
        if line:
            board.append(line.split())
        else:
            board = []
            boards.append(board)

    return boards


def calculate_board(boards: list, numbers: str, first_board: bool) -> int:

    marked = []
    winner_board = [False for _ in range(len(boards))]
    for board in boards:
        marked.append([[False for col in range(5)] for row in range(5)])

    for num in numbers.split(","):
        for i, board in enumerate(boards):
            for row in range(5):
                for col in range(5):
                    if board[row][col] == num:
                        marked[i][row][col] = True

            won_board = False
            for row in range(5):
                won = True
                for col in range(5):
                    if not marked[i][row][col]:
                        won = False
                if won:
                    won_board = True

            for col in range(5):
                won = True
                for row in range(5):
                    if not marked[i][row][col]:
                        won = False
                if won:
                    won_board = True

            if won_board and first_board:
                unmarked_numbers = 0
                for row in range(5):
                    for col in range(5):
                        if not marked[i][row][col]:
                            unmarked_numbers += int(board[row][col])

                return unmarked_numbers * int(num)

            elif won_board:
                winner_board[i] = True
                if all([winner_board[j] for j in range(len(boards))]):
                    unmarked_numbers = 0
                    for row in range(5):
                        for col in range(5):
                            if not marked[i][row][col]:
                                unmarked_numbers += int(board[row][col])

                    return unmarked_numbers * int(num)


def main():
    file_data = read_file("day_04/input.txt")

    loto_numbers = file_data[0]
    boards = find_bingo_boards(file_data[1:])
    first_board = calculate_board(boards, loto_numbers, True)
    last_board = calculate_board(boards, loto_numbers, False)
    print("First winning board:", first_board)
    print("Last winning board:", last_board)


main()
