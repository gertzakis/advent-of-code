

def measure_changes(data):

    position = {"forward": 0, "depth": 0}
    for item in data:
        move = item.split()
        if move[0] == "forward":
            position["forward"] += int(move[1])
        elif move[0] == "down":
            position["depth"] += int(move[1])
        else:
            position["depth"] -= int(move[1])
    
    return position


def measure_changes_aim(data):

    position = {"forward": 0, "depth": 0, "aim": 0}
    for item in data:
        move = item.split()
        if move[0] == "forward":
            position["forward"] += int(move[1])
            position["depth"] += int(move[1]) * position["aim"]
        elif move[0] == "down":
            position["aim"] += int(move[1])
        else:
            position["aim"] -= int(move[1])
    
    return position


def main():
    with open("day_02/input.txt") as f:
        positions = [line.rstrip() for line in f.readlines()]

    position = measure_changes(positions)
    # print(position)
    final_dest = position["forward"] * position["depth"]
    print(final_dest)

    position_with_aim = measure_changes_aim(positions)
    final_dest = position_with_aim["forward"] * position_with_aim["depth"]
    print(final_dest)

main()
