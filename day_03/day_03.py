def calculate_rates(data: list) -> dict:

    rates = {"gamma": "", "epsilon": ""}

    for i in range(len(data[0])):
        zero_count = 0
        one_count = 0
        for line in data:
            if line[i] == "0":
                zero_count += 1
            else:
                one_count += 1

        if one_count >= zero_count:
            rates["gamma"] += "1"
            rates["epsilon"] += "0"
        else:
            rates["gamma"] += "0"
            rates["epsilon"] += "1"

    return rates


def calculate_life_rates(data: list) -> dict:

    oxygen_list = data.copy()
    co2_list = data.copy()

    for i in range(len(data[0])):
        oxygen_diag_rates = calculate_rates(data=oxygen_list)
        co2_diag_rates = calculate_rates(data=co2_list)

        for item in data:
            if oxygen_diag_rates["gamma"][i] != item[i]:
                if item in oxygen_list and len(oxygen_list) > 1:
                    oxygen_list.remove(item)
            if co2_diag_rates["epsilon"][i] != item[i]:
                if item in co2_list and len(co2_list) > 1:
                    co2_list.remove(item)

    life_rates = {"oxygen": oxygen_list[0], "co2": co2_list[0]}

    return life_rates


def main():
    with open("day_03/input.txt") as f:
        diagnostics = [line.rstrip() for line in f.readlines()]

    diag_rates = calculate_rates(diagnostics)
    life_rates = calculate_life_rates(diagnostics)

    print(diag_rates)
    print("Gamma:", int(diag_rates["gamma"], 2))
    print("Epsilon:", int(diag_rates["epsilon"], 2))
    print(
        "Final measurement:",
        int(diag_rates["gamma"], 2) * int(diag_rates["epsilon"], 2),
    )
    print("--" * 10)
    print(life_rates)
    print("oxygen:", int(life_rates["oxygen"], 2))
    print("co2:", int(life_rates["co2"], 2))
    print("Life measurement", int(life_rates["oxygen"], 2) * int(life_rates["co2"], 2))


main()
