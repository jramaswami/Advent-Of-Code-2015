# Advent of Code 2015 :: Day 19 :: Medicine for Rudolph

package require struct::set

# Parse the input into a list where the first item is the molecule
# and the second item is a list of transformations.  Each transformation
# is a list of two items: the from string and the to string.
proc parse_input {input} {
    set transformations [dict create]
    set lines [split $input "\n"]
    set num_lines [llength $lines]
    set molecule [lindex $lines end]
    set transformations {}
    set limit [expr {$num_lines - 2}]
    for {set i 0} {$i < $limit} {incr i} {
        set line [lindex $lines $i]
        set tokens [split $line]
        set from [lindex $tokens 0]
        set to [lindex $tokens 2]
        dict lappend transformations $from $to
    }
    return [list $molecule $transformations]
}

# Given a molecule and a transformation, this proc returns a set of 
# all possible new molecules that can be created with the given
# transformations.
proc possible_molecules {molecule transformations} {
    set possibles {}
    set molecule_length [string length $molecule]

    set index 0
    while {$index < $molecule_length} {
        # Atoms are either a single capital letter or a capital followed by a
        # lowercase letter.
        set atom [string index $molecule $index]
        set atom0 [string index $molecule [expr {$index + 1}]]
        if {[string is lower $atom0]} {
            set atom [string cat $atom $atom0]
        }
        if {[dict exists $transformations $atom]} {
            set lhs [string range $molecule 0 [expr {$index - 1}]]
            set rhs [string range $molecule [expr {$index + [string length $atom]}] end]
            foreach replacement [dict get $transformations $atom] {
                ::struct::set include possibles [string cat $lhs $replacement $rhs]
            }
        }
        incr index [string length $atom]
    }
    return $possibles
}

# Return the number of unique molecules that can be formed by one round
# of all the given transformations.
proc solve_part1 {molecule transformations} {
    set possibles [possible_molecules $molecule $transformations]
    return [::struct::set size $possibles]
}

# Based on the solutoin of u/askalski
# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju/
proc solve_part2 {molecule} {
    set molecule_length [string length $molecule]
    set atoms {}
    set atom_count 0
    set atom_Ar_Rn_count 0
    set atom_Y_count 0
    set index 0
    while {$index < $molecule_length} {
        # Atoms are either a single capital letter or a capital followed by a
        # lowercase letter.
        set atom [string index $molecule $index]
        set atom0 [string index $molecule [expr {$index + 1}]]
        if {[string is lower $atom0]} {
            set atom [string cat $atom $atom0]
        }
        lappend atoms $atom
        incr atom_count
        if {$atom == "Ar" || $atom == "Rn"} {
            incr atom_Ar_Rn_count
        }
        if {$atom == Y} {
            incr atom_Y_count
        }
        incr index [string length $atom]
    }
    return [expr {$atom_count - $atom_Ar_Rn_count - (2 * $atom_Y_count) - 1}]
}

if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    set parsed [parse_input $input]
    set molecule [lindex $parsed 0]
    set transformations [lindex $parsed 1]
    puts "The solution to part 1 is [solve_part1 $molecule $transformations]."
    puts "The solution to part 2 is [solve_part2 $molecule]."
}
