// Advent of Code 2015 :: Day 2 :: I Was Told There Would Be No Math
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func min(a, b, c int) int {
    if (a <= b && a <= c) {
        return a
    } else if (b <= a && b <= c) {
        return b
    } else {
        return c
    }
}

func min2(a, b, c int) (int, int) {
    if (a >= b && a >= c) {
        return b, c
    } else if (b >= a && b >= c) {
        return a, c
    } else {
        return a, b
    }
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    paper := 0
    ribbon := 0
    for scanner.Scan() {
        line := scanner.Text()
        tokens := strings.Split(line, "x")
        l, _ := strconv.Atoi(tokens[0])
        w, _ := strconv.Atoi(tokens[1])
        h, _ := strconv.Atoi(tokens[2])

        paper = paper + (2 * l * w) + (2 * w * h) + (2 * h * l)
        paper = paper + min((l * w), (w * h), (h * l))

        r1, r2 := min2(l, w, h)
        ribbon = ribbon + (r1 + r1 + r2 + r2) + (l * w * h)
    }
    fmt.Println("The answer to part 1 is", paper)
    fmt.Println("The answer to part 2 is", ribbon)
}
