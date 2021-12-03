package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func readFile(filename string) []string {
	var data []string

	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		data = append(data, scanner.Text())

	}

	return data
}

func calculateRates(diagnostics []string) map[string]string {
	rates := make(map[string]string)
	rates["gamma"] = ""
	rates["epsilon"] = ""

	for i := 0; i < len(diagnostics[0]); i++ {
		zeroCount := 0
		oneCount := 0
		for j := 0; j < len(diagnostics); j++ {
			if string(diagnostics[j][i]) == "0" {
				zeroCount += 1
			} else {
				oneCount += 1
			}
		}

		if oneCount >= zeroCount {
			rates["gamma"] += "1"
			rates["epsilon"] += "0"
		} else {
			rates["gamma"] += "0"
			rates["epsilon"] += "1"
		}

	}

	return rates
}

func findElement(slice []string, val string) (int, bool) {
	for i, item := range slice {
		if item == val {
			// fmt.Println(i, item)
			return i, true
		}
	}

	return -1, false
}

func calculateLifeRates(diagnostics []string) map[string]string {
	oxygenSlice := make([]string, len(diagnostics))
	co2Slice := make([]string, len(diagnostics))
	copy(oxygenSlice, diagnostics)
	copy(co2Slice, diagnostics)

	for i := 0; i < len(diagnostics[0]); i++ {
		oxygen_diag_rates := calculateRates(oxygenSlice)
		co2_diag_rates := calculateRates(co2Slice)
		// fmt.Println(oxygen_diag_rates, co2_diag_rates)

		for j := 0; j < len(diagnostics); j++ {
			// fmt.Println(oxygenSlice)

			if string(oxygen_diag_rates["gamma"][i]) != string(diagnostics[j][i]) {
				// fmt.Println(diagnostics[j])
				key, found := findElement(oxygenSlice, diagnostics[j])
				// fmt.Println(key, found)
				if found && len(oxygenSlice) > 1 {
					oxygenSlice = append(oxygenSlice[:key], oxygenSlice[key+1:]...)
				}
				// fmt.Println(key, found)
			}

			if string(co2_diag_rates["epsilon"][i]) != string(diagnostics[j][i]) {
				k, f := findElement(co2Slice, diagnostics[j])
				if f && len(co2Slice) > 1 {
					co2Slice = append(co2Slice[:k], co2Slice[k+1:]...)
				}
				// fmt.Println(key, found)
			}
		}
	}

	lifeRates := make(map[string]string)
	lifeRates["oxygen"] = oxygenSlice[0]
	lifeRates["co2"] = co2Slice[0]

	return lifeRates
}

func main() {

	diagnostics := readFile("day_03/input.txt")
	diagRates := calculateRates(diagnostics)
	lifeRates := calculateLifeRates(diagnostics)

	gamma, err := strconv.ParseInt(diagRates["gamma"], 2, 64)
	epsilon, err := strconv.ParseInt(diagRates["epsilon"], 2, 64)

	oxygen, err := strconv.ParseInt(lifeRates["oxygen"], 2, 64)
	co2, err := strconv.ParseInt(lifeRates["co2"], 2, 64)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(diagRates)
	fmt.Println("Gamma:", gamma)
	fmt.Println("Epsilon:", epsilon)
	fmt.Println("Final measurement:", gamma*epsilon)
	fmt.Println("------------")
	fmt.Println(lifeRates)
	fmt.Println("Oxygen:", oxygen)
	fmt.Println("CO2:", co2)
	fmt.Println("Life measurement:", oxygen*co2)
}
