# Advent of Code 2015 :: Day 5 :: Doesn't He Have Intern-Elves For This?

proc is_vowel {c} {
    set i [string first $c aeiou]
    return [expr {$i >= 0}]
}

proc is_prohibited {cc} {
    set i [string first $cc "ab cd pq xy"]
    return [expr {$i >= 0}]
}

proc is_double {cc} {
    return [expr {[string index $cc 0] == [string index $cc 1]}]
}


proc is_valid_string_part1 {str} {
    set str_length [string length $str]
    set limit [expr {$str_length - 1}]
    set vowels 0
    set doubles 0

    for {set i 0} {$i < $limit} {incr i} {
        set c [string index $str $i]
        if {[is_vowel $c]} {
            incr vowels
        }
        set cc [string range $str $i [expr {$i + 1}]]
        if {[is_double $cc]} {
            incr doubles
        }
        if {[is_prohibited $cc]} {
            return 0
        }
    }

    set c [string index $str $limit]
    if {[is_vowel $c]} {
        incr vowels
    }

    if {[expr {$vowels < 3}]} {
        return 0
    }
    if {[expr {$doubles == 0}]} {
        return 0
    }
    return 1
}

proc solve_part1 {words} {
    set soln 0
    foreach word $words {
        set valid [is_valid_string_part1 $word]
        if {$valid} {
            incr soln
        }
    }
    return $soln
}

proc has_valid_pair {str} {
    set str_length [string length $str]
    set limit [expr {$str_length - 1}]

    for {set i 0} {$i < $limit} {incr i} {
        set cc [string range $str $i [expr {$i + 1}]]
        set double_exists [info exists doubles($cc)]
        if {$double_exists} {
            set double_index [set doubles($cc)]
            if {$double_index < [expr {$i - 1}]} {
                return 1
            }
        } else {
            set doubles($cc) $i
        }
    }
    return 0
}

proc has_valid_triple {str} {
    set str_length [string length $str]
    set limit [expr {$str_length - 2}]

    for {set i 0} {$i < $limit} {incr i} {
        set c1 [string index $str $i]
        set c3 [string index $str [expr {$i + 2}]]
        if {$c1 == $c3} {
            return 1
        }
    }
    return 0
}

proc is_valid_string_part2 {str} {
    return [expr {[has_valid_pair $str] && [has_valid_triple $str]}]
}

proc solve_part2 {words} {
    set soln 0
    foreach word $words {
        set valid [is_valid_string_part2 $word]
        if {$valid} {
            incr soln
        }
    }
    return $soln
}

if {!$tcl_interactive} {
    set file_name [open "../input.txt"]
    set input [string trimright [read $file_name]]
    set words [split $input "\n"]
    puts "The solution to part in is [solve_part1 $words]."
    puts "The solution to part in is [solve_part2 $words]."
}
