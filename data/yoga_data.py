# --------------------------------------------------
# Complete chapter and subchapter structure (from your book)
# --------------------------------------------------

SUBCHAPTERS = {
    "Standing Poses": [
        "Mountain pose",
        "Side bends",
        "Standing backbends",
        "One leg standing balance",
        "Standing forward bends",
        "Legs wide",
        "Downward dog",
        "Intense side stretch",
        "Triangle pose",
        "Warrior and side angle poses",
        "Lunges and kneeling poses",
        "Squats"
    ],
    "Seated Poses": [
        "Easy pose",
        "Accomplished one pose",
        "Fire log pose",
        "Half lotus and lotus pose",
        "Both knees bent",
        "Bound angle pose",
        "Star pose",
        "Legs in front",
        "Horizontal splits",
        "Legs straight in front",
        "Garuda legs",
        "Leg cradle",
        "Head to knee",
        "Hero pose",
        "Thunderbolt pose",
        "One knee bent (variations)",
        "Cow face pose",
        "Sage Vamadeva’s pose",
        "One-legged king pigeon pose",
        "Vertical splits"
    ],
    "Core Poses": [
        "Boat pose",
        "Six triangles pose",
        "Supine poses"
    ],
    "Quadruped Poses": [
        "Child’s pose",
        "Rabbit pose",
        "Cow pose",
        "All fours (variations)",
        "Plank pose",
        "Plank on forearms",
        "Four limbed staff pose",
        "Side plank"
    ],
    "Backbends": [
        "Cow face pose and garuda on knees",
        "Knees on the floor",
        "Backbend on the knees",
        "Backbend",
        "Upward bow pose",
        "Wild thing pose"
    ],
    "Arm Balances": [
        "Lotus pose",
        "Pendant pose",
        "One leg over the shoulder",
        "Crane pose",
        "Firefly pose",
        "Scissor legs",
        "Garuda legs",
        "Peacock and swan poses"
    ],
    "Inversion Poses": [
        "Duck pose",
        "Dolphin pose",
        "Peacock feather pose",
        "Backbends on forearms",
        "Handstands (variations)",
        "Headstands (variations)",
        "Shoulderstand (variations)",
        "Plow pose"
    ],
    "Prone Poses": [
        "Stomach on the floor",
        "Chest facing the floor",
        "Locust pose",
        "Sphinx pose",
        "Cobra pose",
        "King pigeon pose",
        "Upward dog pose",
        "Cobra pose 2",
        "Bow pose",
        "Half lotus and lotus backbends",
        "Sage Gheranda’s pose",
        "Backbends",
        "Chin and chest on the floor",
        "Chest and knees on the floor"
    ],
    "Supine Poses": [
        "Shoulder on the floor",
        "Triceps on the floor",
        "Elbow on the floor",
        "Forearm on the floor",
        "Eastern intense stretch",
        "Bridge poses",
        "Head and sitting bones on the floor",
        "Bound angle pose",
        "Knees bent",
        "Happy baby pose",
        "One and both feet behind head",
        "Horizontal splits",
        "One knee bent to the back (variations)",
        "Vertical splits",
        "Both legs straight and together",
        "Supine lotus and corpse pose"
    ]
}

# --------------------------------------------------
# Class sequence structure: section → chapter
# (The Core Block is inserted between Arm Strength and Core Poses)
# --------------------------------------------------

FLOW = [
    ("Arrival & Breath", "Seated Poses"),
    ("Warm-up", "Quadruped Poses"),
    ("Standing Sequence", "Standing Poses"),
    ("Side Bends / Wide-Leg Poses", "Standing Poses"),
    ("Backbend Preparation", "Prone Poses"),
    ("Backbends", "Backbends"),
    ("Arm Strength", "Arm Balances"),
    # --- Core Block inserted here ---
    ("Core", "Core Poses"),  # ← Book chapter "Core Poses" stays as its own section
    ("Inversions", "Inversion Poses"),
    ("Counterposes & Stretch", "Seated Poses"),
    ("Relaxation", "Supine Poses"),
]

# --------------------------------------------------
# Focus profiles → preferred subchapters per chapter
# (All subchapters appear at least once)
# --------------------------------------------------

