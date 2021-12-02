package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
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

func measure_changes(positions []string) map[string]int {
	location := make(map[string]int)
	location["forward"] = 0
	location["depth"] = 0

	for i := 0; i < len(positions); i++ {
		move := strings.Split(positions[i], " ")
		moveType := move[0]
		moveChange, err := strconv.Atoi(move[1])
		if err != nil {
			log.Fatal(err)
		}

		if moveType == "forward" {
			location["forward"] += moveChange
		} else if moveType == "down" {
			location["depth"] += moveChange
		} else {
			location["depth"] -= moveChange
		}

	}
	return location
}

func measure_changes_aim(positions []string) map[string]int {
	location := make(map[string]int)
	location["forward"] = 0
	location["depth"] = 0
	location["aim"] = 0

	for i := 0; i < len(positions); i++ {
		move := strings.Split(positions[i], " ")
		moveType := move[0]
		moveChange, err := strconv.Atoi(move[1])
		if err != nil {
			log.Fatal(err)
		}

		if moveType == "forward" {
			location["forward"] += moveChange
			location["depth"] += moveChange * location["aim"]
		} else if moveType == "down" {
			location["aim"] += moveChange
		} else {
			location["aim"] -= moveChange
		}
	}

	return location
}

func main() {
	positions := readFile("day_02/input.txt")
	location := measure_changes(positions)
	locationAim := measure_changes_aim(positions)

	finalDest := location["forward"] * location["depth"]
	finalDestAim := locationAim["forward"] * locationAim["depth"]
	fmt.Println(finalDest)
	fmt.Println(finalDestAim)
}
