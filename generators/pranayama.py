from data.yoga_data import PRANAYAMA_ALL, PRANAYAMA_BY_MODE
import random

class PranayamaGenerator:

    def generate_pranayama_block(
        self,
        mode: str,
        prana_min: int,
        prana_max: int,
        seed: int | None = None
    ):
        """
        Generate a pranayama block using mixed logic:

        Logic A + B combined:
        ----------------------
        • Draw N in the interval [prana_min, prana_max].
        • One exercise is always chosen from the full list (PRANAYAMA_ALL).
        • The remaining (N - 1) are drawn from the selected mode category:
              mode = "calming", "activating", "cooling", "neutral"
          If mode = "any", remaining exercises are also drawn from PRANAYAMA_ALL.
        • No duplicates allowed.
        • Final order is shuffled.

        Parameters
        ----------
        mode : str
            Selected pranayama mode ("calming", "activating", "cooling", "neutral", or "any").
        prana_min : int
            Minimum number of pranayama techniques.
        prana_max : int
            Maximum number of pranayama techniques.
        seed : int | None
            Optional random seed for reproducibility.

        Returns
        -------
        list[str]
            A list of pranayama techniques in random order.
        """

        if seed is not None:
            random.seed(seed)

        # Determine number of items to select
        if prana_min == prana_max:
            n = prana_min
        else:
            n = random.randint(prana_min, prana_max)

        n = max(1, n)  # Ensure at least one exercise

        # 1) Always pick one pranayama from the full list
        first = random.choice(PRANAYAMA_ALL)

        # 2) Select remaining N - 1 from chosen mode (or from ALL if mode == "any")
        if mode == "any":
            pool = [x for x in PRANAYAMA_ALL if x != first]
        else:
            # Fall back to ALL if mode is unknown
            pool_base = PRANAYAMA_BY_MODE.get(mode, PRANAYAMA_ALL)
            pool = [x for x in pool_base if x != first]

        # Determine how many additional items can be drawn
        k = max(0, min(n - 1, len(pool)))

        rest = random.sample(pool, k=k)

        # Combine and shuffle final result
        picks = [first] + rest
        random.shuffle(picks)

        return picks
