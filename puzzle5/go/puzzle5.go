// Advent of Code 2015 :: Day 5: Doesn't He Have Intern-Elves For This?

package main

import (
    "bufio"
    "fmt"
    "os"
)

// Global containing vowels
var vowels = [5]byte{'a', 'e', 'i', 'o', 'u'}

func isVowel(c byte) bool {
    switch c {
    case 'a', 'e', 'i', 'o', 'u':
        return true
    default:
        return false
    }
}

func hasThreeVowels(s []byte) bool {
    vowelsFound := 0
    for _, c := range s {
        if isVowel(c) {
            vowelsFound += 1
        }
    }
    return vowelsFound >= 3
}

func hasRepeatedPair(s []byte) bool {
    for i, _ := range s {
        if i + 1 < len(s) {
            if s[i] == s[i+1] {
                return true
            }
        }
    }
    return false
}

func isForbiddenPair(c byte, d byte) bool {
    if c == 'a' && d == 'b' {
        return true
    } else if c == 'c' && d == 'd' {
        return true
    } else if c == 'p' && d == 'q' {
        return true
    } else if c == 'x' && d == 'y' {
        return true
    }
    return false
}

func hasForbiddenPair(s []byte) bool {
    for i, _ := range s {
        if i + 1 < len(s) {
            if isForbiddenPair(s[i], s[i+1]) {
                return true
            }
        }
    }
    return false
}

func nice1(s []byte) bool {
    return hasThreeVowels(s) && !hasForbiddenPair(s) && hasRepeatedPair(s)
}

func hasNonOverlappingPair(s []byte) bool {
    pairs := make(map[[2]byte][]int)
    for i := 0; i < len(s); i += 1 {
        if i + 1 < len(s) {
            var k = [2]byte{s[i], s[i+1]}
            for _, p := range pairs[k] {
                if p + 1 < i {
                    return true
                }
            }
            pairs[k] = append(pairs[k], i)
        }
    }
    return false
}

func hasGappedRepeatedLetter(s []byte) bool {
    for i, c := range(s) {
        if i + 2 < len(s) {
            if c == s[i+2] {
                return true
            }
        }
    }
    return false
}

func nice2(s []byte) bool {
    return hasNonOverlappingPair(s) && hasGappedRepeatedLetter(s)
}

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    solution1 := 0
    solution2 := 0
    for scanner.Scan() {
        s := []byte(scanner.Text())
        if (nice1(s)) {
            solution1 += 1
        }
        if (nice2(s)) {
            solution2 += 1
        }
    }
    fmt.Println("The solution to part 1 is", solution1)
    fmt.Println("The solution to part 2 is", solution2)
}