FOCUS = {
    "Strength": {
        "Standing Poses": [
            "Warrior and side angle poses", "Squats", "Lunges and kneeling poses",
            "Triangle pose", "Downward dog", "Intense side stretch",
            "Standing backbends", "Legs wide", "Mountain pose"
        ],
        "Seated Poses": [
            "Hero pose", "Thunderbolt pose", "Cow face pose",
            "One-legged king pigeon pose", "Legs straight in front",
            "Head to knee", "Fire log pose", "Accomplished one pose",
            "Easy pose", "Star pose", "Legs in front", "Both knees bent",
            "Half lotus and lotus pose", "Garuda legs", "Leg cradle",
            "One knee bent (variations)", "Sage Vamadeva’s pose",
            "Vertical splits", "Horizontal splits", "Bound angle pose"
        ],
        "Core Poses": [
            "Boat pose", "Six triangles pose", "Supine poses"
        ],
        "Quadruped Poses": [
            "Plank pose", "Plank on forearms", "Four limbed staff pose",
            "Side plank", "Cow pose", "Rabbit pose", "All fours (variations)",
            "Child’s pose"
        ],
        "Backbends": [
            "Upward bow pose", "Backbend", "Backbend on the knees",
            "Knees on the floor", "Wild thing pose",
            "Cow face pose and garuda on knees"
        ],
        "Arm Balances": [
            "Crane pose", "Firefly pose", "Scissor legs", "Pendant pose",
            "Garuda legs", "One leg over the shoulder",
            "Peacock and swan poses", "Lotus pose"
        ],
        "Inversion Poses": [
            "Handstands (variations)", "Headstands (variations)",
            "Shoulderstand (variations)", "Plow pose",
            "Dolphin pose", "Peacock feather pose",
            "Backbends on forearms", "Duck pose"
        ],
        "Prone Poses": [
            "Locust pose", "Cobra pose", "Upward dog pose", "Bow pose",
            "King pigeon pose", "Sphinx pose",
            "Stomach on the floor", "Chest facing the floor",
            "Cobra pose 2", "Half lotus and lotus backbends",
            "Sage Gheranda’s pose", "Backbends",
            "Chin and chest on the floor", "Chest and knees on the floor"
        ],
        "Supine Poses": [
            "Bridge poses", "Eastern intense stretch",
            "Bound angle pose", "Happy baby pose",
            "Shoulder on the floor", "Triceps on the floor",
            "Elbow on the floor", "Forearm on the floor",
            "Head and sitting bones on the floor", "Knees bent",
            "One and both feet behind head", "Horizontal splits",
            "One knee bent to the back (variations)", "Vertical splits",
            "Both legs straight and together", "Supine lotus and corpse pose"
        ],
    },

    "Core": {
        "Standing Poses": [
            "One leg standing balance", "Standing forward bends",
            "Warrior and side angle poses", "Triangle pose",
            "Downward dog", "Intense side stretch", "Squats"
        ],
        "Seated Poses": [
            "Legs straight in front", "Head to knee",
            "Cow face pose", "Fire log pose",
            "Hero pose", "Thunderbolt pose",
            "Accomplished one pose", "Easy pose",
            "Bound angle pose", "Garuda legs", "Leg cradle",
            "One knee bent (variations)", "Sage Vamadeva’s pose",
            "Legs in front", "Both knees bent",
            "Vertical splits", "Horizontal splits",
            "Half lotus and lotus pose", "One-legged king pigeon pose",
            "Star pose"
        ],
        "Core Poses": [
            "Boat pose", "Six triangles pose", "Supine poses"
        ],
        "Quadruped Poses": [
            "Plank pose", "Plank on forearms", "Four limbed staff pose",
            "Side plank", "All fours (variations)", "Child’s pose",
            "Rabbit pose", "Cow pose"
        ],
        "Backbends": [
            "Backbend on the knees", "Backbend",
            "Upward bow pose", "Wild thing pose",
            "Knees on the floor", "Cow face pose and garuda on knees"
        ],
        "Arm Balances": [
            "Crane pose", "Firefly pose", "Scissor legs", "Pendant pose",
            "Garuda legs", "One leg over the shoulder",
            "Peacock and swan poses", "Lotus pose"
        ],
        "Inversion Poses": [
            "Dolphin pose", "Handstands (variations)", "Headstands (variations)",
            "Shoulderstand (variations)", "Plow pose",
            "Peacock feather pose", "Backbends on forearms", "Duck pose"
        ],
        "Prone Poses": [
            "Locust pose", "Sphinx pose", "Cobra pose",
            "Upward dog pose", "Bow pose", "King pigeon pose",
            "Stomach on the floor", "Chest facing the floor",
            "Cobra pose 2", "Half lotus and lotus backbends",
            "Sage Gheranda’s pose", "Backbends",
            "Chin and chest on the floor", "Chest and knees on the floor"
        ],
        "Supine Poses": [
            "Bridge poses", "Eastern intense stretch",
            "Happy baby pose", "Bound angle pose",
            "Shoulder on the floor", "Triceps on the floor",
            "Elbow on the floor", "Forearm on the floor",
            "Head and sitting bones on the floor", "Knees bent",
            "One and both feet behind head", "Horizontal splits",
            "One knee bent to the back (variations)", "Vertical splits",
            "Both legs straight and together", "Supine lotus and corpse pose"
        ],
    },

    "Balance": {
        "Standing Poses": [
            "One leg standing balance", "Triangle pose",
            "Warrior and side angle poses", "Intense side stretch",
            "Downward dog", "Mountain pose", "Standing backbends",
            "Legs wide", "Standing forward bends", "Lunges and kneeling poses", "Squats", "Side bends"
        ],
        "Seated Poses": [
            "Garuda legs", "Leg cradle", "Accomplished one pose",
            "Half lotus and lotus pose", "Easy pose", "Hero pose",
            "Thunderbolt pose", "Star pose",
            "Legs straight in front", "Head to knee",
            "Bound angle pose", "Legs in front", "Both knees bent",
            "One knee bent (variations)", "Cow face pose",
            "Sage Vamadeva’s pose", "One-legged king pigeon pose",
            "Vertical splits", "Horizontal splits"
        ],
        "Core Poses": [
            "Boat pose", "Six triangles pose", "Supine poses"
        ],
        "Quadruped Poses": [
            "Side plank", "Plank pose", "Plank on forearms",
            "Four limbed staff pose", "All fours (variations)",
            "Child’s pose", "Rabbit pose", "Cow pose"
        ],
        "Backbends": [
            "Backbend", "Upward bow pose", "Wild thing pose",
            "Backbend on the knees", "Knees on the floor",
            "Cow face pose and garuda on knees"
        ],
        "Arm Balances": [
            "Pendant pose", "Scissor legs", "Garuda legs",
            "Crane pose", "Firefly pose",
            "One leg over the shoulder", "Peacock and swan poses", "Lotus pose"
        ],
        "Inversion Poses": [
            "Handstands (variations)", "Headstands (variations)",
            "Dolphin pose", "Peacock feather pose",
            "Shoulderstand (variations)", "Plow pose",
            "Backbends on forearms", "Duck pose"
        ],
        "Prone Poses": [
            "Locust pose", "Sphinx pose", "Cobra pose",
            "Upward dog pose", "Bow pose", "King pigeon pose",
            "Stomach on the floor", "Chest facing the floor",
            "Cobra pose 2", "Half lotus and lotus backbends",
            "Sage Gheranda’s pose", "Backbends",
            "Chin and chest on the floor", "Chest and knees on the floor"
        ],
        "Supine Poses": [
            "Happy baby pose", "Bridge poses", "Bound angle pose",
            "Eastern intense stretch",
            "Shoulder on the floor", "Triceps on the floor",
            "Elbow on the floor", "Forearm on the floor",
            "Head and sitting bones on the floor", "Knees bent",
            "One and both feet behind head", "Horizontal splits",
            "One knee bent to the back (variations)", "Vertical splits",
            "Both legs straight and together", "Supine lotus and corpse pose"
        ],
    },

    "Stretch": {
        "Standing Poses": [
            "Side bends", "Standing forward bends", "Legs wide",
            "Intense side stretch", "Downward dog",
            "Triangle pose", "Mountain pose",
            "Lunges and kneeling poses", "Standing backbends",
            "One leg standing balance", "Warrior and side angle poses", "Squats"
        ],
        "Seated Poses": [
            "Bound angle pose", "Head to knee", "Legs straight in front",
            "Both knees bent", "Legs in front", "Star pose",
            "Easy pose", "Accomplished one pose", "Thunderbolt pose",
            "Hero pose", "Fire log pose", "Cow face pose",
            "Garuda legs", "Leg cradle",
            "One knee bent (variations)", "Sage Vamadeva’s pose",
            "Half lotus and lotus pose",
            "One-legged king pigeon pose",
            "Vertical splits", "Horizontal splits"
        ],
        "Core Poses": [
            "Supine poses", "Boat pose", "Six triangles pose"
        ],
        "Quadruped Poses": [
            "Child’s pose", "All fours (variations)", "Cow pose",
            "Rabbit pose", "Plank pose", "Plank on forearms",
            "Four limbed staff pose", "Side plank"
        ],
        "Backbends": [
            "Backbend on the knees", "Knees on the floor",
            "Backbend", "Upward bow pose", "Wild thing pose",
            "Cow face pose and garuda on knees"
        ],
        "Arm Balances": [
            "Garuda legs", "Pendant pose", "Scissor legs",
            "Crane pose", "Firefly pose", "One leg over the shoulder",
            "Peacock and swan poses", "Lotus pose"
        ],
        "Inversion Poses": [
            "Dolphin pose", "Shoulderstand (variations)", "Plow pose",
            "Headstands (variations)", "Handstands (variations)",
            "Peacock feather pose", "Backbends on forearms", "Duck pose"
        ],
        "Prone Poses": [
            "Sphinx pose", "Cobra pose", "Stomach on the floor",
            "Chest facing the floor", "Locust pose", "Upward dog pose",
            "Bow pose", "King pigeon pose", "Cobra pose 2",
            "Half lotus and lotus backbends", "Sage Gheranda’s pose",
            "Backbends", "Chin and chest on the floor", "Chest and knees on the floor"
        ],
        "Supine Poses": [
            "Happy baby pose", "Bound angle pose", "Knees bent",
            "Horizontal splits", "Vertical splits",
            "Head and sitting bones on the floor",
            "Shoulder on the floor", "Triceps on the floor",
            "Elbow on the floor", "Forearm on the floor",
            "Bridge poses", "Eastern intense stretch",
            "One and both feet behind head",
            "One knee bent to the back (variations)",
            "Both legs straight and together", "Supine lotus and corpse pose"
        ],
    },
}

