# Advent of Code 2015 :: Day 22 :: Wizard Simulator 20XX

package require struct::stack

# mana_spent hero_mana hero_hp hero_armor boss_hp <effects {{spell timer} ...}> <history {spell ...}>?

set VERBOSE 0

proc log {msg} {
    if {$::VERBOSE} {
        puts $msg
    }
}

proc apply_effects {state} {
    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    set hero_hp [lindex $state 2]
    set hero_armor 0
    set boss_hp [lindex $state 4]
    set effects [lindex $state 5]
    set spells [lindex $state 6]

    set effects0 {}
    foreach effect $effects {
        set effect_name [lindex $effect 0]
        set effect_timer [lindex $effect 1]

        if {$effect_name == "shield"} {
            log "Hero armor +7 ..."
            incr hero_armor 7
        } elseif {$effect_name == "poison"} {
            log "Boss hp -3 ..."
            incr boss_hp -3
        } elseif {$effect_name == "recharge"} {
            log "Hero mana +101 ..."
            incr hero_mana 101
        }
        incr effect_timer -1
        if {$effect_timer > 0} {
            lappend effects0 [list $effect_name $effect_timer]
        }
    }
    return [list $mana_spent $hero_mana $hero_hp $hero_armor $boss_hp $effects0 $spells]
}


proc boss_attack {boss_dmg state} {

    # Apply effects
    set state [apply_effects $state]

    # Boss dead?
    if {[lindex $state 4] <= 0} {
        return $state
    }

    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    set hero_hp [lindex $state 2]
    set hero_armor [lindex $state 3] 
    set boss_hp [lindex $state 4]
    set effects [lindex $state 5]
    set spells [lindex $state 6]

    # Effective damage
    set boss_dmg0 [::tcl::mathfunc::max 1 [expr {$boss_dmg - $hero_armor}]]
    log "Hero hp -$boss_dmg0"
    incr hero_hp -$boss_dmg0

    # Return new state
    return [list $mana_spent $hero_mana $hero_hp $hero_armor $boss_hp $effects $spells]
}

proc magic_missile {state} {
    # Spend mana on spell
    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    incr mana_spent 53
    incr hero_mana -53
    set state [list $mana_spent $hero_mana {*}[lrange $state 2 end]]
    
    # Apply effects
    set state [apply_effects $state]

    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    set hero_hp [lindex $state 2]
    set hero_armor [lindex $state 3] 
    set boss_hp [lindex $state 4]
    set effects [lindex $state 5]
    set spells [lindex $state 6]

    # Damage to boss
    log "Boss hp -4 ..."
    incr boss_hp -4

    # Return new state
    return [list $mana_spent $hero_mana $hero_hp $hero_armor $boss_hp $effects [list magic_missile {*}$spells]]
}

proc drain {state} {
    # Spend mana on spell
    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    incr mana_spent 73
    incr hero_mana -73
    set state [list $mana_spent $hero_mana {*}[lrange $state 2 end]]
    
    # Apply effects
    set state [apply_effects $state]

    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    set hero_hp [lindex $state 2]
    set hero_armor [lindex $state 3] 
    set boss_hp [lindex $state 4]
    set effects [lindex $state 5]
    set spells [lindex $state 6]

    # Damage to boss, heal hero
    log "Boss hp -2, hero hp +2"
    incr boss_hp -2
    incr hero_hp 2

    # Return new state
    return [list $mana_spent $hero_mana $hero_hp $hero_armor $boss_hp $effects [list drain {*}$spells]]
}

proc shield {state} {
    # Spend mana on spell
    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    incr mana_spent 113
    incr hero_mana -113
    set state [list $mana_spent $hero_mana {*}[lrange $state 2 end]]
    
    # Apply effects
    set state [apply_effects $state]

    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    set hero_hp [lindex $state 2]
    set hero_armor [lindex $state 3] 
    set boss_hp [lindex $state 4]
    set effects [lindex $state 5]
    set spells [lindex $state 6]

    # Return new state
    return [list $mana_spent $hero_mana $hero_hp $hero_armor $boss_hp [list {shield 6} {*}$effects] [list shield {*}$spells]]
}

