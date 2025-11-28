from data.yoga_data import MUDRAS_BY_CONTEXT, MUDRAS_INFO, MUDRAS_INTENTION
import random

class MudraGenerator:

    def generate_mudras(self, seed: int | None = None):
        """
        Generate four distinct mudras for a session:

        1) mantra_mudra:
            Selected from MUDRAS_MANTRA.
        2) prana_mudra:
            Selected from the combined pool of universal + pranayama mudras,
            ensuring it does not duplicate the mantra mudra.
        3) symbolic_mudra:
            Selected from symbolic/intention mudras,
            ensuring no duplication with mantra or prana mudra.
        4) medit_mudra:
            Selected from the combined pool of universal + meditation mudras,
            ensuring no duplication with any previously chosen mudra.

        Parameters
        ----------
        seed : int | None
            Optional random seed for reproducible mudra selection.

        Returns
        -------
        tuple[str, str, str, str]
            (mantra_mudra, prana_mudra, symbolic_mudra, medit_mudra)
        """

        if seed is not None:
            random.seed(seed)

        # 1) Mantra mudra
        mantra_mudra = random.choice(MUDRAS_BY_CONTEXT["mantra"])

        # 2) Pranayama mudra (cannot be the mantra mudra)
        prana_pool = [
            m for m in MUDRAS_BY_CONTEXT["pranayama"]
            if m != mantra_mudra
        ]
        prana_mudra = random.choice(prana_pool)

        # 3) Symbolic mudra (must not duplicate anything picked so far)
        symbolic_pool = [
            m for m in MUDRAS_BY_CONTEXT["symbolic"]
            if m not in (mantra_mudra, prana_mudra)
        ]
        symbolic_mudra = random.choice(symbolic_pool)

        # 4) Meditation mudra (must not duplicate anything picked so far)
        medit_pool = [
            m for m in MUDRAS_BY_CONTEXT["meditation"]
            if m not in (mantra_mudra, prana_mudra, symbolic_mudra)
        ]
        medit_mudra = random.choice(medit_pool)

        return mantra_mudra, prana_mudra, symbolic_mudra, medit_mudra
