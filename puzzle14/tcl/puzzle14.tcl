# Advent of Code 2015 :: Day 14 :: Reindeer Olympics

proc tick {reindeers} {
    foreach reindeer $reindeers {
        if {[set ::${reindeer}(status)] > 0} {
            set posn [set ::${reindeer}(position)]
            set speed [set ::${reindeer}(speed)]
            set ::${reindeer}(position) [expr {$posn + $speed}]
            incr ::${reindeer}(status) -1
            if {[set ::${reindeer}(status)] == 0} {
                set ::${reindeer}(status) [set ::${reindeer}(rest)]
            }
        } else {
            incr ::${reindeer}(status) 1
            if {[set ::${reindeer}(status)] == 0} {
                set ::${reindeer}(status) [set ::${reindeer}(flight)]
            }
        }
    }

    set leaders [get_leaders $reindeers]
    foreach leader $leaders {
        incr ::${leader}(points)
    }
}

proc parse_input {input} {
    set reindeers {}
    set lines [split $input "\n"]
    foreach line $lines {
        set tokens [split $line]
        set reindeer [lindex $tokens 0]
        set reindeer_speed [lindex $tokens 3]
        set reindeer_flight_time [lindex $tokens 6]
        set reindeer_rest_time [lindex $tokens 13]

        set ::${reindeer}(speed) $reindeer_speed
        set ::${reindeer}(flight) $reindeer_flight_time
        set ::${reindeer}(rest) [expr {-1 *$reindeer_rest_time}]
        lappend reindeers $reindeer
    }
    return $reindeers
}

proc init_race {reindeers} {
    foreach reindeer $reindeers {
        set ::${reindeer}(status) [set ::${reindeer}(flight)]
        set ::${reindeer}(position) 0
        set ::${reindeer}(points) 0
    }
}

proc get_leaders {reindeers} {
    set winning_distance 0
    set leaders {}
    foreach reindeer $reindeers {
        set position [set ::${reindeer}(position)]
        if {$position > $winning_distance} {
            set winning_distance $position
            set leaders [list $reindeer]
        } elseif {$position == $winning_distance} {
            lappend leaders $reindeer
        }
    }
    return $leaders
}


if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    set reindeers [parse_input $input]

    init_race $reindeers
    for {set t 1} {$t <= 2503} {incr t} {
        tick $reindeers
    }
    set winner [lindex [get_leaders $reindeers]]
    set winner_distance [set ${winner}(position)]
    puts "The winner of the part 1 race is $winner at $winner_distance."

    set winner ""
    set winner_points 0
    foreach reindeer $reindeers {
        set pts [set ${reindeer}(points)]
        if {$pts > $winner_points} {
            set winner $reindeer
            set winner_points $pts
        }
    }
    puts "The winner of the part 2 race is $winner with $winner_points points."
}
