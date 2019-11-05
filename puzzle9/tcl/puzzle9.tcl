# Advent of Code 2015 :: Day 9 :: All in a Single Night

package require struct::set
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

proc trip_distance {cities} {
    set total_distance 0
    set list_length [llength $cities]
    set limit [expr {$list_length - 1}]
    set k -1
    set i 0
    for {set i 0} {$i < $limit} {incr i} {
        set city_a [lindex $cities $i]
        set city_b [lindex $cities [expr {$i+1}]]
        set distance [set ::${city_a}($city_b)]
        incr total_distance $distance
    }
    return $total_distance
}

if {!$tcl_interactive} {
    set cities {}
    set input [read stdin]
    foreach line [split $input "\n"] {
        set tokens [split $line]
        set city_a [lindex $tokens 0]
        set city_b [lindex $tokens 2]
        set distance [lindex $tokens 4]
        set ${city_a}($city_b) $distance
        set ${city_b}($city_a) $distance
        ::struct::set add cities $city_a
        ::struct::set add cities $city_b
    }
    set cities [lsort [list {*}$cities]]

    set shortest_trip 1000000
    set longest_trip 0
    while {$cities != {}} {
        set distance [trip_distance $cities]
        set shortest_trip [::math::min $shortest_trip $distance]
        set longest_trip [::math::max $longest_trip $distance]
        set cities [next_permutation $cities]
    }

    puts "The solution to part 1 is $shortest_trip."
    puts "The solution to part 2 is $longest_trip."

}
