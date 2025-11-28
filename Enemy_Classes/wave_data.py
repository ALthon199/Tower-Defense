WAVE_DATA ={
    "wave_1": {
        "description": "The Basics: A simple, slow trickle to introduce the enemy.",
        "duration": 8,
        "reward": 100,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 5, "spawn_delay": 1, "start_time": 0 }
        ]
    },
    "wave_2": {
        "description": "More of Them: A larger group, spawning slightly faster.",
        "duration": 20,
        "reward": 120,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 10, "spawn_delay": 1.5, "start_time": 1 }
        ]
    },
    "wave_3": {
        "description": "The First Pressure Test: A dense cluster of enemies spawning quickly.",
        "duration": 15,
        "reward": 150,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 12, "spawn_delay": 0.5, "start_time": 0 }
        ]
    },
    "wave_4": {
        "description": "Introducing Armor: A steady stream of zombies is joined by the new, durable Shield Zombies.",
        "duration": 25,
        "reward": 180,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 8, "spawn_delay": 2.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 4, "spawn_delay": 2.5, "start_time": 5 }
        ]
    },
    "wave_5": {
        "description": "The Swarm: A pure endurance test with a very large number of grunts in a tight formation.",
        "duration": 20,
        "reward": 250,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 25, "spawn_delay": 0.25, "start_time": 0 }
        ]
    },
    "wave_6": {
        "description": "Breathe and Panic: Two distinct, dense groups with a pause. The second group is shielded.",
        "duration": 30,
        "reward": 220,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 15, "spawn_delay": 0.4, "start_time": 2 },
            { "mob_type": "Shield_Zombie", "count": 10, "spawn_delay": 0.8, "start_time": 15 }
        ]
    },
    "wave_7": {
        "description": "Overlapping Streams: Three separate streams, including a shielded contingent, create chaos.",
        "duration": 35,
        "reward": 300,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 10, "spawn_delay": 1.8, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 8, "spawn_delay": 1.5, "start_time": 4 },
            { "mob_type": "Zombie", "count": 10, "spawn_delay": 0.5, "start_time": 8 }
        ]
    },
    "wave_8": {
        "description": "The Feint: Starts deceptively slow, then unleashes a massive, mixed horde.",
        "duration": 25,
        "reward": 350,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 3, "spawn_delay": 3.0, "start_time": 0 },
            { "mob_type": "Zombie", "count": 20, "spawn_delay": 0.2, "start_time": 10 },
            { "mob_type": "Shield_Zombie", "count": 10, "spawn_delay": 0.5, "start_time": 11 }
        ]
    },
    "wave_9": {
        "description": "Building Crescendo: The pressure constantly increases as new, shielded streams are added.",
        "duration": 30,
        "reward": 450,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 20, "spawn_delay": 1.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 15, "spawn_delay": 0.7, "start_time": 5 } 
        ]
    },
    "wave_10": {
        "description": "The Final Swarm: A relentless, multi-pronged assault led by a powerful Boss.",
        "duration": 40,
        "reward": 1000,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 25, "spawn_delay": 0.3, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 20, "spawn_delay": 0.4, "start_time": 2 },
            { "mob_type": "Zombie", "count": 15, "spawn_delay": 0.1, "start_time": 15 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 1.0, "start_time": 20 },
            { "mob_type": "Shield_Zombie", "count": 15, "spawn_delay": 0.2, "start_time": 25 }
        ]
    },
    
    
    
    "wave_11": {
        "description": "Shield Wall I: Initial wave of Shield Zombies at high density.",
        "duration": 25,
        "reward": 550,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 20, "spawn_delay": 0.8, "start_time": 0 }
        ]
    },
    "wave_12": {
        "description": "Split Armor: Two separate armored streams with a short gap.",
        "duration": 30,
        "reward": 600,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 15, "spawn_delay": 1.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 15, "spawn_delay": 1.0, "start_time": 10 }
        ]
    },
    "wave_13": {
        "description": "Armored Push: Shield Zombies quickly followed by a large cleanup group of grunts.",
        "duration": 35,
        "reward": 650,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 18, "spawn_delay": 0.7, "start_time": 0 },
            { "mob_type": "Zombie", "count": 25, "spawn_delay": 0.5, "start_time": 8 }
        ]
    },
    "wave_14": {
        "description": "Sustained Armor: A long, slow-burning stream of pure Shield Zombies.",
        "duration": 50,
        "reward": 700,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 30, "spawn_delay": 1.2, "start_time": 0 }
        ]
    },
    "wave_15": {
        "description": "Armor & Grunt Overlap: High pressure from both armored and standard units simultaneously.",
        "duration": 35,
        "reward": 750,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 20, "spawn_delay": 0.5, "start_time": 0 },
            { "mob_type": "Zombie", "count": 30, "spawn_delay": 0.3, "start_time": 3 }
        ]
    },
    "wave_16": {
        "description": "Shield Wall II: Max density of armored units, spawning very fast.",
        "duration": 25,
        "reward": 800,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 25, "spawn_delay": 0.4, "start_time": 0 }
        ]
    },
    "wave_17": {
        "description": "The Deception: A few grunts, followed by a massive, quick armored contingent.",
        "duration": 30,
        "reward": 850,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 5, "spawn_delay": 3.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 30, "spawn_delay": 0.6, "start_time": 10 }
        ]
    },
    "wave_18": {
        "description": "Triple Armored Threat: Three separate armored streams with no pauses.",
        "duration": 45,
        "reward": 900,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 10, "spawn_delay": 1.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 10, "spawn_delay": 0.7, "start_time": 5 },
            { "mob_type": "Shield_Zombie", "count": 10, "spawn_delay": 0.5, "start_time": 10 }
        ]
    },
    "wave_19": {
        "description": "Grunt Flood: A huge number of grunts, with armor cleaning up the rear.",
        "duration": 35,
        "reward": 950,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 50, "spawn_delay": 0.3, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 10, "spawn_delay": 1.5, "start_time": 15 }
        ]
    },
    "wave_20": {
        "description": "Mini-Boss Run: A Boss unit escorted by a dense stream of Shield Zombies.",
        "duration": 50,
        "reward": 1750,
        "spawn_events": [
            { "mob_type": "Boss", "count": 1, "spawn_delay": 15.0, "start_time": 10 },
            { "mob_type": "Shield_Zombie", "count": 35, "spawn_delay": 0.7, "start_time": 0 }
        ]
    },
    
    
    
    "wave_21": {
        "description": "Duration Test I: A sustained, long-duration stream of mixed units.",
        "duration": 60,
        "reward": 1050,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 40, "spawn_delay": 1.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 20, "spawn_delay": 2.0, "start_time": 0 }
        ]
    },
    "wave_22": {
        "description": "Double Overlap: Two tight waves start close together.",
        "duration": 40,
        "reward": 1100,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 25, "spawn_delay": 0.4, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 20, "spawn_delay": 0.5, "start_time": 4 }
        ]
    },
    "wave_23": {
        "description": "The Grinder: A long wave with a constant, slow mix of both types.",
        "duration": 70,
        "reward": 1150,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 50, "spawn_delay": 1.5, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 25, "spawn_delay": 2.0, "start_time": 0 }
        ]
    },
    "wave_24": {
        "description": "Triple Grunt Stack: Three separate, quick streams of grunts, followed by armor.",
        "duration": 45,
        "reward": 1200,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 15, "spawn_delay": 0.3, "start_time": 0 },
            { "mob_type": "Zombie", "count": 15, "spawn_delay": 0.3, "start_time": 5 },
            { "mob_type": "Zombie", "count": 15, "spawn_delay": 0.3, "start_time": 10 },
            { "mob_type": "Shield_Zombie", "count": 15, "spawn_delay": 0.8, "start_time": 20 }
        ]
    },
    "wave_25": {
        "description": "Mid-Game Siege: A full, sustained attack from all non-Boss units.",
        "duration": 50,
        "reward": 1300,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 30, "spawn_delay": 0.7, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 25, "spawn_delay": 0.8, "start_time": 0 }
        ]
    },
    "wave_26": {
        "description": "Duration Test II: A very long, low-delay stream of armored units.",
        "duration": 65,
        "reward": 1400,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 50, "spawn_delay": 0.8, "start_time": 0 }
        ]
    },
    "wave_27": {
        "description": "Heavy Overlap: Grunts at max density overlap perfectly with a heavy armored stream.",
        "duration": 55,
        "reward": 1500,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 40, "spawn_delay": 0.3, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 30, "spawn_delay": 0.5, "start_time": 0 }
        ]
    },
    "wave_28": {
        "description": "Breaker Wave: Designed to overwhelm towers with sheer numbers before a short pause.",
        "duration": 40,
        "reward": 1600,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 60, "spawn_delay": 0.2, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 20, "spawn_delay": 0.5, "start_time": 5 }
        ]
    },
    "wave_29": {
        "description": "Double Armored Blockade: Two highly dense streams of Shield Zombies start close together.",
        "duration": 45,
        "reward": 1700,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 25, "spawn_delay": 0.4, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 25, "spawn_delay": 0.5, "start_time": 10 }
        ]
    },
    "wave_30": {
        "description": "Mega-Boss Escort: The biggest wave yet, featuring a Boss unit and maximum density armored support.",
        "duration": 60,
        "reward": 2500,
        "spawn_events": [
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 15 },
            { "mob_type": "Shield_Zombie", "count": 40, "spawn_delay": 0.5, "start_time": 0 },
            { "mob_type": "Zombie", "count": 50, "spawn_delay": 0.3, "start_time": 5 }
        ]
    },
    
    
    
    "wave_31": {
        "description": "Frequent Boss I: Boss appears early, escorted by a moderate swarm of grunts.",
        "duration": 40,
        "reward": 1900,
        "spawn_events": [
            { "mob_type": "Boss", "count": 1, "spawn_delay": 10.0, "start_time": 0 },
            { "mob_type": "Zombie", "count": 30, "spawn_delay": 0.8, "start_time": 0 }
        ]
    },
    "wave_32": {
        "description": "Armored Isolation: A single, long stream of Shield Zombies, testing sustained armor penetration.",
        "duration": 70,
        "reward": 2000,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 60, "spawn_delay": 0.9, "start_time": 0 }
        ]
    },
    "wave_33": {
        "description": "Boss & Armor Overlap: Boss spawns simultaneously with a dense armored stream.",
        "duration": 50,
        "reward": 2100,
        "spawn_events": [
            { "mob_type": "Boss", "count": 1, "spawn_delay": 15.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 30, "spawn_delay": 0.6, "start_time": 0 }
        ]
    },
    "wave_34": {
        "description": "Triple Threat Reloaded: Heavy pressure from all non-Boss types, constant and tight.",
        "duration": 65,
        "reward": 2200,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 40, "spawn_delay": 0.5, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 35, "spawn_delay": 0.7, "start_time": 0 }
        ]
    },
    "wave_35": {
        "description": "Double Boss I: Two Boss units appear, separated by a wave of Shield Zombies.",
        "duration": 75,
        "reward": 3500,
        "spawn_events": [
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 25, "spawn_delay": 0.8, "start_time": 10 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 30 }
        ]
    },
    "wave_36": {
        "description": "Maximum Grunt Flood: The absolute highest volume of standard grunts possible.",
        "duration": 50,
        "reward": 2400,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 80, "spawn_delay": 0.1, "start_time": 0 }
        ]
    },
    "wave_37": {
        "description": "Armored Wall III: A relentless stream of Shield Zombies with almost no gap.",
        "duration": 70,
        "reward": 2500,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 60, "spawn_delay": 0.5, "start_time": 0 }
        ]
    },
    "wave_38": {
        "description": "Boss sandwich: Grunts, Boss, then Shield Zombies.",
        "duration": 60,
        "reward": 2600,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 20, "spawn_delay": 0.5, "start_time": 0 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 15.0, "start_time": 10 },
            { "mob_type": "Shield_Zombie", "count": 30, "spawn_delay": 0.4, "start_time": 25 }
        ]
    },
    "wave_39": {
        "description": "Final Push Prep: Extreme density of mixed units to drain resources.",
        "duration": 80,
        "reward": 2800,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 50, "spawn_delay": 0.6, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 40, "spawn_delay": 0.8, "start_time": 0 }
        ]
    },
    "wave_40": {
        "description": "Triple Boss II: Three Boss units separated by short, high-density armored waves.",
        "duration": 85,
        "reward": 5000,
        "spawn_events": [
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 20, "spawn_delay": 0.3, "start_time": 10 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 30 },
            { "mob_type": "Shield_Zombie", "count": 20, "spawn_delay": 0.3, "start_time": 40 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 60 }
        ]
    },
    
    
    
    "wave_41": {
        "description": "The Relentless Flow: Non-stop, tight-knit streams of both unit types.",
        "duration": 70,
        "reward": 3500,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 70, "spawn_delay": 0.4, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 50, "spawn_delay": 0.6, "start_time": 0 }
        ]
    },
    "wave_42": {
        "description": "Armored Blockade IV: Pure, continuous stream of Shield Zombies at max spawn rate.",
        "duration": 60,
        "reward": 3750,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 70, "spawn_delay": 0.3, "start_time": 0 }
        ]
    },
    "wave_43": {
        "description": "Boss Cycle: Bosses appear, followed by a grunt rush, followed by another Boss.",
        "duration": 80,
        "reward": 4000,
        "spawn_events": [
            { "mob_type": "Boss", "count": 1, "spawn_delay": 15.0, "start_time": 0 },
            { "mob_type": "Zombie", "count": 40, "spawn_delay": 0.2, "start_time": 10 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 15.0, "start_time": 40 }
        ]
    },
    "wave_44": {
        "description": "Endurance Wall: A marathon wave combining a long armored stream and a grunt flood.",
        "duration": 90,
        "reward": 4250,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 60, "spawn_delay": 1.0, "start_time": 0 },
            { "mob_type": "Zombie", "count": 70, "spawn_delay": 0.8, "start_time": 15 }
        ]
    },
    "wave_45": {
        "description": "Quad Boss I: Four Bosses separated by ultra-dense shielded waves.",
        "duration": 100,
        "reward": 6500,
        "spawn_events": [
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 30, "spawn_delay": 0.4, "start_time": 10 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 30 },
            { "mob_type": "Shield_Zombie", "count": 30, "spawn_delay": 0.4, "start_time": 40 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 60 },
            { "mob_type": "Shield_Zombie", "count": 30, "spawn_delay": 0.4, "start_time": 70 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 85 }
        ]
    },
    "wave_46": {
        "description": "Non-Stop Combined: Maximum spawn rate for both standard and shielded units.",
        "duration": 70,
        "reward": 4750,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 80, "spawn_delay": 0.3, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 60, "spawn_delay": 0.4, "start_time": 0 }
        ]
    },
    "wave_47": {
        "description": "Double Massive Shield: Two huge, simultaneous waves of Shield Zombies.",
        "duration": 80,
        "reward": 5000,
        "spawn_events": [
            { "mob_type": "Shield_Zombie", "count": 50, "spawn_delay": 0.5, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 50, "spawn_delay": 0.5, "start_time": 10 }
        ]
    },
    "wave_48": {
        "description": "Final Grunt Assault: A final, overwhelming wave of grunts to clear out single-target defenses.",
        "duration": 75,
        "reward": 5500,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 100, "spawn_delay": 0.2, "start_time": 0 }
        ]
    },
    "wave_49": {
        "description": "The Final Preparation: A mixed wave with maximum count and minimal delay before the grand finale.",
        "duration": 90,
        "reward": 6000,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 70, "spawn_delay": 0.4, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 50, "spawn_delay": 0.5, "start_time": 0 }
        ]
    },
    "wave_50": {
        "description": "The Grand Siege: A sustained, multi-Boss assault featuring five Boss units with non-stop maximum-density armored support.",
        "duration": 120,
        "reward": 15000,
        "spawn_events": [
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 0 },
            { "mob_type": "Shield_Zombie", "count": 40, "spawn_delay": 0.3, "start_time": 5 },
            { "mob_type": "Zombie", "count": 50, "spawn_delay": 0.2, "start_time": 10 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 30 },
            { "mob_type": "Shield_Zombie", "count": 50, "spawn_delay": 0.2, "start_time": 35 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 60 },
            { "mob_type": "Zombie", "count": 60, "spawn_delay": 0.15, "start_time": 65 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 90 },
            { "mob_type": "Shield_Zombie", "count": 60, "spawn_delay": 0.15, "start_time": 95 },
            { "mob_type": "Boss", "count": 1, "spawn_delay": 20.0, "start_time": 105 }
        ]
    }
}