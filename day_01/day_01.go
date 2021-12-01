package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

// Read the file and return a slice of depths (integer)
func readFile(filename string) []int {
	var data []int

	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// fmt.Println(scanner.Text())
		depth, err := strconv.Atoi(scanner.Text())

		if err != nil {
			log.Fatal(err)
		}

		data = append(data, depth)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return data
}

// Count the times that the depth has been increased
func increasedDeapths(depths []int) int {
	count := 0
	for i := 0; i < len(depths)-1; i++ {
		if depths[i] < depths[i+1] {
			count++
		}
	}

	return count
}

// Count the times that sum of 3 depths have been increased
func increasedSumDeapths(depths []int) int {
	count := 0
	for i := 0; i < len(depths)-3; i++ {
		a := depths[i] + depths[i+1] + depths[i+2]
		b := depths[i+1] + depths[i+2] + depths[i+3]

		if a < b {
			count++
		}
	}

	return count
}

func main() {
	// file := "input.txt"
	data := readFile("day_01/input.txt")
	increasedCounter := increasedDeapths(data)
	increasedSumCounter := increasedSumDeapths(data)
	fmt.Println(increasedCounter)
	fmt.Println(increasedSumCounter)
}
