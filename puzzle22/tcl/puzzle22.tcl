# Advent of Code 2015 :: Day 22 :: Wizard Simulator 20XX

# State of play
# {<Status> <Mana Spent> <Boss Hit Points> <Boss Damage> <Hero Hitpoints> <Hero Mana> <Hero Armor> {<Effect, Effect Timer> <Effect, Effect Timer> ...}}

proc play_state {boss_hp boss_dmg hero_hp hero_mana} {
    return [list ok 0 $boss_hp $boss_dmg $hero_hp $hero_mana 0 {}]
}

proc init_state {} {
    return [list ok 0 71 10 50 500 0 {}]
}

proc spell_is_active {spell effects} {
    foreach spell $effects {
        set effect_name [lindex $spell 0]
        if {$effect_name == $spell} {
            return 1
        }
    }
    return 0
}

# Set state variables in enclosing scope.
proc set_state_vars {state} {
    upvar battle_status local_battle_status
    upvar mana_spent local_mana_spent
    upvar boss_hp local_boss_hp
    upvar boss_dmg local_boss_dmg
    upvar hero_hp local_hero_hp
    upvar hero_mana local_hero_mana
    upvar hero_armor local_hero_armor
    upvar effects local_effects

    set local_battle_status [lindex $state 0]
    set local_mana_spent [lindex $state 1]
    set local_boss_hp [lindex $state 2]
    set local_boss_dmg [lindex $state 3]
    set local_hero_hp [lindex $state 4]
    set local_hero_mana [lindex $state 5]
    set local_hero_armor [lindex $state 6]
    set local_effects [lindex $state end]
}

proc get_battle_status {state} { return [lindex $state 0] }

proc get_mana_spent {state} { return [lindex $state 1] }

proc get_boss_hp {state} { return [lindex $state 2] }

proc get_boss_dmg {state} { return [lindex $state 3] }

proc get_hero_hp {state} { return [lindex $state 4] }

proc get_hero_mana {state} { return [lindex $state 5] }

proc get_hero_armor {state} { return [lindex $state 6] }

proc get_effects {state} { return [lindex $state end] }

proc apply_effects {state} {
    set_state_vars $state

    # Reset hero armor to 0
    set hero_armor 0

    set effects0 {}
    foreach effect $effects {
        set effect_name [lindex $effect 0]
        set effect_timer [lindex $effect 1]

        if {$effect_name == "poison"} {
            incr boss_hp -3
        } elseif {$effect_name == "recharge"} {
            incr hero_mana 101
        } elseif {$effect_name == "shield"} {
            incr hero_armor 7
        }

        incr effect_timer -1
        if {$effect_timer > 0} {
            lappend effects0 [list $effect_name $effect_timer]
        }
    }
    return [list $battle_status $mana_spent $boss_hp $boss_dmg $hero_hp $hero_mana $hero_armor $effects0]
}

proc set_battle_status {state_var value} {
    upvar $state_var local_state
    lset local_state 0 $value
}

proc incr_mana_spent {state_var value} {
    upvar $state_var local_state
    lset local_state 1 [expr {[get_mana_spent $local_state] + $value}]
}

proc incr_boss_hp {state_var value} {
    upvar $state_var local_state
    lset local_state 2 [expr {[get_boss_hp $local_state] + $value}]
}

proc incr_hero_hp {state_var value} {
    upvar $state_var local_state
    lset local_state 4 [expr {[get_hero_hp $local_state] + $value}]
}

proc incr_hero_mana {state_var value} {
    upvar $state_var local_state
    lset local_state 5 [expr {[get_hero_mana $local_state] + $value}]
}

proc append_effect {state_var effect timer} {
    upvar $state_var local_state
    set effects [get_effects $local_state]
    lappend effects [list $effect $timer]
    lset local_state end $effects
}

proc magic_missile {state} {
    if {[get_hero_mana $state] < 53} {
        set_battle_status state loss
        return $state
    }
    incr_hero_mana state -53
    incr_mana_spent state  53

    set state [apply_effects $state]
    if {[get_boss_hp $state] <= 0} {
        set_battle_status state win
        return $state
    }

    incr_boss_hp state -4

    if {[get_boss_hp $state] <= 0} {
        set_battle_status state win
        return $state
    }
    
    set_battle_status state ok
    return $state
}

