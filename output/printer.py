from data.yoga_data import MUDRAS_INFO, MUDRAS_INTENTION

# ──────────────────────────────────────────────────────────────
# ANSI COLORS (very subtle)
# ──────────────────────────────────────────────────────────────
C_RESET = "\033[0m"
C_H1    = "\033[38;5;71m"   # light evergreen (soft, not neon)
C_H2    = "\033[38;5;65m"   # muted sage green
C_H3    = "\033[38;5;240m"  # soft grey-green

class YogaPrinter:
    def __init__(self, use_colors=False):
        self.use_colors = use_colors

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #  INTERNAL HELPERS FOR HEADERS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    def _h1(self, title: str):
        bar = "═" * (len(title) + 8)

        if self.use_colors:
            print(f"\n{C_H1}══ {title.upper()} ══{C_RESET}")
            print(f"{C_H1}{bar}{C_RESET}\n")
        else:
            print(f"\n══ {title.upper()} ══")
            print(f"{bar}\n")

    def _h2(self, title: str):
        bar = "━" * (len(title) + 8)

        if self.use_colors:
            print(f"\n{C_H2}━━ {title.upper()} ━━{C_RESET}")
            print(f"{C_H2}{bar}{C_RESET}")
        else:
            print(f"\n━━ {title.upper()} ━━")
            print(bar)

    def _h3(self, title: str):
        bar = "─" * 48

        if self.use_colors:
            print(f"\n{C_H3}{title}{C_RESET}")
            print(f"{C_H3}{bar}{C_RESET}")
        else:
            print(f"\n{title}")
            print(bar)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #  MUDRA SECTIONS (LEVEL 2)
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    def print_mantra_mudra(self, mudra: str, colw=(26, 20, 90)):
        self._h2("Mantra Mudra")
        desc = MUDRAS_INFO.get(mudra, "")
        print(f"{'Mantra':<{colw[0]}} | {'Mudra':<{colw[1]}} | {mudra} ({desc})")

    def print_pranayama_with_mudra(self, pranayamas, mudra: str, colw=(26, 20, 90)):
        self._h2("Pranayama")
        for item in pranayamas:
            print(f"{'Breathwork':<{colw[0]}} | {'Pranayama':<{colw[1]}} | {item}")

        desc = MUDRAS_INFO.get(mudra, "")
        print(f"{'Breathwork':<{colw[0]}} | {'Mudra':<{colw[1]}} | {mudra} ({desc})")

    def print_symbolic_mudra(self, mudra: str, colw=(26, 20, 90)):
        self._h2("Symbolic Mudra")
        desc    = MUDRAS_INFO.get(mudra, "")
        intent  = MUDRAS_INTENTION.get(mudra, "")
        print(f"{'Closing':<{colw[0]}} | {'Mudra':<{colw[1]}} | {mudra} ({desc})")
        if intent:
            print(f"{'':<{colw[0]}} | {'Intention':<{colw[1]}} | {intent}")

    def print_meditation_mudra(self, mudra: str, colw=(26, 20, 90)):
        self._h2("Meditation Mudra")
        desc = MUDRAS_INFO.get(mudra, "")
        print(f"{'Meditation':<{colw[0]}} | {'Mudra':<{colw[1]}} | {mudra} ({desc})\n")

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #  MAIN SESSION STRUCTURE
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    def print_table(self, rows):
        colw = (30, 20, 90)
        total = sum(colw) + 3 + 12
        thin_line = "─" * total

        # LEVEL 1 HEADER
        self._h1("Yoga Session")

        # Table header
        print(f"{'Section':<{colw[0]}} | {'Chapter':<{colw[1]}} | Content")
        print(thin_line)

        for section, chapter, content in rows:

            # LEVEL 3 HEADERS
            if section == "Back Block":
                self._h3("Back Block")
                for chap, item in content:
                    print(f"{'Back Poses':<{colw[0]}} | {chap:<{colw[1]}} | {item}")
                continue

            if section == "Core Block":
                self._h3("Core Block")
                for item in content:
                    print(f"{'Core Poses':<{colw[0]}} | {'Core Focus':<{colw[1]}} | {item}")
                print()
                continue

            # Standard rows
            items = ", ".join(content)
            print(f"{section:<{colw[0]}} | {chapter:<{colw[1]}} | {items}")

        print(thin_line)
