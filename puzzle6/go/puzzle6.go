// Advent of Code 2015 :: Day 6: Probably a Fire Hazard

package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

type Command struct {
    cmd string
    row1 int
    col1 int
    row2 int
    col2 int
}

func turnOn(row1 int, col1 int, row2 int, col2 int, grid [][]bool) {
    for r := row1; r <= row2; r += 1 {
        for c := col1; c <= col2; c += 1 {
            grid[r][c] = true
        }
    }
}

func toggle(row1 int, col1 int, row2 int, col2 int, grid [][]bool) {
    for r := row1; r <= row2; r += 1 {
        for c := col1; c <= col2; c += 1 {
            grid[r][c] = !grid[r][c]
        }
    }
}

func turnOff(row1 int, col1 int, row2 int, col2 int, grid [][]bool) {
    for r := row1; r <= row2; r += 1 {
        for c := col1; c <= col2; c += 1 {
            grid[r][c] = false
        }
    }
}

func countLightsOn(grid [][]bool) int {
    lightsOn := 0
    for r := 0; r < 1000; r += 1 {
        for c := 0; c < 1000; c += 1 {
            if grid[r][c] {
                lightsOn += 1
            }
        }
    }
    return lightsOn
}

func turnUp(row1 int, col1 int, row2 int, col2 int, grid [][]int) {
    for r := row1; r <= row2; r += 1 {
        for c := col1; c <= col2; c += 1 {
            grid[r][c] += 1
        }
    }
}

func turnWayUp(row1 int, col1 int, row2 int, col2 int, grid [][]int) {
    for r := row1; r <= row2; r += 1 {
        for c := col1; c <= col2; c += 1 {
            grid[r][c] += 2
        }
    }
}

func turnDown(row1 int, col1 int, row2 int, col2 int, grid [][]int) {
    for r := row1; r <= row2; r += 1 {
        for c := col1; c <= col2; c += 1 {
            grid[r][c] -= 1
            if (grid[r][c] < 0) {
                grid[r][c] = 0
            }
        }
    }
}

func countBrightness(grid [][]int) int {
    brightness := 0
    for r := 0; r < 1000; r += 1 {
        for c := 0; c < 1000; c += 1 {
            brightness += grid[r][c]
        }
    }
    return brightness
}

func solve1(commands []Command) int {
    // Create grid
    grid := make([][]bool, 1000)
    for i := 0; i < 1000; i += 1 {
        grid[i] = make([]bool, 1000)
    }

    for _, command := range commands {
        switch command.cmd {
        case "turn off":
            turnOff(command.row1, command.col1, command.row2, command.col2, grid)
        case "turn on":
            turnOn(command.row1, command.col1, command.row2, command.col2, grid)
        case "toggle":
            toggle(command.row1, command.col1, command.row2, command.col2, grid)
        }
    }
    return countLightsOn(grid)
}

func solve2(commands []Command) int {
    // Create grid
    grid := make([][]int, 1000)
    for i := 0; i < 1000; i += 1 {
        grid[i] = make([]int, 1000)
    }

    for _, command := range commands {
        switch command.cmd {
        case "turn off":
            turnDown(command.row1, command.col1, command.row2, command.col2, grid)
        case "turn on":
            turnUp(command.row1, command.col1, command.row2, command.col2, grid)
        case "toggle":
            turnWayUp(command.row1, command.col1, command.row2, command.col2, grid)
        }
    }
    return countBrightness(grid)
}

func main() {

    commands := []Command{}

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        // Read
        line := scanner.Text()
        tokens := strings.Split(line, " ")
        // Parse
        cmd := tokens[0]
        if cmd == "turn" {
            cmd = cmd + " " + tokens[1]
        }
        start := 2
        end := 4
        if cmd == "toggle" {
            start = 1
            end = 3
        }
        posn := strings.Split(tokens[start], ",")
        row1, _ := strconv.Atoi(posn[0])
        col1, _ := strconv.Atoi(posn[1])
        posn = strings.Split(tokens[end], ",")
        row2, _ := strconv.Atoi(posn[0])
        col2, _ := strconv.Atoi(posn[1])

        command := Command{cmd, row1, col1, row2, col2}
        commands = append(commands, command)
    }
    fmt.Println("The solution to part 1 is", solve1(commands))
    fmt.Println("The solution to part 1 is", solve2(commands))
}
