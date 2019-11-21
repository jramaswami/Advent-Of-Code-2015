# Advent of Code 2015 :: Day 24 :: It Hangs in the Balance

package require struct::set

proc get_total_package_weight {packages} {
    set total_weight 0
    foreach pkg $packages {
        incr total_weight $pkg
    }
    return $total_weight
}

proc minimum_quantum_entanglement {group} {
    set min_qe 9999999999999999
    foreach pkg $group {
        set min_qe [::tcl::mathfunc::min $min_qe [lindex $pkg 1]]
    }
    return $min_qe
}

proc has_intersection {previous possible} {
    foreach xs previous {
        if {[::struct::set intersect $xs $possible] != {}} {
            return 1
        }
    }
    return 0
}

proc solve {packages compartment_count} {

    set total_package_weight [get_total_package_weight $packages]
    set weight_limit [expr {$total_package_weight / $compartment_count}]

    set queue [list [list 0 1 {} 0]]
    set new_queue {}

    foreach pkg $packages {
        foreach state $queue {
            # Without this package
            lappend new_queue $state

            # With this package?
            set compartment_weight [lindex $state 0]
            incr compartment_weight $pkg
            if {$compartment_weight > $weight_limit} {
                continue
            }
            set quantum_entanglement [expr {[lindex $state 1] * $pkg}]
            set compartment_packages [lindex $state 2]
            set compartment_packages [list $pkg {*}$compartment_packages]
            set state0 [list $compartment_weight $quantum_entanglement $compartment_packages]

            
            lappend new_queue $state0
        }
        set queue $new_queue
        set new_queue {}
    }

    set solns {}
    foreach item $queue {
        if {[lindex $item 0] == $weight_limit} {
            lappend solns $item
        }
    }
    set solns [lsort -real -index 1 $solns]

    set min_qe 999999999999999
    set queue [list {}]
    set new_queue {}
    foreach soln $solns {
        foreach qs $queue {
            if {[has_intersection $qs $soln]} {
                continue
            }
            set qs0 [list $soln {*}$qs]
            set m_qe [minimum_quantum_entanglement $qs0]
            if {$m_qe < $min_qe} {
                if {[llength $qs0] == $compartment_count} {
                    set min_qe [::tcl::mathfunc::min $min_qe $m_qe]
                } else {
                    lappend new_queue $qs0
                }
            }
            if {[minimum_quantum_entanglement $qs] < $min_qe} {
                lappend new_queue $qs
            }
        }
        set queue $new_queue
        set new_queue {}
    }
    return $min_qe
}

if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    set packages [split $input "\n"]
    puts "The solution to part 1 is [solve $packages 3]."
    puts "The solution to part 2 is [solve $packages 4]."
}
