# Advent of Code 2015 :: Day 21 :: RPG Simulator 20XX

############### Store ##################
# Weapons:    Cost  Damage  Armor
set dagger      {8      4       0}
set shortsword  {10     5       0}
set warhammer   {25     6       0}
set longsword   {40     7       0}
set greataxe    {74     8       0}

# Armor:      Cost  Damage  Armor
set noarmor     {0      0       0}
set leather     {13     0       1}
set chainmail   {31     0       2}
set splintmail  {53     0       3}
set bandedmail  {75     0       4}
set platemail   {102    0       5}

# Rings:      Cost  Damage  Armor
set norings   {0      0       0}
set damage1   {25     1       0}
set damage2   {50     2       0}
set damage3   {100    3       0}
set defense1  {20     0       1}
set defense2  {40     0       2}
set defense3  {80     0       3}
########################################

# Given a list of equipment, compute the total cost, damage, and armor.
proc equipment_stats {equipment} {
    set total_cost 0
    set total_damage 0
    set total_armor 0
    foreach piece $equipment {
        set piece_cost [lindex [set ::${piece}] 0]
        set piece_damage [lindex [set ::${piece}] 1]
        set piece_armor [lindex [set ::${piece}] 2]
        incr total_cost $piece_cost
        incr total_damage $piece_damage
        incr total_armor $piece_armor
    }
    return [list $total_cost $total_damage $total_armor]
}

# Function to compare two equipment lists by price.
proc compare_equipment_price {e0 e1} {
    set e0_price [lindex $e0 0]
    set e1_price [lindex $e1 0]
    return [expr {$e0_price - $e1_price}]
}

# Return a list of possible equipment configurations, sorted by the price
# where the list is {cost armor damage item1 item2 ...}.
proc possible_equipment_lists {} {
    set weapons {dagger shortsword warhammer longsword greataxe}
    set armors {noarmor leather chainmail splintmail bandedmail platemail}
    set rings {damage1 damage2 damage3 defense1 defense2 defense3}


    # Add 0, 1, or 2 rings to equipment ...
    # No rings 
    set rings_list [list [list norings]]
    # One ring
    foreach ring $rings { 
        lappend rings_list [list $ring]
    }
    # Two rings
    for {set i 0} {$i < [llength $rings]} {incr i} {
        for {set j [expr {$i + 1}]} {$j < [llength $rings]} {incr j} {
            set ring1 [lindex $rings $i]
            set ring2 [lindex $rings $j]
            lappend rings_list [list $ring1 $ring2]
        }
    }

    # Add optional armor ...
    set rings_armors {}
    foreach armor $armors {
        foreach ring $rings_list {
            set equipment0 [list {*}$ring]
            lappend equipment0 $armor
            lappend rings_armor $equipment0
        }
    }

    # Add a weapon ...
    set equipment {}
    foreach weapon $weapons {
        foreach equipment0 $rings_armor {
            set equipment1 [list {*}$equipment0]
            lappend equipment1 $weapon
            lappend equipment $equipment1
        }
    }

    # Compute stats ...
    set priced_equipment {}
    foreach e $equipment {
        set e0 [list {*}[equipment_stats $e] {*}$e]
        lappend priced_equipment $e0
    }

    # Return list of possible configurations sorted by price.
    return [lsort -command compare_equipment_price $priced_equipment]
}

proc solve {equipment_list} {
    set boss_hits 0
    set boss_damage 8
    set boss_armor 2

    set min_win 10000000
    set max_loss 0

    foreach equipment $equipment_list {
        set hero_hits 100
        set equip_cost [lindex $equipment 0]
        set hero_damage [lindex $equipment 1]
        set hero_armor [lindex $equipment 2]

        set boss_effective_damage [::tcl::mathfunc::max 1 [expr {$boss_damage - $hero_armor}]]
        set hero_effective_damage [::tcl::mathfunc::max 1 [expr {$hero_damage - $boss_armor}]]

        set rounds_to_boss_death [::tcl::mathfunc::ceil [expr {100.00 / $hero_effective_damage}]]
        set rounds_to_hero_death [::tcl::mathfunc::ceil [expr {100.00 / $boss_effective_damage}]]
        if {$rounds_to_boss_death <= $rounds_to_hero_death} {
            set min_win [::tcl::mathfunc::min $min_win $equip_cost]
        } else {
            set max_loss [::tcl::mathfunc::max $min_win $equip_cost]
        }
    }
    return [list $min_win $max_loss]
}

if {!$tcl_interactive} {
    set soln [solve [possible_equipment_lists]]
    puts "The solution to part 1 is [lindex $soln 0]."
    puts "The solution to part 2 is [lindex $soln 1]."
}
