from tools.read_file import read_file



def find_position(data: list, expensive: bool) -> float:
    data.sort()
    minfuel = float("inf")

    for i in range(min(data), max(data) + 1):
        fuel = 0

        for pos in data:
            distance = abs(pos - i)

            if not expensive:
                fuel += distance
            else:
                for j in range(1, distance + 1):
                    fuel += j

        if minfuel > fuel:
            minfuel = fuel

    return minfuel


def main():
    file_data = read_file("day_07/input.txt")
    file_data = [int(x) for x in file_data[0].split(",")]

    fuel = find_position(file_data, False)
    print(fuel)
    fuel = find_position(file_data, True)
    print(fuel)
    # print("average:", sum(file_data) / len(file_data))



main()
