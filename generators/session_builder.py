from data.yoga_data import SUBCHAPTERS, FLOW, FOCUS
import random

class SessionBuilder:
    def __init__(self, backblock, coreblock, pranayama):
        self.backblock = backblock          # instance of BackBlockGenerator
        self.coreblock = coreblock          # instance of CoreBlockGenerator
        self.pranayama = pranayama          # instance of PranayamaGenerator

    def pick_subchapters(
        self,
        chapter: str,
        k: int,
        focus: str = "none"
    ) -> list[str]:
        """
        Pick k subchapters from SUBCHAPTERS[chapter].

        Logic:
        -------
        • If focus == "none": pure random selection.
        • If a focus profile is specified:
              - Subchapters listed under FOCUS[focus][chapter] are preferred.
              - Preferred ones come first (their internal order is still random).
              - The rest follow (also randomized).
        """
        # Full chapter list from the book
        base = SUBCHAPTERS[chapter][:]

        # Basic randomization
        random.shuffle(base)

        # Apply focus preference if available
        if focus != "none" and focus in FOCUS and chapter in FOCUS[focus]:
            preferred = [u for u in FOCUS[focus][chapter] if u in base]
            random.shuffle(preferred)

            rest = [u for u in base if u not in preferred]
            pool = preferred + rest
        else:
            pool = base

        # Clamp k to valid range
        k = max(1, min(k, len(pool)))
        return pool[:k]

    def generate_session(
        self,
        count: int,
        back_min: int,
        back_max: int,
        core_min: int,
        core_max: int,
        seed: int | None = None,
        focus: str = "none"
    ):
        """
        Build a full yoga session according to FLOW.

        Logic:
        -------
        • Each FLOW section picks its subchapters using pick_subchapters().
        • After the section "Arm Strength" the generator inserts:

              1) Back Block (using BackBlockGenerator)
              2) Core Block (random selection from CORE_ASANAS)

        Parameters
        ----------
        count : int
            Number of subchapters to draw per section.
        back_min, back_max : int
            Min/max size of the back block.
        core_min, core_max : int
            Min/max number of core asanas.
        seed : int | None
            Random seed for reproducibility.
        focus : str
            Focus profile name.

        Returns
        -------
        list[tuple[str, str, list[str]]]
            List of rows (section_name, chapter_name, items).
        """

        if seed is not None:
            random.seed(seed)

        rows = []

        for section, chapter in FLOW:

            # Insert Back Block + Core Block after Arm Strength section
            if section == "Arm Strength":
                # --- normal Arm Strength section ---
                subchapters = self.pick_subchapters(chapter, count, focus)
                rows.append((section, chapter, subchapters))

                # --- Back Block ---
                used_items = [
                    u
                    for _, _, ulist in rows
                    for u in ulist
                ]
                back_rows = self.backblock.generate_backblock(
                    back_min, back_max, used_items, seed
                )
                rows.append(("Back Block", "Back Focus", back_rows))

                # --- Core Block ---
                core_rows = self.coreblock.generate_coreblock(
                    core_min, core_max, used_items, seed
                )
                rows.append(("Core Block", "Core Focus", core_rows))

                continue

            # Standard sections
            subchapters = self.pick_subchapters(chapter, count, focus)
            rows.append((section, chapter, subchapters))

        return rows
