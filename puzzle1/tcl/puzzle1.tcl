# Advent of Code 2015 :: Day 1 :: Not Quite Lisp

set file [open "../input.txt"]
set input [read $file]

set floor 0
set index 1
set entered_basement 0 

foreach char [split $input {}] {
    if {$char == "("} {
        incr floor
    } elseif {$char == ")"} {
        incr floor -1
    }
    if {$entered_basement == 0 && $floor < 0} {
        set entered_basement $index
    }
    incr index
}

puts "Answer to part 1 is $floor."
puts "Answer to part 2 is $entered_basement."
