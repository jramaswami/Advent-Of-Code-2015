"""Different strategies for picking spells for combat."""

import operator
import random

class ShieldsUpSpellList(object):
    """Strategy giving priority to shield."""
    def __init__(self, spell_book):
        self.effects = None
        self.player = None
        self.spell_book = spell_book
        self.spells_cast = []
        self.cost = 0

    def __iter__(self):
        return self

    def next(self):
        """Return next spell."""
        spell = None

        spells_in_effect = [e.spell_name for e in self.effects]
        if 'Shield' not in spells_in_effect:
            if self.player.mana - self.spell_book.get_spell_cost('Shield') \
               < self.spell_book.get_spell_cost('Recharge'):
                spell = 'Recharge'
            else:
                spell = 'Shield'
        elif 'Poison' not in spells_in_effect:
            if self.player.mana - self.spell_book.get_spell_cost('Poison') \
               < self.spell_book.get_spell_cost('Recharge'):
                spell = 'Recharge'
            else:
                spell = 'Poison'
        elif 'Drain' not in spells_in_effect:
            if self.player.mana - self.spell_book.get_spell_cost('Drain') \
               < self.spell_book.get_spell_cost('Recharge'):
                spell = 'Recharge'
            else:
                spell = 'Drain'

        return spell

    def set_environ(self, player, effects):
        """Set the environment so that spell can be chosen."""
        self.player = player
        self.effects = effects


class MaxDamageSpellList(object):
    """Strategy to use strategy of most damage."""
    def __init__(self, spell_book):
        self.effects = None
        self.player = None
        self.spell_book = spell_book
        self.spells_cast = []
        self.cost = 0

    def __iter__(self):
        return self

    def next(self):
        """Return next spell."""
        spells_in_effect = [e.spell_name for e in self.effects]
        for spell_name in ['Poison', 'Magic Missile']:
            if spell_name not in spells_in_effect:
                if self.player.can_cast_spell(spell_name):
                    self.cost += self.spell_book.get_spell_cost(spell_name)
                    self.spells_cast.append(spell_name)
                    return spell_name

        return None

    def set_environ(self, player, effects):
        """Set the environment so that spell can be chosen."""
        self.player = player
        self.effects = effects


class RandomSpellList(object):
    """Strategy to go with the maximum possible cost spell available."""
    def __init__(self, spell_book):
        self.effects = None
        self.player = None
        self.spell_book = spell_book
        self.spell_names = [k for k in self.spell_book.spells.keys()]
        self.spells_cast = []
        self.cost = 0

    def __iter__(self):
        return self

    def next(self):
        """Return next spell."""
        spells_in_effect = [e.spell_name for e in self.effects]
        random.shuffle(self.spell_names)
        for spell_name in self.spell_names:
            if spell_name not in spells_in_effect:
                if self.player.can_cast_spell(spell_name):
                    self.cost += self.spell_book.get_spell_cost(spell_name)
                    self.spells_cast.append(spell_name)
                    return spell_name

        return None

    def set_environ(self, player, effects):
        """Set the environment so that spell can be chosen."""
        self.player = player
        self.effects = effects

class MaxCostSpellList(object):
    """Strategy to go with the maximum possible cost spell available."""
    def __init__(self, spell_book):
        self.effects = None
        self.player = None
        self.spell_book = spell_book
        self.spells_by_cost = sorted(self.spell_book.spells.items(),
                                     key=operator.itemgetter(1),
                                     reverse=True)
        self.spells_cast = []
        self.cost = 0

    def __iter__(self):
        return self

    def next(self):
        """Return next spell."""
        spells_in_effect = [e.spell_name for e in self.effects]
        for spell_name, spell_cost in self.spells_by_cost:
            if spell_name not in spells_in_effect:
                if self.player.can_cast_spell(spell_name):
                    self.cost += spell_cost
                    self.spells_cast.append(spell_name)
                    return spell_name

        return None

    def set_environ(self, player, effects):
        """Set the environment so that spell can be chosen."""
        self.player = player
        self.effects = effects

class SpellList(object):
    """Represents the strategy of a list of spells."""

    def __init__(self, spell_list):
        self.spell_list = iter(spell_list)
        self.effects = None
        self.player = None

    def __iter__(self):
        return self

    def next(self):
        """Return next spell."""
        return self.spell_list.next()

    def set_environ(self, player, effects):
        """Set the environment so that spell can be chosen."""
        self.player = player
        self.effects = effects