# --------------------------------------------------
# Back subchapters for back block
# --------------------------------------------------

BACK_SUBCHAPTERS = {
    "Quadruped Poses": [
        "Plank pose",
        "Plank on forearms",
        "Side plank",
        "All fours (variations)",
    ],
    "Prone Poses": [
        "Locust pose",
        "Sphinx pose",
        "Cobra pose",
        "Chest facing the floor",
    ],
    "Standing Poses": [
        "Warrior and side angle poses",
        "Triangle pose",
        "Downward dog",
    ],
    "Backbends": [
        "Wild thing pose",
        "Backbend",
        "Upward bow pose",
    ],
}

# --------------------------------------------------
# Additional real asanas for the Back Block
# Always assigned to "Back Focus"
# --------------------------------------------------

BACK_ASANAS_EXTRA = [
    "Shalabhasana (Locust Pose)",
    "Dhanurasana (Bow Pose)",
    "Bhujangasana (Cobra Pose)",
    "Ustrasana (Camel Pose)",
    "Setu Bandhasana (Bridge Pose – Core engaged)",

    # Arm balances
    "Bakasana (Crow Pose)",
    "Parsva Bakasana (Side Crow)",
    "Eka Pada Koundinyasana I",
    "Eka Pada Koundinyasana II",
    "Lolasana (Pendant Pose)",
    "Tolasana (Scale Pose)",
    "Bhujapidasana (Shoulder Press Pose)",
    "Astavakrasana (Eight-Angle Pose)",
    "Mayurasana (Peacock Pose)",

    # Standing balance / strength
    "Virabhadrasana III (Warrior III)",
    "Ardha Chandrasana (Half Moon)",
    "Utthita Hasta Padangusthasana (Extended Hand-to-Big-Toe Pose)",

    # Inversions
    "Pincha Mayurasana (Forearm Stand, Core focus)",
    "Adho Mukha Vrksasana (Handstand, Core variations)",
]

