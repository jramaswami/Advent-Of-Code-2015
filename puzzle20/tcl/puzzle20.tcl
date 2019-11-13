# Advent of Code 2015 :: Day 20 :: Infinite Elves and Infinite Houses

package require math::numtheory

proc divisors {n} {
    if {$n == 1} { return [list 1] }
    set divs [list 1]
    for {set i 2} {[expr {$i*$i}] <= $n} {incr i} {
        if {!([expr {$n % $i}])} {
            lappend divs $i
            if {[expr {$i*$i}] < $n} {
                lappend divs [expr {$n / $i}]
            }
        }
    }
    lappend divs $n
    return $divs
}

proc solve {input} {
    set soln1 0
    set soln2 0
    set house 1
    while {1} {
        if {[expr {$house % 100000 == 0}]} {
            puts "$house ..."
        }
        set presents1 0
        set presents2 0
        foreach divisor [divisors $house] {
            incr presents1 [expr {10 * $divisor}]
            if {[expr {$divisor * 50}] >= $house} {
                incr presents2 [expr {11 * $divisor}]
            }
        }
        #puts "$house $presents1 $presents2"

        if {!$soln1 && $presents1 >= $input} {
            set soln1 $house
        }

        if {!$soln2 && $presents2 >= $input} {
            set soln2 $house
            return [list $soln1 $soln2]
        }

        incr house
    }
}

if {!$tcl_interactive} {
    set input 34000000
    set solns [solve $input]
    puts "The solution to part 1 is [lindex $solns 0]."
    puts "The solution to part 2 is [lindex $solns 1]."
}