proc drain {state} {
    if {[get_hero_mana $state] < 73} {
        set_battle_status state loss
        return $state
    }
    incr_hero_mana state -73
    incr_mana_spent state 73

    set state [apply_effects $state]

    if {[get_boss_hp $state] <= 0} {
        set_battle_status state win
        return $state
    }

    incr_boss_hp state -2
    incr_hero_hp state 2
    if {[get_boss_hp $state] <= 0} {
        set_battle_status state win
        return $state
    }

    set_battle_status state ok
    return $state
}

proc shield {state} {
    if {[get_hero_mana $state] < 113} {
        set_battle_status state loss
        return $state
    }
    incr_hero_mana state -113
    incr_mana_spent state 113

    set state [apply_effects $state]

    if {[get_boss_hp $state] <= 0} {
        set_battle_status state win
        return $state
    }

    if {[spell_is_active shield [get_effects $state]]} {
        set_battle_status state loss
        return $state
    }

    append_effect state shield 6
    set_battle_status state ok
    return $state
}

proc poison {state} {
    if {[get_hero_mana $state] < 173} {
        set_battle_status state loss
        return $state
    }
    incr_hero_mana state -173
    incr_mana_spent state 173

    set state [apply_effects $state]

    if {[get_boss_hp $state] <= 0} {
        set_battle_status state win
        return $state
    }
     
    if {[spell_is_active poison [get_effects $state]]} {
        set_battle_status state loss
        return $state
    }

    append_effect state poison 6
    set_battle_status state ok
    return $state
}

proc recharge {state} {
    if {[get_hero_mana $state] < 229} {
        set_battle_status state loss
        return $state
    }
    incr_hero_mana state -229
    incr_mana_spent state 229

    set state [apply_effects $state]

    if {[get_boss_hp $state] <= 0} {
        set_battle_status state win
        return $state
    }
     
    if {[spell_is_active recharge [get_effects $state]]} {
        set_battle_status state loss
        return $state
    }

    append_effect state recharge 5
    set_battle_status state ok
    return $state
}

proc boss_attack {state} {
    set state [apply_effects $state]

    if {[get_boss_hp $state] <= 0} {
        set_battle_status state win
        return $state
    }

    set boss_dmg0 [::tcl::mathfunc::max 1 [expr {[get_boss_dmg $state] - [get_hero_armor $state]}]]
    incr_hero_hp state -$boss_dmg0

    if {[get_hero_hp $state] <= 0} {
        set_battle_status state loss
        return $state
    }

    set_battle_status state ok
    return $state
}

proc solve_part1 {} {
    set spells {{magic_missile 53} {drain 73} {shield 113} {poison 173} {recharge 229}}
    set min_mana 1000000
    set queue [list [init_state]]
    set new_queue {}

    set ticks 0
    while {$ticks < 1000} {
        incr ticks
        puts "****** TICKS $ticks :: [llength $queue] :: $min_mana ******"
        foreach state $queue {
            
            if {[get_mana_spent $state] > $min_mana} { continue }

            foreach spell_data $spells {
                set spell [lindex $spell_data 0]
                set mana [lindex $spell_data 1]

                # Hero Turn
                set state0 [$spell $state]
                # puts "Hero casting $spell_data :: $state --> $state0"
                set status [get_battle_status $state0]
                if {$status == "win"} {
                    set min_mana [::tcl::mathfunc::min $min_mana [get_mana_spent $state0]]
                    puts "setting min_mana $min_mana"
                    continue
                } elseif {$status == "loss"} {
                    continue
                }

                # Boss Turn
                set state1 [boss_attack $state0]
                # puts "Boss attacks : $state0 --> $state1"
                set status [get_battle_status $state1]
                if {$status == "win"} {
                    set min_mana [::tcl::mathfunc::min $min_mana [get_mana_spent $state1]]
                    puts "setting min_mana $min_mana"
                    continue
                } elseif {$state1 == "loss"} {
                    continue
                } elseif {[get_mana_spent $state1] < $min_mana} {
                    lappend new_queue $state1
                }
            }
        }

        if {[llength $new_queue] == 0} {
            return $min_mana
        }

        set queue {}
        set queue $new_queue
        set new_queue {}
    }
}

proc play {boss_hp boss_dmg hero_hp hero_mana spell_list} {
    set state [play_state $boss_hp $boss_dmg $hero_hp $hero_mana]
    foreach spell $spell_list {
        set state0 [$spell $state]
        puts "Hero cast $spell: $state --> $state0"
        set state1 [boss_attack $state0]
        puts "Boss attack: $state0 --> $state1"
        set state $state1
    }
}

if {!$tcl_interactive} {
    puts [solve_part1]
}