# --------------------------------------------------
# Combined back list (subchapters + asanas)
# --------------------------------------------------

BACK_ALL = []

# 1) Real back subchapters
for chapter, subs in BACK_SUBCHAPTERS.items():
    for sub in subs:
        BACK_ALL.append((chapter, sub))

# 2) Additional real asanas (always Back Focus)
for asana in BACK_ASANAS_EXTRA:
    BACK_ALL.append(("Back Focus", asana))

# --------------------------------------------------
# Lange Core-Asana-Liste (vollständig, wie gewünscht)
# --------------------------------------------------

CORE_ASANAS = [
    # Boat
    "Paripurna Navasana (Full Boat Pose)",
    "Ardha Navasana (Half Boat Pose)",
    "Parivrtta Navasana (Revolved Boat Pose)",
    "Ubhaya Padangusthasana (Both Big Toe Pose)",

    # Planks
    "Phalakasana (High Plank Pose)",
    "Forearm Plank",
    "Side Plank (Vasisthasana)",
    "Dolphin Plank",
    "Reverse Plank (Purvottanasana)",
    "Chaturanga Dandasana (Four-Limbed Staff Pose)",

    # Balance / Arm balances (Core focused)
    "Bakasana (Crow Pose)",
    "Parsva Bakasana (Side Crow)",
    "Eka Pada Koundinyasana I",
    "Eka Pada Koundinyasana II",
    "Lolasana (Pendant Pose)",
    "Tolasana (Scale Pose)",
    "Bhujapidasana (Shoulder Press Pose)",
    "Astavakrasana (Eight-Angle Pose)",
    "Mayurasana (Peacock Pose)",

    # Back / Stabilization
    "Shalabhasana (Locust Pose)",
    "Dhanurasana (Bow Pose)",
    "Utkatasana (Chair Pose)",
    "Utkata Konasana (Goddess Pose)",
    "Ustrasana (Camel Pose – Core engaged)",
    "Setu Bandhasana (Bridge Pose – Core engaged)",
    "Purvottanasana (Upward Plank Pose)",

    # Dynamic / Supine Core
    "Supta Padangusthasana (Core Variation)",
    "Apanasana (Knee-to-Chest with Core Control)",
    "Dead Bug Variation",
    "Leg Lifts from Supine",
    "Bicycle Kicks",

    # Twists (Core)
    "Parivrtta Utkatasana (Revolved Chair Pose)",
    "Jathara Parivartanasana (Belly Twist)",
    "Marichyasana III (Seated Twist)",

    # Standing Core Stability
    "Virabhadrasana III (Warrior III)",
    "Ardha Chandrasana (Half Moon)",
    "Utthita Hasta Padangusthasana (Extended Hand-to-Big-Toe Pose)",

    # Inversions (Core control)
    "Pincha Mayurasana (Forearm Stand, Core focus)",
    "Adho Mukha Vrksasana (Handstand, Core variations)"
]

