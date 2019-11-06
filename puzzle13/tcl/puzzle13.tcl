# Advent of Code 2015 :: Day 13 :: Knights of the Dinner Table
package require math

proc next_permutation {lst} {
    # Find the largest index k such that a[k] < a[k + 1]. 
    # If no such index exists, the permutation is the last permutation.
    set list_length [llength $lst]
    set search_limit [expr {$list_length - 1}]
    set k -1
    set i 0
    for {set i 0} {$i < $search_limit} {incr i} {
        set a [lindex $lst $i]
        set b [lindex $lst [expr {$i+1}]]
        if {[string compare $a $b] < 0} {
            set k $i
        }
    }

    if {$k == -1} {
        return {}
    }

    # Find the largest index l greater than k such that a[k] < a[l].
    set ak [lindex $lst $k]
    set l -1
    for {set i [expr {$k+1}]} {$i < $list_length} {incr i} {
        set al [lindex $lst $i]
        if {[string compare $ak $al] < 0} {
            set l $i
        }
    }

    # Swap the value of a[k] with that of a[l].
    set t [lindex $lst $k]
    lset lst $k [lindex $lst $l]
    lset lst $l $t

    # Reverse the sequence from a[k + 1] up to and including the 
    # final element a[n].
    set lst0 [lrange $lst 0 $k]
    set tail [lreverse [lrange $lst [expr {$k+1}] end]]
    lappend lst0 {*}$tail
    return $lst0
}

proc happiness_change {arrangement} {
    set total 0
    set n [llength $arrangement]
    for {set i 0} {$i < $n} {incr i} {
        set h [expr {$i - 1}]
        if {$h < 0} {
            set h [expr {$n - 1}]
        }
        set j [expr {$i + 1}]
        if {$j == $n} {
            set j 0
        }

        set left [lindex $arrangement $h]
        set attendee [lindex $arrangement $i]
        set right [lindex $arrangement $j]

        set left_delta [set ::${attendee}(${left})]
        set right_delta [set ::${attendee}(${right})]
        incr total $left_delta
        incr total $right_delta
    }
    return $total
}

proc optimal_happiness_change {attendees} {
    set arrangement [lsort $attendees]
    set soln -1000000
    while {$arrangement != {}} {
        set h [happiness_change $arrangement]
        set soln [::math::max $h $soln]
        set arrangement [next_permutation $arrangement]
    }
    return $soln
}

if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    set lines [split $input "\n"]
    set attendees {}
    foreach line $lines {
        set tokens [split $line]
        set attendee_a [lindex $tokens 0]
        set attendee_b [string range [lindex $tokens end] 0 end-1]
        set sign 1
        if {[string compare [lindex $tokens 2] "lose"] == 0} {
            set sign -1
        }
        set delta [lindex $tokens 3]
        set ${attendee_a}(${attendee_b}) [expr {$sign * $delta}]
        if {[lsearch $attendees $attendee_a] == -1} {
            lappend attendees $attendee_a
        }
        if {[lsearch $attendees $attendee_b] == -1} {
            lappend attendees $attendee_b
        }
    }
    puts "The answer to part 1 is [optimal_happiness_change $attendees]."

    foreach attendee $attendees {
        set ${attendee}(Joseph) 0
        set Joseph($attendee) 0
    }
    lappend attendees Joseph
    puts "The answer to part 2 is [optimal_happiness_change $attendees]."
}
