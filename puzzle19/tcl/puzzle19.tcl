# Advent of Code 2015 :: Day 19 :: Medicine for Rudolph

# Parse the input into a list where the first item is the molecule
# and the second item is a list of transformations.  Each transformation
# is a list of two items: the from string and the to string.
proc parse_input {input} {
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
        lappend transformations [list $from $to]
    }
    return [list $molecule $transformations]
}

# Given a molecule and a transformation, append to the given list (by ref)
# any new molecules that are formed by the given transformation.
proc append_possible_transformations {molecule transformation accumulator_name} {
    upvar $accumulator_name possibles
    set start_search 0
    set search_limit [string length $molecule]
    set from [lindex $transformation 0]
    set from_length [string length $from]
    set to [lindex $transformation 1]
    set to_length [string length $to]

    set index [string first $from $molecule $start_search]
    while {$index >= 0 && $index < $search_limit} {
        set index_end [expr {$index + $from_length - 1}]
        set molecule0 [string replace $molecule $index $index_end $to]
        if {[lsearch $possibles $molecule0] < 0} {
            lappend possibles $molecule0
        }
        set start_search [expr {$index + $from_length}]
        set index [string first $from $molecule $start_search]
    }
}

# Return the number of unique molecules that can be formed by one round
# of all the given transformations.
proc solve_part1 {molecule transformations} {
    set possible_molecules {}
    foreach transformation $transformations {
        append_possible_transformations $molecule $transformation possible_molecules
    }
    return [llength $possible_molecules]
}

proc reverse_transformations {transformations} {
    for {set i 0} {$i < [llength $transformations]} {incr i} {
        set t [lindex $transformations $i]
        set from [lindex $t 0]
        set to [lindex $t 1]
        set t0 [list $to $from]
        lset transformations $i $t0
    }
    return $transformations
}

proc solve_part2 {molecule transformations} {
    set molecule_length [string length $molecule]
    set queue [list e]
    set new_queue {}
    set ticks 0
    while {1} {
        incr ticks
        foreach transformation $transformations {
            foreach medicine $queue {
                if {[string length $medicine] <= $molecule_length} {
                    append_possible_transformations $medicine $transformation new_queue
                }
            }
        }
        puts "$ticks [llength $new_queue]"
        if {[lsearch $new_queue $medicine] >= 0} {
            return $ticks
        }
        set queue $new_queue
        set new_queue {}
    }
}

if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    set parsed [parse_input $input]
    set molecule [lindex $parsed 0]
    set transformations [lindex $parsed 1]
    puts "The solution to part 1 is [solve_part1 $molecule $transformations]."
    puts "The solution to part 2 is [solve_part2 $molecule $transformations]."
}