CORE_ALL = [("Core Poses", asana) for asana in CORE_ASANAS]

# --------------------------------------------------
# Pranayama – full list + categories
# --------------------------------------------------
PRANAYAMA_ALL = [
    # Foundations / Awareness
    "Natural Breath (natural breathing)",
    "Diaphragmatic Breathing",
    "Three-Part Breath (Dirgha Pranayama)",

    # Basic Patterns
    "Sama Vritti (equal inhale/exhale)",
    "Visama Vritti (uneven breath ratios)",
    "Ujjayi (gentle throat constriction)",
    "Box Breathing (4-4-4-4)",

    # Alternate Nostril / Nadi
    "Nadi Shodhana (without retention)",
    "Anuloma Viloma (1:4:2, with retention)",
    "Surya Bhedana (inhale right, exhale left)",
    "Chandra Bhedana (inhale left, exhale right)",

    # Cooling
    "Sitali (rolled tongue, cooling)",
    "Sitkari (through teeth, cooling)",

    # Sound / Calming
    "Bhramari (humming sound)",
    "Omkara / Pranava (OM on exhale)",

    # Activating / Cleansing
    "Kapalabhati (active exhalations)",
    "Bhastrika (bellows breath)",

    # Retentions (advanced)
    "Antara Kumbhaka (retention after inhale)",
    "Bahya Kumbhaka (retention after exhale)",
    "Kevala Kumbhaka (spontaneous breath suspension)",

    # Stepwise / Reverse Breathing
    "Viloma I (stepwise inhale)",
    "Viloma II (stepwise exhale)",
    "Pratiloma (opposing steps)",

    # Posture-specific / Somatic
    "Crocodile Breath (in prone position)",
    "Side-Lying Breath (upper side)",
    "Counted Breath (metronome / counted breath)"
]

