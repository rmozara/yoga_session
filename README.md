# Yoga Session Generator

A small Python program that generates structured yoga sessions, complete with:
- Opening mantra mudra
- Pranayama block + pranayama mudra
- Full yoga session (standing, warm-up, bends, arm balance, etc.)
- Back block (back-focused asanas)
- Core block (core-focused asanas)
- Symbolic closing mudra + intention
- Meditation mudra

Output is cleanly formatted for terminals, optionally with ANSI color codes.

---

## Features

- Deterministic or random generation (via seed)
- Configurable focus profiles
- Flexible ranges for pranayama, back block, and core block
- Three-level section formatting (H1, H2, H3)
- Optional color mode (“dark forest” scheme)
- All data stored in simple Python dictionaries for easy modification

---

## Installation

Clone the repository:

    git clone https://github.com/USERNAME/yoga_session.git
    cd yoga_session

Run with Python 3:

    python3 main.py

No external dependencies are required.

---

## Running the Program

Example:

    python3 main.py \
        --count 2 \
        --focus none \
        --core-min 3 \
        --core-max 5 \
        --prana-mode any \
        --prana-min 4 \
        --prana-max 5 \
        --back-min 2 \
        --back-max 3

---

## Command Line Arguments

**--count**
Number of subchapters per standard section.
Default: 2

**--focus**
Focus profile. Options: `none`, `Strength`, `Core`, `Balance`, `Stretch`.
Default: none

**--core-min**
Minimum number of core asanas.
Default: 3

**--core-max**
Maximum number of core asanas.
Default: 5

**--prana-mode**
Category for pranayama selection (`activating`, `calming`, `cooling`, `neutral`, `any`).
Default: any

**--prana-min**
Minimum number of pranayamas.
Default: 2

**--prana-max**
Maximum number of pranayamas.
Default: 4

**--back-min**
Minimum back-focused items.
Default: 2

**--back-max**
Maximum back-focused items.
Default: 3

**--seed**
Optional integer seed for reproducibility.

**--colors**
`on` or `off`. Enables minimal ANSI color highlights.
Default: off

---

## Output Structure

The program prints the full session in this order:

1. Mantra Mudra (H2)
2. Pranayama Block + Mudra (H2)
3. Yoga Session (H1)
4. Back Block (H3)
5. Core Block (H3)
6. Symbolic Mudra (H2)
7. Meditation Mudra (H2)

Formatting hierarchy:

    H1 → Large block title (═)
    H2 → Mid-level title (━)
    H3 → Sub-section (─)

Example:

    ══ YOGA SESSION ══
    ─────────────────────
    Section | Chapter | Content
    …

---

## Color Mode (optional)

The optional color mode provides:

DF-1 = soft dim gray
DF-2 = medium cool green
DF-3 = dark forest green (section headers)
RESET = normal text

To enable:

    python3 main.py --colors on

All colors are standard ANSI escape sequences and safe for most terminals.

---

## Project Structure

main.py
    Entry point and argument parser.

data/
    yoga_data.py — all asanas, pranayama lists, mudras.

generators/
    pranayama_generator.py
    session_builder.py
    backblock.py
    coreblock.py

output/
    printer.py — ANSI formatting and hierarchical headers.

README.md
    You are reading it.

---

## Focus Profiles

The `--focus` flag controls which subchapters are preferred inside each book chapter.

Available profiles:
- **none** – pure random choice inside each chapter.
- **Strength** – prefers pose groups emphasizing strength and stability.
- **Core** – prefers entries loading the abdominal / trunk area.
- **Balance** – prefers balancing and stabilizing work.
- **Stretch** – prefers lengthening and opening poses.

Mechanism (as implemented in `FOCUS` in `data/yoga_data.py`):
- Shuffle the full chapter list.
- Move all preferred subchapters to the front (still randomized internally).
- Select `--count` from the reordered list.
- If no mapping exists for the chosen profile, purely random selection is used.

---

## How the Session Is Built

The core section order is defined in `FLOW` (in `data/yoga_data.py`):

- Arrival & Breath → Seated Poses
- Warm-up → Quadruped Poses
- Standing Sequence → Standing Poses
- Side Bends / Wide-Leg Poses → Standing Poses
- Backbend Preparation → Prone Poses
- Backbends → Backbends
- Arm Strength → Arm Balances
- Core → Core Poses
- Inversions → Inversion Poses
- Counterposes & Stretch → Seated Poses
- Relaxation → Supine Poses

For each of these standard sections, the generator:
- Looks up the corresponding chapter in `SUBCHAPTERS`.
- Uses `pick_subchapters()` to select `--count` subchapters (possibly focus-weighted).
- Stores them as `(section, chapter, [sub1, sub2, …])`.

---

## Back Block

Right after **Arm Strength**, two additional blocks are added:
- **Back Block** – from `BACK_ALL`
- **Core Block** – from `CORE_ASANAS`

Back Block composition:
- `BACK_SUBCHAPTERS`: book subchapters suitable for posterior-chain work
- `BACK_ASANAS_EXTRA`: curated single asanas (arm balances, inversions, balances, etc.)
  always tagged with `"Back Focus"`
- `BackBlockGenerator.generate_backblock()` picks `--back-min` to `--back-max` items
  and avoids duplicates when possible.

Each entry is a `(chapter, item)` tuple, where `chapter` is either a real book chapter
(e.g. `"Prone Poses"`) or the pseudo-chapter `"Back Focus"`.

---

## Core Block

The Core Block uses the list `CORE_ASANAS`.

`CoreBlockGenerator.generate_coreblock()` selects `--core-min` to `--core-max` items,
avoiding duplicates where possible.

All Core Block items appear under `"Core Poses"` with chapter `"Core Focus"`.

---

## Output Layout

The printer builds a 3-column table:

- **Section** – logical part of the class
- **Chapter** – book chapter or pseudo-chapter (`Back Focus`, `Core Focus`)
- **Content** – comma-separated list of subchapters or asanas

Mudra sections:
- Mantra Mudra – opening mudra
- Pranayama – pranayama list + pranayama mudra
- Symbolic Mudra – closing mudra + intention
- Meditation Mudra – meditation posture mudra

Mudra descriptions come from `MUDRAS_INFO`, intentions from `MUDRAS_INTENTION`.

---

## Data Source

This program uses the chapter and subchapter structure from the book **“2,100 Asanas”**.
A public reference copy is available here:

https://www.scribd.com/document/334551448/2-100-Asanas-pdf

Additional back-focused and core-focused asanas are manually curated for functional clarity.

---

## Modifying the Data

All content lists live in `data/yoga_data.py`:

- `SUBCHAPTERS` – book-based chapter → subchapter mapping
- `FLOW` – sequence of sections
- `FOCUS` – focus profile preferences
- `BACK_SUBCHAPTERS` – subchapters usable in the Back Block
- `BACK_ASANAS_EXTRA` – manually curated back-focused single asanas
- `CORE_ASANAS` – core-focused asanas
- `PRANAYAMA_ALL`, `PRANAYAMA_BY_MODE` – pranayama pools
- `MUDRAS_*`, `MUDRAS_INFO`, `MUDRAS_INTENTION` – mudra data

You can freely:
- add new asanas
- rename entries
- extend categories
- adjust which asanas count as “back-focused” or “core-focused”

The generator will automatically use the updated data on the next run.

---

## License

MIT License.

You are free to modify, extend, or embed this generator in your own yoga tools,
scripts, or teaching materials.
