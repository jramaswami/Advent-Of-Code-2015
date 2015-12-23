"""RPG Simulation components of Day 22 Puzzle."""

VERBOSE = False
HARDMODE = False

import magic

def log(msg):
    """Prints message if VERBOSE == True"""
    if VERBOSE:
        print msg

class SpellCastingException(Exception):
    """Exception for trying to cast a spell you can't"""
    def __init__(self, value):
        self.value = value

    def __stri__(self):
        return repr(self.value)

class Character(object):
    """Represents a character in the game."""

    def __init__(self, name, hit_points, damage=0, armor=0, mana=0):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.mana = mana

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
        return magic.get_spell_cost(spell_name) <= self.mana

def spell_can_be_cast(spell, player, effects):
    """Function to say if spell can be cast."""
    spells_in_effect = effects.keys()
    if spell in spells_in_effect and effects[spell] > 0:
        return False
    elif not player.can_cast_spell(spell):
        return False
    else:
        return True

def execute_effects(player, boss, effects):
    """Execute the effects"""
    for effect, timer in effects.items():
        log('Execute effect %s (%d)' % (effect, (timer - 1)))
        effect_function = magic.EFFECTS[effect]
        effect_function(player, boss)
        effects[effect] = timer - 1
        if timer - 1 == 0:
            log('Effect %s expiring' % effect)
            if effect == 'Shield':
                log('Turning off shield')
                magic.shield_expire(player, boss)
            del effects[effect]

def simulate_combat_round(player, boss, effects, spell):
    """Simulate combat"""
    # hardmode
    if HARDMODE:
        player.hit_points = player.hit_points - 1

    # player turn
    log("\n-- Player Turn --")
    log(str(player))
    log(str(boss))

    execute_effects(player, boss, effects)
    if boss.is_dead():
        log('Boss is dead!')
        return

    # Cast spell
    log('Player casting spell %s' % spell)
    spell_function = magic.SPELLBOOK[spell]['func']
    spell_cost = magic.SPELLBOOK[spell]['cost']
    log('Player spell costs %d mana' % spell_cost)
    if spell_can_be_cast(spell, player, effects):
        player.mana = player.mana - spell_cost
        spell_function(player, boss, effects)
    else:
        raise SpellCastingException('Unable to cast spell %s')

    # boss turn effects first
    log("\n-- Boss Turn --")
    log(str(player))
    log(str(boss))

    execute_effects(player, boss, effects)

    if boss.is_dead():
        log('Boss is dead!')
        log(str(player))
        log(str(boss))
        return 1

    attack_damage = boss.attack(player)
    log('Boss attacked player for %d damage.' % attack_damage)
    log('Player now has %d hp.' % player.hit_points)

    if player.is_dead():
        log('Player is dead!')
        log(str(player))
        log(str(boss))
        return -1

    log(str(player))
    log(str(boss))

def simulate_combat(player, boss, spells, effects):
    """Simulate combat"""
    log('Beginning combat ...')
    log(str(player))
    log(str(boss))

    while player.hit_points > 0 and boss.hit_points > 0:
        try:
            player_spell = spells.next()
        except StopIteration:
            return 0
        simulate_combat_round(player, boss, effects, player_spell)

    if boss.is_dead():
        return 1
    elif player.is_dead():
        return -1