PRANAYAMA_BY_MODE = {
    "calming": [
        "Natural Breath (natural breathing)",
        "Diaphragmatic Breathing",
        "Three-Part Breath (Dirgha Pranayama)",
        "Sama Vritti (equal inhale/exhale)",
        "Visama Vritti (uneven breath ratios)",
        "Ujjayi (gentle throat constriction)",
        "Nadi Shodhana (without retention)",
        "Chandra Bhedana (inhale left, exhale right)",
        "Bhramari (humming sound)",
        "Omkara / Pranava (OM on exhale)",
        "Viloma I (stepwise inhale)",
        "Viloma II (stepwise exhale)",
        "Crocodile Breath (in prone position)",
        "Side-Lying Breath (upper side)",
        "Counted Breath (metronome / counted breath)"
    ],

    "activating": [
        "Surya Bhedana (inhale right, exhale left)",
        "Kapalabhati (active exhalations)",
        "Bhastrika (bellows breath)",
        "Antara Kumbhaka (retention after inhale)",
        "Bahya Kumbhaka (retention after exhale)",
        "Pratiloma (opposing steps)"
    ],

    "cooling": [
        "Sitali (rolled tongue, cooling)",
        "Sitkari (through teeth, cooling)",
        "Chandra Bhedana (inhale left, exhale right)",
        "Bhramari (humming sound)"
    ],

    "neutral": [
        "Ujjayi (gentle throat constriction)",
        "Sama Vritti (equal inhale/exhale)",
        "Visama Vritti (uneven breath ratios)",
        "Box Breathing (4-4-4-4)",
        "Nadi Shodhana (without retention)",
        "Viloma I (stepwise inhale)",
        "Viloma II (stepwise exhale)",
        "Counted Breath (metronome / counted breath)"
    ],
}

# --------------------------------------------------
# Mudra structure (complete, categorized)
# --------------------------------------------------

# Universal hand mudras (usable in pranayama and meditation)
MUDRAS_UNIVERSAL = [
    "Chin Mudra",
    "Jnana Mudra",
    "Dhyana Mudra",
    "Anjali Mudra",
    "Abhaya Mudra",
    "Varada Mudra",
    "Hakini Mudra",
    "Shuni Mudra",
    "Prana Mudra",
    "Adi Mudra",
    "Brahma Mudra",
]

# Mantra-related mudras
MUDRAS_MANTRA = [
    "Chin Mudra",
    "Jnana Mudra",
    "Dhyana Mudra",
    "Anjali Mudra",
    "Hakini Mudra",
    "Kalesvara Mudra",
    "Adi Mudra",
    "Brahma Mudra",
]


# Pranayama-specific mudras (incl. bandhas)
MUDRAS_PRANAYAMA = [
    "Apan Mudra",
    "Apan Vayu Mudra",
    "Hridaya Mudra",
    "Mritsanjivani Mudra",
    "Surya / Agni Mudra",
    "Vayu Mudra",
    "Prithvi Mudra",
    "Varun Mudra",
    "Akash Mudra",
    "Linga Mudra",
    "Bhudi Mudra",
    "Jalandhara Bandha",
    "Uddiyana Bandha",
    "Mula Bandha",
    "Maha Bandha",
]

# Meditation-specific mudras
MUDRAS_MEDITATION = [
    "Shambhavi Mudra",
    "Nasikagra Drishti",
    "Khechari Mudra",
    "Yoni Mudra (Sensory Withdrawal)",
    "Maha Mudra",
    "Maha Vedha Mudra",
    "Maha Bheda Mudra",
    "Kalesvara Mudra",
]

# Symbolic / therapeutic mudras
MUDRAS_SYMBOLIC = [
    "Garuda Mudra",
    "Matsya Mudra",
    "Ksepana Mudra",
    "Padma Mudra",
    "Kamal Mudra",
    "Yoni Mudra (Hand Triangle)",
]

# --------------------------------------------------
# Mudra short descriptions
# --------------------------------------------------

