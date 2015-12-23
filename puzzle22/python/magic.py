"""Classes for magic in simulation."""

def get_spell_cost(spell):
    """Return cost of spell."""
    return SPELLBOOK[spell]['cost']

def magic_missile(player, boss, effects):
    """Magic Missile spell."""
    boss.hit_points -= 4

def drain(player, boss, effects):
    """Drain spell."""
    player.hit_points += 2
    boss.hit_points -= 2

def shield(player, boss, effects):
    """Shield spell."""
    player.armor = 7
    effects['Shield'] = 6

def shield_effect(player, boss):
    """Shield effect."""
    player.armor = 7

def shield_expire(player, boss):
    """Expire shield."""
    player.armor = player.original_armor

def poison(player, boss, effects):
    """Add poison effect."""
    effects['Poison'] = 6

def poison_effect(player, boss):
    """Poison effect."""
    boss.hit_points -= 3

def recharge(player, boss, effects):
    """Recharge spell."""
    effects['Recharge'] = 5

def recharge_effect(player, boss):
    """Recharge effect."""
    player.mana += 101

def score_spell_list(spell_list):
    """Returns the score for given spell list."""
    return sum([SPELLBOOK[s]['cost'] for s in spell_list])

SPELLBOOK = {'Magic Missile': {'cost': 53, 'func': magic_missile},
             'Drain': {'cost': 73, 'func': drain},
             'Shield': {'cost': 113, 'func': shield},
             'Poison': {'cost': 173, 'func': poison},
             'Recharge': {'cost': 229, 'func': recharge},}

EFFECTS = {'Poison': poison_effect, 'Shield': shield_effect, \
           'Recharge': recharge_effect}

