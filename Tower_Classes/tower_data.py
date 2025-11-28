
ARCHER_DATA = [
    # Level 1: Start
    {"Cost": 75, "Range": 200, "Cooldown": 750, "Damage": 50, "Upgrade": 100,
     "Description": """Lvl 1: Hit 1 enemy. \nDMG 50. Range 200. \nWait 0.75 seconds."""},

    # Level 2: Better damage and speed
    {"Range": 250, "Cooldown": 600, "Damage": 85, "Upgrade": 180,
     "Description": """Lvl 2: Hit 1 enemy. \nDMG 85. Range 250. \nWait 0.6 seconds."""},

    # Level 3: Max power
    {"Range": 300, "Cooldown": 450, "Damage": 130, "Upgrade": None,
     "Description": """Lvl 3: Hit 1 enemy. \nDMG 130. Range 300. \nWait 0.45 seconds. Max power."""},
]


ZAP_DATA = [
    # Level 1: Hits 3 enemies
    {"Cost": 150, "Range": 120, "Cooldown": 700, "Damage": 40, "Chain": 3, "Upgrade": 200,
     "Description": """Lvl 1: Hits 3 nearby enemies. \nDMG 40. Range 120. \nWait 0.7 seconds."""},

    # Level 2: Hits 5 enemies
    {"Range": 130, "Cooldown": 550, "Damage": 60, "Chain": 5, "Upgrade": 400,
     "Description": """Lvl 2: Hits 5 nearby enemies. \nDMG 60. Range 130. \nWait 0.55 seconds."""},

    # Level 3: Hits 8 enemies
    {"Range": 140, "Cooldown": 400, "Damage": 85, "Chain": 8, "Upgrade": None,
     "Description": """Lvl 3: Hits 8 nearby enemies. \nDMG 85. Range 140. \nWait 0.4 seconds. Max chain."""},
]


CATAPULT_DATA = [
    # Level 1: Small splash (Scale 2). Low damage, fast fire.
    {"Cost": 60, "Range": 220, "Cooldown": 750, "Damage": 30, 'explosion_scale' : 2, "Upgrade": 90,
     "Description": """Lvl 1: Splash damage. \nDMG 30. Range 220. \nWait 0.75s. Small area."""},

    # Level 2: Medium splash (Scale 3).
    {"Range": 260, "Cooldown": 650, "Damage": 45, 'explosion_scale' : 3, "Upgrade": 180,
     "Description": """Lvl 2: Splash damage. \nDMG 45. Range 260. \nWait 0.65s. Medium area."""},

    # Level 3: Max splash (Scale 5). Still less powerful than previous Lvl 2.
    {"Range": 300, "Cooldown": 550, "Damage": 60, 'explosion_scale' : 5, "Upgrade": None,
     "Description": """Lvl 3: Splash damage. \nDMG 60. Range 300. \nWait 0.55s. Max splash area."""},
]

FIRE_DATA = [
    # Level 1: Shoots LEFT, pushes 10
    {"Cost": 75, "Range": 180, "Cooldown": 750, "Damage": 55, "Push_Back": 20, "Upgrade": 100,
     "Pattern": ["LEFT"], 
     "Description": """Lvl 1: Shoots LEFT. \nDMG 55. Range 180. \nPush 10. Wait 0.75s."""},

    # Level 2: Shoots LEFT/RIGHT, pushes 15
    {"Range": 200, "Cooldown": 625, "Damage": 70, "Push_Back": 30, "Upgrade": 175,
     "Pattern": ["LEFT", "RIGHT"], 
     "Description": """Lvl 2: Shoots L/R. \nDMG 70. Range 200. \nPush 15. Wait 0.625s."""},

    # Level 3: Shoots ALL, pushes 25
    {"Range": 220, "Cooldown": 550, "Damage": 90, "Push_Back": 50, "Upgrade": None,
     "Pattern": ["LEFT", "RIGHT", "UP", "DOWN"], 
     "Description": """Lvl 3: Shoots ALL ways. \nDMG 90. Range 220. \nPush 25. Wait 0.55s. Max push."""},
]