# Advent of Code 2015 :: Day 12 :: JSAbacusFramework.io

package require json

proc sum_json {json level} {
    set total 0
    if {[string is alpha $json]} {
        # do nothing
    }  elseif {[string is integer $json]} {
        incr total $json
    } else {
        foreach json0 $json {
            set level0 [expr {$level + 1}]
            incr total [sum_json $json0 $level0]
        }
    }
    return $total
}

if {!$tcl_interactive} {
    set input [read stdin]
    set json [::json::json2dict $input]
    puts "The answer to part 1 is [sum_json $json 0]."
}
