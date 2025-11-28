from generators.mudras import MudraGenerator
from generators.pranayama import PranayamaGenerator
from generators.backblock import BackBlockGenerator
from generators.coreblock import CoreBlockGenerator
from generators.session_builder import SessionBuilder
from output.printer import YogaPrinter
import argparse


def main():
    # --- Initialization ---
    mudra_gen = MudraGenerator()
    prana_gen = PranayamaGenerator()
    back_gen = BackBlockGenerator()
    core_gen = CoreBlockGenerator()
    session = SessionBuilder(back_gen, core_gen, prana_gen)

    # --- Argument Parser ---
    ap = argparse.ArgumentParser(
        description="Yoga session with complete book structure."
    )

    ap.add_argument("--count", type=int, default=2)
    ap.add_argument("--focus",
                    choices=["none", "Strength", "Core", "Balance", "Stretch"],
                    default="none")
    ap.add_argument("--core-min", type=int, default=3)
    ap.add_argument("--core-max", type=int, default=5)
    ap.add_argument("--prana-mode",
                    choices=["any", "calming", "activating", "cooling", "neutral"],
                    default="any")
    ap.add_argument("--prana-min", type=int, default=2)
    ap.add_argument("--prana-max", type=int, default=4)
    ap.add_argument("--back-min", type=int, default=2)
    ap.add_argument("--back-max", type=int, default=3)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--colors", choices=["on", "off"], default="off")

    # --- NOW parse ---
    args = ap.parse_args()

    # --- NOW we can create printer ---
    printer = YogaPrinter(use_colors=(args.colors == "on"))

    # --- Mudra selection ---
    mantra_mudra, prana_mudra, symbolic_mudra, medit_mudra = \
        mudra_gen.generate_mudras(args.seed)

    printer.print_mantra_mudra(mantra_mudra)

    # --- Pranayama block ---
    pranayamas = prana_gen.generate_pranayama_block(
        args.prana_mode, args.prana_min, args.prana_max, args.seed
    )
    printer.print_pranayama_with_mudra(pranayamas, prana_mudra)

    # --- Session generation ---
    rows = session.generate_session(
        args.count,
        args.back_min,
        args.back_max,
        args.core_min,
        args.core_max,
        args.seed,
        args.focus
    )

    printer.print_table(rows)

    # --- Symbolic Mudra (closing) ---
    printer.print_symbolic_mudra(symbolic_mudra)

    # --- Meditation Mudra ---
    printer.print_meditation_mudra(medit_mudra)


if __name__ == "__main__":
    main()
