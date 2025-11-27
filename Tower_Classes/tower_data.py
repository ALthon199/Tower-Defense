ARCHER_DATA = [
    # Base Tower (Level 1)
    {"Cost": 50, "Range": 200, "Cooldown": 1500, "Damage": 45, "Upgrade": 75,
     "Description": """Lvl 1: DMG 45. Range 200. \nCD 1500ms.\nSingle Target."""},

    # Upgrade 1 (Level 2)
    {"Range": 240, "Cooldown": 1250, "Damage": 65, "Upgrade": 125,
     "Description": """Lvl 2: DMG 65. Range 240. \nCD 1250ms.\nHigh Efficiency."""},

    # Upgrade 2 (Level 3)
    {"Range": 280, "Cooldown": 1000, "Damage": 90, "Upgrade": None,
     "Description": """Lvl 3: DMG 90. Range 280. \nCD 1000ms.\nMax Single Target DPS."""},
]



ZAP_DATA = [
    # Base Tower (Level 1)
    {"Cost": 125, "Range": 110, "Cooldown": 1400, "Damage": 30, "Chain": 2, "Upgrade": 150,
     "Description": """Lvl 1: DMG 30. Range 110. \nCD 1400ms. Chain 2.\nChain Lightning."""},

    # Upgrade 1 (Level 2)
    {"Range": 110, "Cooldown": 1100, "Damage": 45, "Chain": 4, "Upgrade": 350,
     "Description": """Lvl 2: DMG 45. Range 110. \nCD 1100ms. Chain 4.\nIncreased Chain Targets."""},

    # Upgrade 2 (Level 3)
    {"Range": 115, "Cooldown": 800, "Damage": 75, "Chain": 8, "Upgrade": None,
     "Description": """Lvl 3: DMG 75. Range 115. \nCD 800ms. Chain 8.\nMaximum Chain Capacity."""},
]



CATAPULT_DATA = [
    # Base Tower (Level 1)
    {"Cost": 50, "Range": 200, "Cooldown": 1500, "Damage": 45, 'explosion_scale' : 2, "Upgrade": 75,
     "Description": """Lvl 1: DMG 45. Range 200. \nCD 1500ms. Scale 2.\nArea Damage."""},

    # Upgrade 1 (Level 2)
    {"Range": 240, "Cooldown": 1250, "Damage": 65, 'explosion_scale' : 4, "Upgrade": 125,
     "Description": """Lvl 2: DMG 65. Range 240. \nCD 1250ms. Scale 4.\nLarger AoE."""},

    # Upgrade 2 (Level 3)
    {"Range": 280, "Cooldown": 1000, "Damage": 90, 'explosion_scale' : 8, "Upgrade": None,
     "Description": """Lvl 3: DMG 90. Range 280. \nCD 1000ms. Scale 8.\nMax AoE and Damage."""},
]