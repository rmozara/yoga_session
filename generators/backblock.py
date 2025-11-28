from data.yoga_data import BACK_ALL
import random

class BackBlockGenerator:

    def generate_backblock(
        self,
        back_min: int,
        back_max: int,
        used: list[str],
        seed: int | None = None
    ):
        """
        Generate a Back Block consisting of a mix of subchapters and explicit
        back-focused asanas. Ensures no duplicates with the 'used' list.

        Parameters
        ----------
        back_min : int
            Minimum number of items to draw.
        back_max : int
            Maximum number of items to draw.
        used : list[str]
            A list of already-used items (strings only), to avoid duplicates.
        seed : int | None
            Optional random seed for reproducibility.

        Returns
        -------
        list[tuple[str, str]]
            A list of (chapter, item) tuples drawn from BACK_ALL.
        """
        if seed is not None:
            random.seed(seed)

        # Filter out already-used items
        candidates = [
            (chapter, item)
            for (chapter, item) in BACK_ALL
            if item not in used
        ]

        # If everything is used up, allow fallback to the full list
        if not candidates:
            candidates = BACK_ALL[:]

        # Determine how many items to draw
        if back_min == back_max:
            k = back_min
        else:
            k = random.randint(back_min, back_max)

        # Ensure k is within valid limits
        k = max(1, min(k, len(candidates)))

        # Randomize selection
        random.shuffle(candidates)

        return candidates[:k]
