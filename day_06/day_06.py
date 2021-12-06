from tools.read_file import read_file


def calculate_fish(data: list, days: int) -> list:

    fish_list = [int(x) for x in data]
    fish_map = {k: 0 for k in range(9)}

    for fish in fish_list:
        fish_map[fish] += 1

    for day in range(days):
        new_fish_map = {k: 0 for k in range(9)}
        for key, value in fish_map.items():
            if key == 0:
                new_fish_map[6] += value
                new_fish_map[8] += value
            else:
                new_fish_map[key - 1] += value

        fish_map = new_fish_map
        # initial_zero = fish_map[0]
        # fish_map[0] = fish_map[1]
        # fish_map[1] = fish_map[2]
        # fish_map[2] = fish_map[3]
        # fish_map[3] = fish_map[4]
        # fish_map[4] = fish_map[5]
        # fish_map[5] = fish_map[6]
        # fish_map[6] = fish_map[7] + initial_zero
        # fish_map[7] = fish_map[8]
        # fish_map[8] = initial_zero

    return fish_map


def main():
    file_data = read_file("day_06/input.txt")
    file_data = file_data[0].split(",")

    fish_map = calculate_fish(file_data, 80)
    print(fish_map)
    print("Sum after 80 days:", sum(fish_map.values()))
    fish_map = calculate_fish(file_data, 256)
    print(fish_map)
    print("Sum after 256 days:", sum(fish_map.values()))



main()
