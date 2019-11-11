# Advent of Code 2015 :: Day 18 :: Like a GIF For Your Yard

set block_size 8
set input ""
set part2_constraints 0
set stop 0

proc init_canvas {} {
    global block_size
    for {set row 0} {$row < 100} {incr row} {
        for {set col 0} {$col < 100} {incr col} {
            set y1 [expr {$block_size * $row}]
            set x1 [expr {$block_size * $col}]
            set y2 [expr {$y1 + $block_size}]
            set x2 [expr {$x1 + $block_size}]

            if {[set ::matrix($row,$col)] == 1} {
                set fillColor red
            } else {
                set fillColor black
            }
            set cell_id [.c create rectangle $x1 $y1 $x2 $y2 -fill $fillColor]
            set ::cells($row,$col) $cell_id
        }
    }
}

proc inbounds {row col} {
    if {$row < 0} {
        return 0
    }
    if {$row >= 100} {
        return 0
    }
    if {$col < 0} {
        return 0
    }
    if {$col >= 100} {
        return 0
    }
    return 1
}

proc moore_neighborhood {row col} {
    set neighborhood {}
    set offsets {{-1 0} {-1 1} {0 1} {1 1} {1 0} {1 -1} {0 -1} {-1 -1}}
    foreach offset $offsets {
        set off_row [expr {$row + [lindex $offset 0]}]
        set off_col [expr {$col + [lindex $offset 1]}]
        if {[inbounds $off_row $off_col] == 1} {
            lappend neighborhood [list $off_row $off_col]
        }
    }
    return $neighborhood
}

proc get_status {posn} {
    set row [lindex $posn 0]
    set col [lindex $posn 1]
    return [set ::matrix($row,$col)]
}

proc next_status {row col} {
    set my_status [get_status [list $row $col]]
    set neighbors [moore_neighborhood $row $col]
    set living_neighbors 0
    foreach neighbor $neighbors {
        set neighbor_status [get_status $neighbor]
        if {$neighbor_status == 1} {
            incr living_neighbors
        }
    }
    if {$my_status == 0 && $living_neighbors == 3} {
        return 1
    } elseif {$my_status == 1 && ($living_neighbors == 2 || $living_neighbors == 3)} {
        return 1
    }
    return 0
}

proc tick {} {
    global part2_constraints

    for {set row 0} {$row < 100} {incr row} {
        for {set col 0} {$col < 100} {incr col} {
            set future($row,$col) [next_status $row $col]
        }
    }

    if {$part2_constraints} {
        set future(0,0) 1
        set future(0,99) 1
        set future(99,0) 1
        set future(99,99) 1
    }

    for {set row 0} {$row < 100} {incr row} {
        for {set col 0} {$col < 100} {incr col} {
            set ::matrix($row,$col) [set future($row,$col)]
            if {[set ::matrix($row,$col)] == 1} {
                set fillColor red
            } else {
                set fillColor black
            }
            set cell_id [set ::cells($row,$col)]
            .c itemconfigure $cell_id -fill $fillColor
        }
    }
}

proc parse_input {} {
    global input
    global part2_constraints
    set lines [split $input "\n"]
    set row_limit [llength $lines]
    for {set row 0} {$row < $row_limit} {incr row} {
        set line [lindex $lines $row]
        set col_limit [string length $line]
        for {set col 0} {$col < $col_limit} {incr col} {
            set status [string index $line $col]
            if {$status == "#"} {
                set ::matrix($row,$col) 1
            } else {
                set ::matrix($row,$col) 0
            }
        }
    }

    if {$part2_constraints} {
        set ::matrix(0,0) 1
        set ::matrix(0,99) 1
        set ::matrix(99,0) 1
        set ::matrix(99,99) 1
    }
}

proc init_game {} {
    parse_input
    init_canvas
    .status.living configure -text "Living Cells: [count_living_cells]"
}

proc count_living_cells {} {
    set living_cells 0
    for {set row 0} {$row < 100} {incr row} {
        for {set col 0} {$col < 100} {incr col} {
            set status [set ::matrix($row,$col)]
            if {$status == 1} {
                incr living_cells
            }
        }
    }
    return $living_cells
}

proc go {} {
    global stop
    set stop 0
    set ticks 0
    init_game
    while {1} {
        if {$ticks == 100 || $stop == 1} {
            break
        }
        tick
        incr ticks
        .status.ticks configure -text "Ticks: $ticks"
        .status.living configure -text "Living Cells: [count_living_cells]"
        update
        after 50
    }
}

if {!$tcl_interactive} {
    global input
    set input [string trimright [read stdin]]

    set canvas_dim [expr {$block_size * 100}]
    canvas .c -height $canvas_dim -width $canvas_dim -background white
    pack .c -side top

    
    frame .status
    label .status.ticks -text "Ticks: 0"
    label .status.living -text "Living Cells: 0"
    pack .status.ticks -side left
    pack .status.living -side left
    pack .status -side bottom
    
    frame .control
    # button .control.init -text Init -command init_game
    button .control.go -text Go -command go
    button .control.stop -text Stop -command {set ::stop 1}
    # pack .control.init -side left
    pack .control.go -side left
    pack .control.stop -side left
    frame .control.part2
    label .control.part2.lbl -text "Part 2: "
    checkbutton .control.part2.cbtn -variable part2_constraints
    pack .control.part2.lbl -side left
    pack .control.part2.cbtn -side right
    pack .control.part2 -side right
    pack .control -side bottom

    init_game
}
