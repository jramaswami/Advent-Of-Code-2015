/*****************************************************
 *
 *  Solution to puzzle 1 in Io
 * 
 *  Answer 1 should be 232.
 *  Answer 2 should be 1783.
 *
 *****************************************************/
 
// read file
s := File with("../input.txt") openForReading readLine
// count ups
u := s occurancesOfSeq("(")
// count downs
d := s occurancesOfSeq(")")
// do the math
x := u - d
"Santa ended up on floor #{x}" interpolate println

// start on floor 0
f := 0
for (i, 0, s size,
	c := s exSlice(i, i+1)
	if (c == "(") then (f = f + 1) elseif (c == ")") then (f = f - 1)
	if (f < 0) then (
		// Be sure to add one because the puzzle specifies that the first
		// character in the string is position 1 not 0.
		"Santa went into the basement on move #{i + 1}" interpolate println
		break
	)
)
