# Advent of Code 2015 :: Day 23 :: Opening the Turing Lock

proc hlf {r} {
    set val [expr {int($::register($r) / 2)}]
    set ::register($r) $val
    incr ::instruction_pointer
}

proc tpl {r} {
    set val [expr {$::register($r) * 3}]
    set ::register($r) $val
    incr ::instruction_pointer
}

proc inc {r} {
    incr ::register($r)
    incr ::instruction_pointer
}

proc jmp {offset} {
    set ::instruction_pointer [expr {$::instruction_pointer + $offset}]
}

proc jie {r offset} {
    # Chop off comma
    set r [string range $r 0 end-1]
    if {[expr {[set ::register($r)] % 2}] == 0} {
        set ::instruction_pointer [expr {$::instruction_pointer + $offset}]
    } else {
        incr ::instruction_pointer
    }
}

proc jio {r offset} {
    # Chop off comma
    set r [string range $r 0 end-1]
    if {[set ::register($r)] == 1} {
        set ::instruction_pointer [expr {$::instruction_pointer + $offset}]
    } else {
        incr ::instruction_pointer
    }
}

proc solve {instructions {reg_a 0}} {
    set ::instruction_pointer 0
    set ::register(a) $reg_a
    set ::register(b) 0

    while {1} {
        if {$::instruction_pointer >= [llength $instructions]} {
            break
        }

        set line [lindex $instructions $::instruction_pointer]
        eval $line

    }
}


if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    set instructions [split $input "\n"]
    solve $instructions
    puts "The solution to part 1 is [set ::register(b)]"
    solve $instructions 1
    puts "The solution to part 2 is [set ::register(b)]"
}
