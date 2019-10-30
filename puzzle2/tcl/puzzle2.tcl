# Advent of Code 2015 :: Day 2 :: I Was Told There Would Be No Math

package require math

proc required_wrapping_paper {dimensions} {
    set side1 [expr {[lindex $dimensions 0] * [lindex $dimensions 1]}]
    set side2 [expr {[lindex $dimensions 0] * [lindex $dimensions 2]}]
    set side3 [expr {[lindex $dimensions 1] * [lindex $dimensions 2]}]
    set total_area [expr {2 * ($side1 + $side2 + $side3)}]
    set smallest_side [::math::min $side1 $side2 $side3]
    return [expr {$total_area + $smallest_side}]
}

proc required_ribbon {dimensions} {
    set largest_side [::math::max {*}$dimensions]
    set wrapping_ribbon [expr {(2 * [::math::sum {*}$dimensions]) - (2 * $largest_side)}]
    set bow_ribbon [::math::product {*}$dimensions]
    return [expr {$wrapping_ribbon + $bow_ribbon}]
}

if {!$tcl_interactive} {
    set file_name [open "../input.txt"]
    set input [string trimright [read $file_name]]

    set total_wrapping_paper 0
    set total_ribbon 0
    foreach box [split $input "\n"] {
        set dimensions [split $box "x"]
        set total_wrapping_paper [expr {$total_wrapping_paper + [required_wrapping_paper $dimensions]}]
        set total_ribbon [expr {$total_ribbon + [required_ribbon $dimensions]}]
    }

    puts "The answer to part 1 is $total_wrapping_paper."
    puts "The answer to part 2 is $total_ribbon."
}
