# Advent of Code 2015 :: Day 3 :: Perfectly Spherical Houses in a Vacuum

proc move {posn dirn} {
    set row [lindex $posn 0]
    set col [lindex $posn 1]
    if {$dirn == "^"} {
        incr row -1
    } elseif {$dirn == "v"} {
        incr row
    } elseif {$dirn == "<"} {
        incr col -1
    } elseif {$dirn == ">"} {
        incr col
    }
    return [list $row $col]
}
        
proc solve_part1 {input} {
    set posn [list 0 0]
    set soln 1
    set delivered [dict create $posn 1]
    foreach dirn [split $input {}] {
        set posn [move $posn $dirn]
        if {[dict exists $delivered $posn]} {
            dict incr delivered $posn 1
        } else {
            dict set delivered $posn 1
            incr soln
        }
    }
    return $soln
}

proc solve_part2 {input} {
    set santa [list 0 0]
    set robot [list 0 0]
    set index 0
    set soln 1
    set delivered [dict create $santa 1]
    foreach dirn [split $input {}] {
        if {[expr {$index % 2}]} {
            set posn [move $robot $dirn]
            set robot $posn
        } else {
            set posn [move $santa $dirn]
            set santa $posn
        }
        if {[dict exists $delivered $posn]} {
            dict incr delivered $posn 1
        } else {
            dict set delivered $posn 1
            incr soln
        }
        incr index
    }
    return $soln
}

if {!$tcl_interactive} {
    set file_name [open "../input.txt"]
    set input [string trimright [read $file_name]]
    puts "The solution to part 1 is [solve_part1 $input]."
    puts "The solution to part 2 is [solve_part2 $input]."
}
