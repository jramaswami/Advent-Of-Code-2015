# Advent of Code 2015 :: Day 19 :: Medicine for Rudolph

package require struct::set

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

# Given a molecule and a transformation, this proc returns a set of 
# all possible new molecules that can be created with the given
# transformation.
proc possible_molecules {molecule transformation} {
    set possibles {}
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
        ::struct::set include possibles $molecule0
        set start_search [expr {$index + 1}]
        set index [string first $from $molecule $start_search]
    }
    return $possibles
}

# Return the number of unique molecules that can be formed by one round
# of all the given transformations.
proc solve_part1 {molecule transformations} {
    set possibles {}
    foreach transformation $transformations {
        set possibles0 [possible_molecules $molecule $transformation]
        ::struct::set add possibles $possibles0
    }
    return [::struct::set size $possibles]
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

proc solve_part2_in_reverse {molecule transformations} {
    set transformations0 [reverse_transformations $transformations]
    set molecule_length [string length $molecule]
    ::struct::set include visited $molecule
    ::struct::set include queue $molecule
    set ticks 0
    while {1} {
        incr ticks
        foreach transformation $transformations0 {
            foreach medicine $queue {
                set possibles [possible_molecules $medicine $transformation]
                foreach possible $possibles {
                    if {[::struct::set contains $visited $possible]} {
                        continue
                    }
                    if {[string compare e $medicine] == 0} {
                        return $ticks
                    }
                    ::struct::set include visited $possible
                    ::struct::set include new_queue $possible
                }
            }
        }
        puts "$ticks [::struct::set size $new_queue]"
        set queue $new_queue
        set new_queue {}
    }
}

proc solve_part2 {molecule transformations} {
    set molecule_length [string length $molecule]
    ::struct::set include visited e
    ::struct::set include queue e
    set ticks 0
    while {1} {
        incr ticks
        foreach transformation $transformations {
            foreach medicine $queue {
                set possibles [possible_molecules $medicine $transformation]
                foreach possible $possibles {
                    if {[string length $possible] > $molecule_length} {
                        continue
                    }
                    if {[::struct::set contains $visited $possible]} {
                        continue
                    }
                    if {[string compare $molecule $medicine] == 0} {
                        return $ticks
                    }
                    ::struct::set include visited $possible
                    ::struct::set include new_queue $possible
                }
            }
        }
        puts "$ticks [::struct::set size $new_queue]"
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
    puts "The solution to part 2 is [solve_part2_in_reverse $molecule $transformations]."
}
