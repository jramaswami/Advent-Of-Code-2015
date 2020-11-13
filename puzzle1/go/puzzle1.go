// Advent of Code 2015 :: Day 1 :: Day 1: Not Quite Lisp
package main

import (
    "fmt"
    "io/ioutil"
)

func main() {
    data, err := ioutil.ReadFile("../input.txt")
    if err != nil {
        fmt.Println("File reading error!", err)
        return
    }

    floor := 0
    basement := -1
    for i, c := range string(data) {
        if c == '(' {
            floor = floor + 1
        } else {
            floor = floor - 1
        }

        if basement == -1 && floor == -1 {
            basement = (i + 1)  // Convert to 1-based index.
        }
    }
    fmt.Println("Answer to part 1 is", floor)
    fmt.Println("Answer to part 2 is", basement)
}
