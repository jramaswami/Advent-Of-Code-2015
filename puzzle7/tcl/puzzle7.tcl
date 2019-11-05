# Advent of Code 2015 :: Day 7 :: Some Assembly Required

package require struct::queue

set alphabet [list a b c d e f g h i j k l m n o p q r s t u v w x y z]

proc clear_vars {} {
    global alphabet
    foreach letter1 $alphabet {
        if {[uplevel [join [list "info exists " $letter1] ""]]} {
            uplevel [join [list "unset " $letter1] ""]
        }
        foreach letter2 $alphabet {
            if {[uplevel [join [list "info exists " $letter1 $letter2] ""]]} {
                uplevel [join [list "unset " $letter1 $letter2] ""]
            }
        }
    }
}

proc make_varexpr {token} {
    if {[string is integer $token]} {
        return $token
    } else {
        return [join [list {$} $token] ""]
    }
}

proc oper_NOT_X {rhs} {
    set bitstring [format "%016b" $rhs]
    set bitstring [regsub 1 $bitstring 2]
    set bitstring [regsub 0 $bitstring 1]
    set bitstring [regsub 2 $bitstring 0]
    return [scan $bitstring %b]
}

proc oper_NOT {rhs} {
    return [expr {~$rhs}]
}

proc oper_AND {lhs rhs} {
    return [expr {$lhs & $rhs}]
}

proc oper_OR {lhs rhs} {
    return [expr {$lhs | $rhs}]
}

proc oper_LSHIFT {lhs rhs} {
    return [expr {$lhs << $rhs}]
}

proc oper_RSHIFT {lhs rhs} {
    return [expr {$lhs >> $rhs}]
}

proc parse_wire_spec {spec} {
    set tokens [split $spec]
    set wire_name [lindex $tokens end]
    set gate_tokens [lrange $tokens 0 end-2]
    set gate_tokens_count [llength $gate_tokens]
    if {$gate_tokens_count == 1} {
        set rhs [make_varexpr [lindex $gate_tokens 0]]
        set spec_proc [join [list "set " $wire_name " $rhs "] ""]
    } elseif {$gate_tokens_count == 2} {
        set op [lindex $gate_tokens 0]
        set rhs [make_varexpr [lindex $gate_tokens 1]]
        set spec_proc [join [list {set } $wire_name { [oper_} $op " " $rhs {]}] ""]
    } else {
        set lhs [make_varexpr [lindex $gate_tokens 0]]
        set op [lindex $gate_tokens 1]
        set rhs [make_varexpr [lindex $gate_tokens 2]]
        set spec_proc [join [list {set } $wire_name { [oper_} $op " " $lhs " " $rhs {]}] ""]
    }
}

if {!$tcl_interactive} {
    set file_name [open "../input.txt"]
    set input [string trimright [read $file_name]]
    set specs [split $input "\n"]

    set spec_queue [::struct::queue]
    foreach spec $specs {
        set wire_proc [parse_wire_spec $spec]
        $spec_queue put $wire_proc
    }
    while {[$spec_queue size] > 0} {
        set wire_proc [$spec_queue get]
        if {[catch $wire_proc err]} {
            $spec_queue put $wire_proc
        }
    }
    puts "The answer to part 1 is [set a]."

    set override $a
    clear_vars
    set spec_queue [::struct::queue]
    foreach spec $specs {
        set wire_proc [parse_wire_spec $spec]
        if {[string equal [string range $wire_proc 0 5] {set b }]} {
            set wire_proc [join [list {set b } $override] ""]
        }
        $spec_queue put $wire_proc
    }
    while {[$spec_queue size] > 0} {
        set wire_proc [$spec_queue get]
        if {[catch $wire_proc err]} {
            $spec_queue put $wire_proc
        }
    }
    puts "The answer to part 2 is [set a]."
}
