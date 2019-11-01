# Advent of Code 2015 :: Day 6 :: Probably a Fire Hazard

package require math

global light_array
global bright_array

proc init_array {} {
    global light_array
    global bright_array
    for {set row 0} {$row < 1000} {incr row} {
        for {set col 0} {$col < 1000} {incr col} {
            set light_array($row,$col) 0
            set bright_array($row,$col) 0
        }
    }
}

proc turn {on_off start_coord through end_coord} {
    global light_array
    global bright_array

    set start_list [split $start_coord ,]
    set end_list [split $end_coord ,]
    set start_row [lindex $start_list 0]
    set start_col [lindex $start_list 1]
    set end_row [lindex $end_list 0]
    set end_col [lindex $end_list 1]

    for {set row $start_row} {$row <= $end_row} {incr row} {
        for {set col $start_col} {$col <= $end_col} {incr col} {
            set brightness [set bright_array($row,$col)]
            if {$on_off == off} {
                set light_array($row,$col) 0
                set bright_array($row,$col) [::math::max 0 [expr {$brightness - 1}]]
            } else {
                set light_array($row,$col) 1
                set bright_array($row,$col) [expr {$brightness + 1}]
            }
        }
    }
}

proc toggle {start_coord through end_coord} {
    global light_array
    global bright_array

    set start_list [split $start_coord ,]
    set end_list [split $end_coord ,]
    set start_row [lindex $start_list 0]
    set start_col [lindex $start_list 1]
    set end_row [lindex $end_list 0]
    set end_col [lindex $end_list 1]

    for {set row $start_row} {$row <= $end_row} {incr row} {
        for {set col $start_col} {$col <= $end_col} {incr col} {
            set light [set light_array($row,$col)]
            if {$light == 1} {
                set light_array($row,$col) 0
            } else {
                set light_array($row,$col) 1
            }
            set brightness [set bright_array($row,$col)]
            set bright_array($row,$col) [expr {$brightness + 2}]
        }
    }
}

proc count_lit {} {
    global light_array
    set lit 0
    for {set row 0} {$row < 1000} {incr row} {
        for {set col 0} {$col < 1000} {incr col} {
            set light [set light_array($row,$col)]
            if {$light == 1} {
                    incr lit
            }
        }
    }
    return $lit
}

proc sum_brightness {} {
    global bright_array
    set total_brightness 0
    for {set row 0} {$row < 1000} {incr row} {
        for {set col 0} {$col < 1000} {incr col} {
            incr total_brightness [set bright_array($row,$col)]
        }
    }
    return $total_brightness
}

if {!$tcl_interactive} {
    global light_array
    init_array
    source "../input.txt"
    puts "The solution to part 1 is [count_lit]."
    puts "The solution to part 2 is [sum_brightness]."
}
