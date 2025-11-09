WAVE_DATA = {
    "wave_1": {
        "description": "The Basics: A simple, slow trickle to introduce the enemy.",
        "duration": 8,
        "reward": 500,
        "spawn_events": [
            { "mob_type": "Zombie", "count": 30, "spawn_delay": 0.1, "start_time": 0 }
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
    } 
}