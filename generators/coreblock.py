from data.yoga_data import CORE_ALL
import random

class CoreBlockGenerator:

    def generate_coreblock(self, core_min, core_max, used, seed=None):
        if seed is not None:
            random.seed(seed)

        # Base list
        core_all = CORE_ALL

        # Avoid duplicates
        candidates = [(chap, item) for (chap, item) in core_all if item not in used]

        if not candidates:
            candidates = core_all[:]  # allow fallback

        k = core_min if core_min == core_max else random.randint(core_min, core_max)
        k = max(1, min(k, len(candidates)))

        random.shuffle(candidates)
        return [item for (_, item) in candidates[:k]]
