"""Classes for magic in simulation."""

import copy

class SpellBook(object):
    """A factory for spell objects."""

    def __init__(self):
        self.spells = {'Magic Missile': 53, 'Shield': 113, 'Drain': 73,
                       'Poison': 173, 'Recharge': 229}

    def get_spell_cost(self, spell_name):
        """Returns the cost of a spell."""
        return self.spells[spell_name]

    def get_spell(self, spell_name):
        """Returns spell of spell_name"""
        if spell_name not in self.spells.keys():
            return None


        if spell_name == 'Magic Missile':
            effect = SpellEffect(spell_name=spell_name, duration=1,
                                 caster_effect=CharacterEffects(),
                                 target_effect=CharacterEffects(hit_points=-4))
            spell = Spell(spell_name, 53, effect)
        elif spell_name == 'Drain':
            effect = SpellEffect(spell_name=spell_name, duration=1,
                                 caster_effect=CharacterEffects(hit_points=+2),
                                 target_effect=CharacterEffects(hit_points=-2))
            spell = Spell(spell_name, 73, effect)
        elif spell_name == 'Shield':
            effect = SpellEffect(spell_name=spell_name, duration=6,
                                 caster_effect=CharacterEffects(armor=+7),
                                 target_effect=CharacterEffects())
            spell = Spell(spell_name, 113, effect)
        elif spell_name == 'Poison':
            effect = SpellEffect(spell_name=spell_name, duration=6,
                                 caster_effect=CharacterEffects(),
                                 target_effect=CharacterEffects(hit_points=-3))
            spell = Spell(spell_name, 173, effect)
        elif spell_name == 'Recharge':
            effect = SpellEffect(spell_name=spell_name, duration=5,
                                 caster_effect=CharacterEffects(mana=+101),
                                 target_effect=CharacterEffects())
            spell = Spell(spell_name, 229, effect)
        else:
            spell = None

        return spell

class Spell(object):
    """Represents spells"""

    def __init__(self, name, cost, effect):
        self.name = name
        self.cost = cost
        self.effect = effect

    def cast(self):
        """Returns the effect of the spell."""
        return copy.deepcopy(self.effect)

class SpellEffect(object):
    """Represents spell effect."""

    def __init__(self, spell_name, duration, caster_effect, target_effect):
        """
        Duration is twice the number of rounds because spell
        effects are applied twice per round.
        """
        self.spell_name = spell_name
        self.duration = duration
        self.caster_effect = caster_effect
        self.target_effect = target_effect

        self.caster = None
        self.target = None
        self.timer = 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "%s (%d): caster %s | target %s" \
               % (self.spell_name, self.timer, \
                 str(self.caster_effect), str(self.target_effect))

    def activate(self, caster, target):
        """Activates the spell with the given caster and target."""
        self.caster = caster
        self.target = target
        self.timer = self.duration

    def execute(self):
        """Executes changes on characters."""
        # target, boss only gets damage
        self.target.hit_points += self.target_effect.hit_points

        # caster
        self.caster.hit_points += self.caster_effect.hit_points
        self.caster.mana += self.caster_effect.mana
        # shield isn't additive
        if self.caster.armor < self.caster_effect.armor:
            self.caster.armor = self.caster_effect.armor

        # tick
        self.timer -= 1

    def deactivate(self):
        """Deactivates a spell, removing any temporary effects."""
        # armor
        self.caster.armor -= self.caster_effect.armor

class CharacterEffects(object):
    """Represents the effects on a given character."""

    def __init__(self, hit_points=0, armor=0, mana=0):
        """
        hit_points:  The effect on the character's hitpoints,
                     positive number for healing, negative for damage

        armor:       The effect on the character's armor

        mana:        The effect on the character's mana
        """
        self.hit_points = hit_points
        self.armor = armor
        self.mana = mana

    def __str__(self):
        return "%d hp; %d armor; %d mana" \
               % (self.hit_points, self.armor, self.mana)