proc poison {state} {
    # Spend mana on spell
    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    incr mana_spent 173
    incr hero_mana -173
    set state [list $mana_spent $hero_mana {*}[lrange $state 2 end]]
    
    # Apply effects
    set state [apply_effects $state]

    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    set hero_hp [lindex $state 2]
    set hero_armor [lindex $state 3] 
    set boss_hp [lindex $state 4]
    set effects [lindex $state 5]
    set spells [lindex $state 6]

    # Return new state
    return [list $mana_spent $hero_mana $hero_hp $hero_armor $boss_hp [list {poison 6} {*}$effects] [list poison {*}$spells]]
}

proc recharge {state} {
    # Spend mana on spell
    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    incr mana_spent 229
    incr hero_mana -229
    set state [list $mana_spent $hero_mana {*}[lrange $state 2 end]]
    
    # Apply effects
    set state [apply_effects $state]

    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    set hero_hp [lindex $state 2]
    set hero_armor [lindex $state 3] 
    set boss_hp [lindex $state 4]
    set effects [lindex $state 5]
    set spells [lindex $state 6]

    # Return new state
    return [list $mana_spent $hero_mana $hero_hp $hero_armor $boss_hp [list {recharge 5} {*}$effects] [list recharge {*}$spells]]
}

proc spell_ok {spell state min_mana} {
    set mana_spent [lindex $state 0]
    set hero_mana [lindex $state 1]
    set spell_name [lindex $spell 0]
    set spell_cost [lindex $spell 1]

    if {$spell_cost > $hero_mana} { 
        log "Not enough hero mana to cast $spell_name : $state\n"
        return 0 
    }

    incr mana_spent $spell_cost
    if {$mana_spent >= $min_mana} { 
        return 0 
    }

    set effects [lindex $state 5]
    foreach effect $effects {
        set effect_name [lindex $effect 0]
        set effect_timer [lindex $effect 1]
        if {$effect_name == $spell_name && $effect_timer > 1} { 
            log "$spell_name already in effect: $state\n"
            return 0 
        }
    }
    return 1
}

proc solve_part1 {boss_hp boss_dmg hero_hp hero_mana} {
    # State {mana_spent hero_mana hero_hp hero_armor boss_hp effects history}
    set state [list 0 $hero_mana $hero_hp 0 $boss_hp {} {}]
    set min_mana 1000000

    set tick 0
    set queue [list $state]
    set new_queue {}

    set spell_list [list {magic_missile 53} {drain 73} {shield 113} {poison 173} {recharge 229}]

    while {[llength $queue] > 0} {
        incr tick
        puts "Tick $tick : [llength $queue]"

        foreach state $queue {

            foreach spell $spell_list {

                # Can this attack be made?
                if {![spell_ok $spell $state $min_mana]} {
                    continue
                }
                
                set spell_name [lindex $spell 0]
                set spell_cost [lindex $spell 1]


                # Hero Attack
                log "Hero cast $spell_name from $state"
                set state0 [$spell_name $state]

                # Boss Dead?
                if {[lindex $state0 4] <= 0} {
                    set min_mana [::tcl::mathfunc::min $min_mana [lindex $state0 0]]
                    log "Win!!! $min_mana"
                    log "Hero cast $spell_name to $state0\n"
                    continue
                }
                # Hero dead?
                if {[lindex $state0 2] <= 0} { 
                    log "Loss..."
                    log "Hero cast $spell_name to $state0\n"
                    continue
                }
                log "Hero cast $spell_name to $state0"

                # Boss Attack
                log "Boss attack from $state0"
                set state1 [boss_attack $boss_dmg $state0]
                # Boss Dead?
                if {[lindex $state1 4] <= 0} {
                    set min_mana [::tcl::mathfunc::min $min_mana [lindex $state0 0]]
                    log "Win!!! $min_mana"
                    log "Boss attack to $state1\n"
                    continue
                }
                # Hero dead?
                if {[lindex $state1 2] <= 0} { 
                    log "Loss..."
                    log "Boss attack to $state1\n"
                    continue
                }
                log "Boss attack to $state1\n"

                # Enqueue
                lappend new_queue $state1
            }
        }

        set queue $new_queue
        set new_queue {}

    }
    return $min_mana
}

if {!$tcl_interactive} {
    puts [solve_part1 71 10 50 500]
}
