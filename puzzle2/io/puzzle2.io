/*********************************************************
 *
 *	Day 2 Puzzle
 *
 * Answer 1 should be: 1606483
 * Answer 2 should be: 3842356
 *
 *********************************************************/

// read input file
d := File with("../input.txt") openForReading readLines 

/****************************** PART 1 ******************************/

/**
 * Function to calcuate the surface area of each side
 * and the extra required.
 *
 * Returns a list: (2*l*h, 2*w*l, 2*w*h, extra)
 */
calc_sas := method(
	x := at(0) * at(1)
	y := at(1) * at(2)
	z := at(2) * at(0)
	w := list(x, y, z) min
	v := list(2 * x, 2 * y, 2 * z, w)
	return v
)
// split data; 
// convert it into a list of numbers; 
e := d map(split("x") map(asNumber)) 
// calculate the surface area of the sides and the extra;
// sum to get the total surface area of each box;
// and then sum the surface areas to get the grand total;
f := e map(calc_sas) map(sum) sum
"#{f} square foot of wrapping paper should be ordered." interpolate println

/****************************** PART 2 ******************************/

/**
 * Function to calculate the ribbon required for each box by:
 *		sorting list
 *		selecting the first two elements
 *		multiplying them by 2
 *		summing them
 *		adding the product of the three dimensions
 */
m := method( sort exSlice(0, 2) map(*2) sum + reduce( * ) )
// calculate the amount of required ribbon for each box
// then sum the amounts to get the grand total
g := e map(m) sum
"#{g} feet of ribbon is should be ordered." interpolate println
