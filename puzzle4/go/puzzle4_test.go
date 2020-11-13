package main

import "testing"

func TestPart1 (t *testing.T) {
    key := "abcdef"
    expected := 609043
    actual := solve(key, 5)
    if (expected != actual) {
        t.Log("key", key, "expected", expected, "got", actual)
        t.Fail()
    }

    key = "pqrstuv"
    expected = 1048970
    actual = solve(key, 5)
    if (expected != actual) {
        t.Log("key", key, "expected", expected, "got", actual)
        t.Fail()
    }
}
