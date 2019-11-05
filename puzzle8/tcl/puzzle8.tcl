# Advent of Code 2015 :: Day 8 :: Matchsticks

proc solve_part1 {words} {
    set total_literal_length 0
    set total_string_length 0
    foreach word $words {
        set literal_length [string length $word]
        set string_length [expr {[string length [subst $word]] - 2}]
        incr total_literal_length $literal_length
        incr total_string_length $string_length
    }
    return [expr {$total_literal_length - $total_string_length}]
}

set escapes "nabfrtv\"\\'"
proc encode_word {word} {
    global escapes
    set encoded_word ""
    set string_length [string length $word]
    for {set i 0} {$i < $string_length} {incr i} {
        set c [string index $word $i]
        if {[string equal $c "\\"]} {
            set j [expr {$i + 1}]
            set d [string index $word $j]
            if {[string first $d $escapes] >= 0} {
                set replacement "\\\\\\$d"
                set encoded_word [string cat $encoded_word $replacement]
                incr i
            } elseif [string equal $d "x"] {
                set replacement "\\\\x"
                set encoded_word [string cat $encoded_word $replacement]
                incr i
            } else {
                error "OOPS!!! $word $j $d"
            }
        } else {
            set encoded_word [string cat $encoded_word $c]
        }
    }
    return $encoded_word
}

proc solve_part2 {words} {
    set total_literal_length 0
    set total_encoded_length 0
    foreach word $words {
        set literal_length [string length $word]
        set encoded_word [encode_word $word]
        set encoded_length [expr {4 + [string length $encoded_word]}]
        incr total_literal_length $literal_length
        incr total_encoded_length $encoded_length
    }
    return [expr {$total_encoded_length - $total_literal_length}]
}


if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    set words [split $input "\n"]
    puts "The answer to part 1 is [solve_part1 $words]."
    puts "The answer to part 2 is [solve_part2 $words]."
}
