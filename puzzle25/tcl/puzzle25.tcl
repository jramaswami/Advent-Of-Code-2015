# Advent of Code 2015 :: Day 25 :: Let It Snow

proc index_of {row col} {
    set init_number [expr {(($col + 1) * $col) / 2}]
    set offset [expr {((($row + $col - 1) * ($row + $col - 2)) / 2) - (($col * ($col - 1)) / 2)}]
    return [expr {$init_number + $offset}]
}

proc compute_code {index} {
    set prev 20151125
    set curr [expr {($prev * 252533) % 33554393}]
    if {$index == 1} {
        return $prev
    } elseif {$index == 2} {
        return $curr
    }
    set i 2
    while {$i < $index} {
        set t $curr
        set curr [expr {($curr * 252533) % 33554393}]
        set prev $t
        incr i 1
    }
    return $curr
}

if {!$tcl_interactive} {
    # Input
    set row 2947
    set col 3029
    puts "The solution to day 25 is [compute_code [index_of $row $col]]."
}
