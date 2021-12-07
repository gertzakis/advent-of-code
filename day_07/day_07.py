from tools.read_file import read_file



def find_position(data: list):
    data.sort()
    position = 0
    med =data[len(data) // 2]

    for pos in data:
        position += abs(pos - med)
        
    return position


def main():
    file_data = read_file("day_07/input.txt")
    file_data = [int(x) for x in file_data[0].split(",")]

    position = find_position(file_data)
    print(position)
    # position = find_expensive_position(file_data)
    # print(position)
    # print("average:", sum(file_data) / len(file_data))



main()
