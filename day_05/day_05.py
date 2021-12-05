from typing import Tuple
from tools.read_file import read_file


def normalize_data(data_list: list) -> Tuple[list, int, int]:

    lines_list = []
    max_x = 0
    max_y = 0

    for line in data_list:
        line_pos = {}
        line_calc = line.replace(" ", "").split("->")
        line_pos["x1"] = int(line_calc[0].split(",")[0])
        line_pos["y1"] = int(line_calc[0].split(",")[1])
        line_pos["x2"] = int(line_calc[1].split(",")[0])
        line_pos["y2"] = int(line_calc[1].split(",")[1])
        if line_pos["x1"] > max_x:
            max_x = line_pos["x1"]
        elif line_pos["x2"] > max_x:
            max_x = line_pos["x2"]

        if line_pos["y1"] > max_y:
            max_y = line_pos["y1"]
        elif line_pos["y2"] > max_y:
            max_y = line_pos["y2"]

        lines_list.append(line_pos)

    return lines_list, max_x, max_y


def calculate_board(
    lines_list: list, max_x: int, max_y: int, diagonal: bool
) -> list:

    board = [[0 for col in range(max_y + 1)] for row in range(max_x + 1)]

    for line in lines_list:
        x1 = line["x1"]
        x2 = line["x2"]
        y1 = line["y1"]
        y2 = line["y2"]
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                board[x1][i] += 1

        elif y1 == y2:
            for i in range(min(x1, x2), max(x1,x2) + 1):
                board[i][y1] += 1

        elif diagonal:              
            if (x1 < x2):
               for i in range(x2 - x1 + 1):
                   if y1 < y2:
                        board[x1 + i][y1 + i] += 1
                   elif y1 > y2:
                       board[x1 + i][y1 - i] += 1
            elif x1 > x2:
                for i in range(x1 - x2 + 1):
                    if y1 < y2:
                        board[x1 - i][y1 + i] += 1
                    elif y1 > y2:
                        board[x1 - i][y1 - i] += 1
    

    return board


def main():
    file_data = read_file("day_05/input.txt")

    lines_list, max_x, max_y = normalize_data(file_data)
    first_board = calculate_board(lines_list, max_x, max_y, False)
    board_counter = 0
    for row in range(max_x):
        for col in range(max_y):
            if first_board[row][col] >= 2:
                board_counter += 1

    print("First puzzle lines:", board_counter)

    second_board = calculate_board(lines_list, max_x, max_y, True)
    board_counter = 0
    for row in range(max_x):
        for col in range(max_y):
            if second_board[row][col] >= 2:
                board_counter += 1
    print("Second puzzle lines:", board_counter)


main()
