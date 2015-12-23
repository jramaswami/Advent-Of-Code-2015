"""RPG Simulation components of Day 22 Puzzle."""

VERBOSE = False

import magic

def log(msg):
    """Prints message if VERBOSE == True"""
    if VERBOSE:
        print msg

class Character(object):
    """Represents a character in the game."""

    def __init__(self, name, hit_points, damage=0, armor=0, mana=0):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.mana = mana
        if mana > 0:
            self.spell_book = magic.SpellBook()
        else:
            self.spell_book = None

        self.original_hit_points = hit_points
        self.original_damage = damage
        self.original_armor = armor
        self.original_mana = mana

    def __str__(self):
        return "%s: %d hp; %d dmg; %d armor; %d mana" \
               % (self.name, self.hit_points, self.damage, \
                  self.armor, self.mana)

    def reset(self):
        """Resets Character to original state."""
        self.hit_points = self.original_hit_points
        self.damage = self.original_damage
        self.armor = self.original_armor
        self.mana = self.original_mana

    def is_dead(self):
        """Returns true if character is dead, false if alive."""
        return self.hit_points <= 0

    def attack(self, target):
        """Attacks target, reducing target.hitpoints by self.damage."""
        attack_damage = max(1, (self.damage - target.armor))
        target.hit_points -= attack_damage
        return attack_damage

    def can_cast_spell(self, spell_name):
        """Can character cast requested spell?"""
        return self.spell_book.get_spell_cost(spell_name) <= self.mana

    def cast_spell(self, spell_name, target):
        """Cast the spell"""
        if self.spell_book != None \
        and self.spell_book.get_spell_cost(spell_name) <= self.mana:
            spell = self.spell_book.get_spell(spell_name)
            spell_effect = spell.cast()
            self.mana -= spell.cost
            spell_effect.activate(self, target)
            return spell_effect

def execute_effects(effects):
    """Executes all the effects."""
    # execute all active effects
    for effect in effects:
        effect.execute()
        log('Executed effects of %s' % effect.spell_name)
        log(str(effect))

        if effect.timer == 0:
            log("%s expired." % effect.spell_name)
            effect.deactivate()


    # remove expired items
    effects[:] = [e for e in effects if e.timer > 0]

def simulate_combat_round(player, boss, effects, player_spell):
    """Simulates a single round of combat."""

    # player turn
    log("\n-- Player Turn --")
    log(str(player))
    log(str(boss))
    execute_effects(effects)
    if boss.is_dead():
        log('Boss is dead!')
        return
    if player_spell != None and player.can_cast_spell(player_spell):
        log(str(effects))
        log('Player casting %s.' % player_spell)
        new_spell_effect = player.cast_spell(player_spell, boss)
        effects.append(new_spell_effect)
    else:
        log('Player unable to cast %s, not enough mana.' % player_spell)

    # boss turn effects first
    log("\n-- Boss Turn --")
    log(str(player))
    log(str(boss))
    execute_effects(effects)
    if boss.is_dead():
        log('Boss is dead!')
        log(str(boss))
        log(str(player))
        return
    attack_damage = boss.attack(player)
    log('Boss attacked player for %d damage.' % attack_damage)
    log('Player now has %d hp.' % player.hit_points)
    if player.is_dead():
        log('Player is dead!')
        log(str(boss))
        log(str(player))
        return

    log(str(boss))
    log(str(player))

def simulate_combat(player, boss, player_spell_iterator, effects=[]):
    """Simluate combat"""

    log('Beginning combat ...')
    log(str(player))
    log(str(boss))

    # player_spell_iterator.set_environ(player, effects)
    while player.hit_points > 0 and boss.hit_points > 0:
        try:
            player_spell = player_spell_iterator.next()
        except StopIteration:
            return 0
        simulate_combat_round(player, boss, effects, player_spell)
        if boss.is_dead():
            return 1
        if player.is_dead():
            return -1

def spell_can_be_cast(spell, player, effects):
    """Function to say if spell can be cast."""
    spells_in_effect = [e.spell_name for e in effects]
    if spell in spells_in_effect:
        return False
    elif not player.can_cast_spell(spell):
        return False
    else:
        return True

def simulate_combat_round_with_functions(player, boss, spell, effects):
    # player turn
    log("\n-- Player Turn --")
    log(str(player))
    log(str(boss))

    for effect in effects:
        effect(player, boss)

    if boss.is_dead():
        log('Boss is dead!')
        return

    # Cast spell
    spell(player, boss, effects)

    # boss turn effects first
    log("\n-- Boss Turn --")
    log(str(player))
    log(str(boss))
    execute_effects(effects)
    if boss.is_dead():
        log('Boss is dead!')
        log(str(boss))
        log(str(player))
        return
    attack_damage = boss.attack(player)
    log('Boss attacked player for %d damage.' % attack_damage)
    log('Player now has %d hp.' % player.hit_points)
    if player.is_dead():
        log('Player is dead!')
        log(str(boss))
        log(str(player))
        return

    log(str(boss))
    log(str(player))


def simulate_combat_with_functions(boss, player, spells, effects):
    log('Beginning combat ...')
    log(str(player))
    log(str(boss))

    while player.hit_points > 0 and boss.hit_points > 0:
        try:
            player_spell = spells.next()
        except StopIteration:
            return 0
        simulate_combat_round_with_functions(player, boss, effects, player_spell)
        if boss.is_dead():
            return 1
        if player.is_dead():
            return -1
