# Advent of Code 2015 :: Day 11 :: Corporate Policy

proc char_to_code {c} {
    return [expr {[scan $c %c] - [scan "a" %c]}]
}

proc code_to_char {c} {
    return [string index "abcdefghijklmnopqrstuvwxyz" $c]
}

proc password_to_passcode {password} {
    return [lmap c [split $password ""] {char_to_code $c}]
}

proc passcode_to_password {passcode} {
    return [join [lmap c $passcode {code_to_char $c}] ""]
}

proc incr_passcode {passcode_ref} {
    upvar $passcode_ref passcode
    set passcode_length [llength $passcode]
    for {set i [expr {$passcode_length - 1}]} {$i >= 0} {incr i -1} {
        set code [lindex $passcode $i]
        incr code
        if {$code < 26} {
            lset passcode $i $code
            break
        }
        lset passcode $i 0
    }
}

# Passwords must include one increasing straight of at least three letters
proc rule1_valid {passcode} {
    set passcode_length [llength $passcode]
    set search_limit [expr {$passcode_length - 2}]
    for {set i 0} {$i < $search_limit} {incr i} {
        set c0 [lindex $passcode $i]
        set c1 [lindex $passcode [expr {$i+1}]]
        set c2 [lindex $passcode [expr {$i+2}]]
        if { $c1 == [expr {$c0 + 1}] && $c2 == [expr {$c1 + 1}] } {
            return 1
        }
    }
    return 0
}

# Passwords may not contain the letters i, o, or l
proc rule2_valid {passcode} {
    set passcode_length [llength $passcode]
    for {set i 0} {$i < $passcode_length} {incr i} {
        set c [lindex $passcode $i]
        if {$c == 8 || $c == 11 || $c == 14} {
            return 0
        }
    }
    return 1
}

# Passwords must contain at least two different, non-overlapping pairs of
# letters
proc rule3_valid {passcode} {
    set double -1
    set passcode_length [llength $passcode]
    set search_limit [expr {$passcode_length - 1}]
    for {set i 0} {$i < $search_limit} {incr i} {
        set c0 [lindex $passcode $i]
        set c1 [lindex $passcode [expr {$i + 1}]]
        if {$c0 == $c1} {
            if {$double >= 0 && $c0 != $double} {
                return 1
            } elseif {$double == -1} {
                set double $c0
            }
            incr i
        }
    }
    return 0
}

proc valid_passcode {passcode} {
    return [expr {[rule1_valid $passcode] && [rule2_valid $passcode] && [rule3_valid $passcode]}]
}

proc incr_password {password} {
    set passcode [password_to_passcode $password]
    incr_passcode passcode
    return [passcode_to_password $passcode]
}

proc next_passcode {passcode} {
    incr_passcode passcode
    set is_valid [valid_passcode $passcode]
    while {!$is_valid} {
        incr_passcode passcode
        set is_valid [valid_passcode $passcode]
    }
    return $passcode
}

proc next_password {password} {
    set passcode [password_to_passcode $password]
    set passcode0 [next_passcode $passcode]
    set password0 [passcode_to_password $passcode0]
    return $password0
}

if {!$tcl_interactive} {
    set input hepxcrrq
    set password1 [next_password $input]
    puts "The answer to part 1 is $password1."
    set password2 [next_password $password1]
    puts "The answer to part 2 is $password2."
}
