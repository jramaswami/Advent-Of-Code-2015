// Advent of Code 2015 :: Day 3 :: Perfectly Spherical Houses in a Vacuum
package main

import (
    "bufio"
    "fmt"
    "os"
)

type Position struct {
    x int
    y int
}

func move(posn Position, dirn rune) Position {
    if dirn == '>' {
        return Position{posn.x + 1, posn.y}
    } else if dirn == '<' {
        return Position{posn.x - 1, posn.y}
    } else if dirn == '^' {
        return Position{posn.x, posn.y + 1}
    } else {
        return Position{posn.x, posn.y - 1}
    }
}

func solve1(directions string) int {
    posn := Position{0, 0}
    var visited = make(map[Position]bool)
    soln := 1
    visited[posn] = true

    for _, dirn := range directions {
        posn = move(posn, dirn)
        _, v := visited[posn]
        if !v {
            visited[posn] = true
            soln = soln + 1
        }
    }
    return soln
}

func solve2(directions string) int {
    santaPosn := Position{0, 0}
    robotPosn := Position{0, 0}
    var visited = make(map[Position]bool)
    soln := 1
    visited[santaPosn] = true

    for i, dirn := range directions {
        if i % 2 > 0 {
            robotPosn = move(robotPosn, dirn)
            _, v := visited[robotPosn]
            if !v {
                visited[robotPosn] = true
                soln = soln + 1
            }
        } else {
            santaPosn = move(santaPosn, dirn)
            _, v := visited[santaPosn]
            if !v {
                visited[santaPosn] = true
                soln = soln + 1
            }
        }
    }
    return soln
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()
    directions := scanner.Text()
    fmt.Println("The answer to part 1 is", solve1(directions))
    fmt.Println("The answer to part 2 is", solve2(directions))
}
