// Advent of Code 2015 :: Day 4 :: The Ideal Stocking Stuffer

package main

import (
    "crypto/md5"
    "fmt"
    "strconv"
    "strings"
)


func md5Hash(key string) string {
    data := []byte(key)
    hash := fmt.Sprintf("%x", md5.Sum(data))
    return hash
}

func solve(secretKey string, k int) int {
    index := 1
    key := secretKey + strconv.Itoa(index)
    hash := md5Hash(key)
    prefix := strings.Repeat("0", k)
    for !strings.HasPrefix(hash, prefix) {
        index += 1
        key = secretKey + strconv.Itoa(index)
        hash = md5Hash(key)
    }
    return index
}

func main() {
    secretKey := "iwrupvqb"
    fmt.Println("The answer to part 1 is", solve(secretKey, 5))
    fmt.Println("The answer to part 2 is", solve(secretKey, 6))
}
