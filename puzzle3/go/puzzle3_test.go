// Advent of Code 2015 :: Day 3 :: Perfectly Spherical Houses in a Vacuum
package main

import "testing"

func TestPart1(t *testing.T) {
    expected := 2
    actual := solve1(">")
    if expected != actual {
        t.Errorf("Test failed: expected %d; got %d", expected, actual)
    }
    expected = 4
    actual = solve1("^>v<")
    if expected != actual {
        t.Errorf("Test failed: expected %d; got %d", expected, actual)
    }
    expected = 2
    actual = solve1("^v^v^v^v^v")
    if expected != actual {
        t.Errorf("Test failed: expected %d; got %d", expected, actual)
    }
}

func TestPart2(t *testing.T) {
    expected := 3
    actual := solve2("^v")
    if expected != actual {
        t.Errorf("Test failed: expected %d; got %d", expected, actual)
    }
    expected = 3
    actual = solve2("^>v<")
    if expected != actual {
        t.Errorf("Test failed: expected %d; got %d", expected, actual)
    }
    expected = 11
    actual = solve2("^v^v^v^v^v")
    if expected != actual {
        t.Errorf("Test failed: expected %d; got %d", expected, actual)
    }
}
