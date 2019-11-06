# Advent of Code 2015 :: Day 12 :: JSAbacusFramework.io

# The json package in tcllib does not include type information.
# I found a json package on the Tcl'ers Wiki.  It does include
# the type information neccesary to sovle part 2.

source json.tcl

proc sum_json {json level {filter_red 0}} {
    set total 0
    set type [lindex $json 0]
    set value [lindex $json 1]
    if {$type == "array"} {
        foreach json0 $value {
            incr total [sum_json $json0 [expr {$level + 1}] $filter_red]
        }
    } elseif {$type == "object"} {
        dict for {k v} $value {
            incr total [sum_json $v [expr {$level + 1}] $filter_red]
            if {$filter_red && [string compare [lindex $v 1] "red"] == 0} {
                return 0
            }
        }
    } else {
        if {$type == "number"} {
            incr total $value
        }
    }
    return $total
}

if {!$tcl_interactive} {
    set input [read stdin]
    set json [::json::decode $input]
    puts "The solution to part 1 is [sum_json $json 0]."
    puts "The solution to part 2 is [sum_json $json 0 1]."
}
