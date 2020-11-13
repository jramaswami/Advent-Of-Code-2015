// Advent of Code 2015 :: Day 5: Doesn't He Have Intern-Elves For This?
// Tests

package main

import "testing"

func TestHasThreeVowels(t * testing.T) {
    s := "aei"
    expected := true
    actual := hasThreeVowels([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = "xazegov"
    expected = true
    actual = hasThreeVowels([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = "aeiouaeiouaeiou"
    expected = true
    actual = hasThreeVowels([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = "axxxxxxu"
    expected = false
    actual = hasThreeVowels([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }
}

func TestHasRepeatedPair(t *testing.T) {
    s := "xx"
    expected := true
    actual := hasRepeatedPair([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = "abcdde"
    expected = true
    actual = hasRepeatedPair([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = "aabbccdd"
    expected = true
    actual = hasRepeatedPair([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }
    s = "axaxbxbxcxcxdxd"
    expected = false
    actual = hasRepeatedPair([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }
}

func TestHasForbiddenPairs(t *testing.T) {
    s := "xx"
    expected := false
    actual := hasForbiddenPair([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = "xy"
    expected = true
    actual = hasForbiddenPair([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = "xzy"
    expected = false
    actual = hasForbiddenPair([]byte(s))
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }
}

func TestNice1(t *testing.T) {
    s := []byte("ugknbfddgicrmopn")
    expected := true
    actual := nice1(s)
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = []byte("aaa")
    expected = true
    actual = nice1(s)
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = []byte("jchzalrnumimnmhp")
    expected = false
    actual = nice1(s)
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = []byte("haegwjzuvuyypxyu")
    expected = false
    actual = nice1(s)
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = []byte("dvszwmarrgswjxmb")
    expected = false
    actual = nice1(s)
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }
}

func TestHasNonOverlappingPairs(t *testing.T) {
    s := "xyxy"
    expected := true
    actual := hasNonOverlappingPair([]byte(s))
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = "xxyxx"
    expected = true
    actual = hasNonOverlappingPair([]byte(s))
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = "aabcdefgaa"
    expected = true
    actual = hasNonOverlappingPair([]byte(s))
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = "aaa"
    expected = false
    actual = hasNonOverlappingPair([]byte(s))
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }
}

func TestHasGappedRepeatedLetter(t *testing.T) {
    s := "xyx"
    expected := true
    actual := hasGappedRepeatedLetter([]byte(s))
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = "abcdefeghi"
    expected = true
    actual = hasGappedRepeatedLetter([]byte(s))
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = "aaa"
    expected = true
    actual = hasGappedRepeatedLetter([]byte(s))
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

    s = "abcabc"
    expected = false
    actual = hasGappedRepeatedLetter([]byte(s))
    if (expected != actual) {
        t.Log(s, "expected", expected, "got", actual)
        t.Fail()
    }

}

func TestNice2(t *testing.T) {
    s := []byte("qjhvhtzxzqqjkmpb")
    expected := true
    actual := nice2(s)
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = []byte("xxyxx")
    expected = true
    actual = nice2(s)
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = []byte("uurcxstgmygtbstg")
    expected = false
    actual = nice2(s)
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }

    s = []byte("ieodomkazucvgmuy")
    expected = false
    actual = nice2(s)
    if (expected != actual) {
        t.Log(string(s), "expected", expected, "got", actual)
        t.Fail()
    }
}
