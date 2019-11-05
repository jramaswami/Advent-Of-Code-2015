# Advent of Code 2015 :: Day 10 :: Elves Look, Elves Say

package require struct::queue

proc sentence_to_queue {sentence} {
    set sentence_length [string length $sentence]
    set new_sentence_queue [::struct::queue]
    for {set i 0} {$i < $sentence_length} {incr i} {
        $new_sentence_queue put [string index $sentence $i]
    }
    return $new_sentence_queue
}

proc look_and_say {sentence_queue} {
    set new_sentence_queue [::struct::queue]
    while {[$sentence_queue size] > 0} {
        set char0 [$sentence_queue get]
        set group_count 1
        while {[$sentence_queue size] > 0 && $char0 == [$sentence_queue peek]} {
            $sentence_queue get
            incr group_count
        }
        $new_sentence_queue put $group_count
        $new_sentence_queue put $char0
    }
    return $new_sentence_queue
}

proc solve_part1 {sentence} {
    set sentence_queue [sentence_to_queue $sentence]
    for {set i 1} {$i <= 40} {incr i} {
        set sentence_queue [look_and_say $sentence_queue]
    }
    return [$sentence_queue size]
}

proc solve_part2 {sentence} {
    set sentence_queue [sentence_to_queue $sentence]
    for {set i 1} {$i <= 50} {incr i} {
        set sentence_queue [look_and_say $sentence_queue]
    }
    return [$sentence_queue size]
}
if {!$tcl_interactive} {
    set input 3113322113
    puts "The solution to part 1 is [solve_part1 $input]."
    puts "The solution to part 2 is [solve_part2 $input]."
}
