def count_larger_measurements(data):
    count = 0

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1

    return count


def count_larger_sums(data):
    count = 0

    for i in range(0, len(data) - 3):
        a = data[i] + data[i + 1] + data[i + 2]
        b = data[i + 1] + data[i + 2] + data[i + 3]
        if b > a:
            count += 1

    return count


def main():
    with open("day_01/input.txt") as f:
        measurements = [int(x) for x in f.readlines()]

    print(count_larger_measurements(measurements))

    print(count_larger_sums(measurements))


main()
