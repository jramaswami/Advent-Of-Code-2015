# Advent of Code 2015 :: Day 16 :: Aunt Sue

# Parse input and place properties for each aunt in array.
# E.g. Aunt500(trees) = 4
proc parse_input {input} {
    set lines [split $input "\n"]
    foreach line $lines {
        set split_index [string first ":" $line]
        set name [join [split [string range $line 0 [expr {$split_index - 1}]]] ""]

        set properties [split [string range $line [expr {$split_index + 2}] end] ","]
        foreach property $properties {
            set tokens [split $property ":"]
            set property_name [string trim [lindex $tokens 0]]
            set property_value [string trim [lindex $tokens 1]]
            set ::${name}($property_name) $property_value
        }
    }
}

# Recursive search for solution to part 1.
proc solve_part1 {requirements index} {
    set aunt_name "Sue${index}"
    foreach requirement $requirements {
        set req_name [lindex $requirement 0]
        set req_value [lindex $requirement 1]
        if {[info exists ::${aunt_name}($req_name)]} {
            set aunt_value [set ::${aunt_name}($req_name)]
            if {$aunt_value != $req_value} {
                return [solve_part1 $requirements [expr {$index + 1}]]
            }
        }
    }
    return $aunt_name
}

# Recursive search for solution to part 2.
proc solve_part2 {requirements index} {
    set aunt_name "Sue${index}"
    foreach requirement $requirements {
        set req_name [lindex $requirement 0]
        set req_value [lindex $requirement 1]
        if {[info exists ::${aunt_name}($req_name)]} {
            set aunt_value [set ::${aunt_name}($req_name)]
            if {$req_name == "cats" || $req_name == "trees"} {
                if {$aunt_value <= $req_value} {
                    return [solve_part2 $requirements [expr {$index + 1}]]
                }
            } elseif {$req_name == "pomeranians" || $req_name == "goldfish"} {
                if {$aunt_value >= $req_value} {
                    return [solve_part2 $requirements [expr {$index + 1}]]
                }
            } else {
                if {$aunt_value != $req_value} {
                    return [solve_part2 $requirements [expr {$index + 1}]]
                }
            }
        }
    }
    return $aunt_name
}

# Main.
if {!$tcl_interactive} {
    set input [string trimright [read stdin]]
    parse_input $input
    set requirements {{children  3} {cats 7} {samoyeds 2} {pomeranians 3} \
                      {akitas 0} {vizslas 0} {goldfish 5} {trees 3} \
                      {cars 2} {perfumes 1}}
    puts "The solution to part 1 is [solve_part1 $requirements 1]."
    puts "The solution to part 2 is [solve_part2 $requirements 1]."
}
