# Advent of Code 2015 :: Day 15 :: Science for Hungry People

package require math


# Return a list of partitions where each partition sums to target_sum
# and has a length of target_length.
proc partition {target_sum target_length} {
    set solutions {}
    partition0 $target_sum $target_length {} 0 0 solutions
    return $solutions
}

# Recursive function to generate partitions.
proc partition0 {target_sum target_length accumulator current_length current_sum solution_name} {
    upvar solutions $solution_name
    set limit [expr {$target_length - 1}]
    if {$current_length == $limit} {
        set x [expr {$target_sum - $current_sum}]
        lappend accumulator $x
        lappend solutions $accumulator
    } else {
        for {set i 1} {$i < $target_sum} {incr i} {
            set accumulator0 $accumulator
            lappend accumulator0 $i
            set current_length0 [expr {$current_length + 1}]
            set current_sum0 [expr {$current_sum + $i}]
            if {$current_sum0 < $target_sum} {
                partition0 $target_sum $target_length $accumulator0 $current_length0 $current_sum0 $solution_name
            }
        }
    }
}

proc score_partition {partition properties} {
    set total_score 1
    for {set property 0} {$property < 4} {incr property} {
        set property_sum 0
        for {set ingredient 0} {$ingredient < 4} {incr ingredient} {
            set ingredient_property_value [lindex [lindex $properties $ingredient] $property]
            set ingredient_measure [lindex $partition $ingredient]
            incr property_sum [expr {$ingredient_measure * $ingredient_property_value}]
        }
        set property_sum [::math::max 0 $property_sum]
        set total_score [expr {$total_score * $property_sum}]
    }

    set total_calories 0
    for {set ingredient 0} {$ingredient < 4} {incr ingredient} {
        set ingredient_calories [lindex [lindex $properties $ingredient] 4]
        set ingredient_measure [lindex $partition $ingredient]
        incr total_calories [expr {$ingredient_measure * $ingredient_calories}]
    }

    return [list $total_score $total_calories]
}

if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    set lines [split $input "\n"]
    set properties {}
    foreach line $lines {
        set tokens [split $line]
        set capacity [string range [lindex $tokens 2] 0 end-1]
        set durability [string range [lindex $tokens 4] 0 end-1]
        set flavor [string range [lindex $tokens 6] 0 end-1]
        set texture [string range [lindex $tokens 8] 0 end-1]
        set calories [lindex $tokens 10]
        set props [list $capacity $durability $flavor $texture $calories]
        lappend properties $props
    }
    set ingredients [llength $properties]
    set partitions [partition 100 $ingredients]
    set part1_soln 0
    set part2_soln 0
    foreach part $partitions {
        set score [score_partition $part $properties]
        set part1_soln [::math::max $part1_soln [lindex $score 0]]
        if {[lindex $score 1] == 500} {
            set part2_soln [::math::max $part2_soln [lindex $score 0]]
        }
    }
    puts "The solution to part 1 is $part1_soln."
    puts "The solution to part 2 is $part2_soln."
}