MUDRAS_INFO = {
    # Universal mudras
    "Chin Mudra": "Thumb and index fingertips touch, remaining fingers extended.",
    "Jnana Mudra": "Like Chin Mudra, hands resting on the thighs, palms facing upward.",
    "Dhyana Mudra": "Both hands rest in the lap, right hand placed on the left, thumb tips touching.",
    "Anjali Mudra": "Palms placed together in front of the chest or forehead.",
    "Abhaya Mudra": "Right palm facing forward, fingers upright at shoulder height.",
    "Varada Mudra": "Palm facing forward and downward, fingers slightly open.",
    "Hakini Mudra": "Fingertips of both hands touching, hands forming a dome shape.",
    "Shuni Mudra": "Thumb and middle finger touch, other fingers extended.",
    "Prana Mudra": "Thumb touches ring finger and little finger, other fingers extended.",
    "Adi Mudra": "Thumb enclosed inside the fist, back of the hand facing upward.",
    "Brahma Mudra": "Both fists with thumbs inside, pressed together in front of the solar plexus.",

    # Mantra-related mudras
    "Kalesvara Mudra": "Fingers form a heart shape, thumbs touching the sternum.",

    # Pranayama-specific mudras (incl. bandhas)
    "Apan Mudra": "Thumb touches middle and ring fingers, other fingers extended.",
    "Apan Vayu Mudra": "Thumb, middle finger, and ring finger touch, index finger folded inward.",
    "Hridaya Mudra": "Index and middle finger touch the thumb tip, ring finger placed at the base of the thumb.",
    "Mritsanjivani Mudra": "Variation of the heart mudra, with the index finger folded inward.",
    "Surya / Agni Mudra": "Ring finger placed at the base of the thumb, thumb presses downward.",
    "Vayu Mudra": "Index finger pressed to the base of the thumb, thumb pressing onto it.",
    "Prithvi Mudra": "Thumb and ring finger touch, other fingers extended.",
    "Varun Mudra": "Thumb and little finger touch, other fingers extended.",
    "Akash Mudra": "Thumb and middle finger touch, other fingers extended.",
    "Linga Mudra": "Fingers interlaced, right thumb pointing upward.",
    "Bhudi Mudra": "Thumb and little finger touch, other fingers extended.",
    "Jalandhara Bandha": "Chin drawn to the chest, neck long, chest lifted.",
    "Uddiyana Bandha": "Abdomen drawn inward and upward, held after the exhalation.",
    "Mula Bandha": "Pelvic floor drawn inward and upward (internal, invisible action).",
    "Maha Bandha": "All three bandhas applied simultaneously (chin, abdomen, pelvic floor).",

    # Meditation-specific mudras
    "Shambhavi Mudra": "Gaze directed toward the point between the eyebrows.",
    "Nasikagra Drishti": "Gaze directed toward the tip of the nose.",
    "Khechari Mudra": "Tongue drawn back and upward toward the soft palate or throat.",
    "Yoni Mudra (Sensory Withdrawal)": "Fingers close the eyes, ears, nostrils, and lips.",
    "Maha Mudra": "One leg extended, forward bend, hands on the foot, breath retained with bandhas.",
    "Maha Vedha Mudra": "In lotus pose, slight lifting and lowering using the bandhas.",
    "Maha Bheda Mudra": "In lotus pose, deep breath retention, directing energy upward.",

    # Symbolic / therapeutic mudras
    "Garuda Mudra": "Hands crossed, thumbs hooked, fingers spread like wings.",
    "Matsya Mudra": "Hands interlaced, thumbs extended like a fish’s mouth.",
    "Ksepana Mudra": "Fingers interlaced, index fingers pointing downward.",
    "Padma Mudra": "Palms touching at the base of the thumbs, fingers spread like a lotus blossom.",
    "Kamal Mudra": "Lotus variation – fingers spread, palms connected only at the base.",
    "Yoni Mudra (Hand Triangle)": "Hands form a triangle, thumbs at the bottom, index fingers at the top.",
}

# --------------------------------------------------
# Intentions for symbolic mudras
# --------------------------------------------------

MUDRAS_INTENTION = {
    "Garuda Mudra": "Maintain spaciousness and protection",
    "Ksepana Mudra": "Release what is old",
    "Padma Mudra": "Let calmness grow from the center",
    "Yoni Mudra (Hand Triangle)": "Withdraw and gather new strength",
    "Matsya Mudra": "Stay in the flow",
    "Kamal Mudra": "Open with softness",
}

# --------------------------------------------------
# Combined mudra lists
# --------------------------------------------------

MUDRAS_ALL = MUDRAS_UNIVERSAL + MUDRAS_PRANAYAMA + MUDRAS_MEDITATION + MUDRAS_SYMBOLIC

MUDRAS_BY_CONTEXT = {
    "mantra": MUDRAS_MANTRA,
    "pranayama": MUDRAS_UNIVERSAL + MUDRAS_PRANAYAMA,
    "meditation": MUDRAS_UNIVERSAL + MUDRAS_MEDITATION,
    "symbolic": MUDRAS_SYMBOLIC,
    "all": MUDRAS_ALL,
}
