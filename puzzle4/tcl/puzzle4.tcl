# Advent of Code 2015 :: Day 4 :: The Ideal Stocking Stuffer

package require md5

proc prefix_zeros {hash} {
    set idx 0
    while {[string index $hash $idx] == 0} {
        incr idx 
    }
    return $idx
}

proc solve {input} {
    set idx 1
    set hash [::md5::md5 -hex "${input}${idx}"]
    set five_zeros 0
    set six_zeros 0
    # puts "$idx $hash"
    while {![expr {$five_zeros && $six_zeros}]} {
        set zeros [prefix_zeros $hash]
        if {[expr {!$five_zeros && $zeros >= 5}]} {
            set five_zeros $idx
        }
        if {[expr {$zeros >= 6}]} {
            set six_zeros $idx
        }
        incr idx
        set hash [::md5::md5 -hex "${input}${idx}"]
    }
    return [list $five_zeros $six_zeros]
}

if {!$tcl_interactive} {
    set input iwrupvqb
    set soln [solve $input]
    puts "The answer to part 1 is [lindex $soln 0]."
    puts "The answer to part 2 is [lindex $soln 1]."
}
