# Advent of Code 2015 :: Day 17 :: No Such Thing as Too Much

# Recursive procedure to determine all ways to get target sum
# using the given containers.
proc solve {target_sum containers} {
    set accumulator {}
    set queue {}
    set new_queue {}

    foreach container $containers {
        foreach item $queue {
            lappend new_queue $item
            set current_sum [lindex $item 0]
            set container_count [lindex $item 1]
            set included_containers [lindex $item 2]
            set new_sum [expr {$current_sum + $container}]
            if {$new_sum < $target_sum} {
                lappend included_containers $container
                lappend new_queue [list $new_sum [expr {$container_count + 1}] $included_containers]
            } elseif {$new_sum == $target_sum} {
                lappend included_containers $container
                lappend accumulator [list [expr {$container_count + 1}] $included_containers]
            }
        }
        lappend new_queue [list $container 1 [list $container]]
        set queue $new_queue
        set new_queue {}
    }
    return $accumulator
}

proc solve_part2 {solutions} {
    set min_containers 1000000
    set count 0
    foreach soln $solutions {
        set container_count [lindex $soln 0]
        if {$container_count == $min_containers} {
            incr count
        } elseif {$container_count < $min_containers} {
            set min_containers $container_count
            set count 1
        }
    }
    return $count
}

if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    set containers [split $input "\n"]
    set solutions [solve 150 $containers]
    puts "The solution to part 1 is [llength $solutions]."
    puts "The solution to part 2 is [solve_part2 $solutions]."
}
