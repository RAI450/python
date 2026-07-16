# ==========================================================
# UTILS
# Small shared helper functions used across the whole game.
# Keeping them here avoids repeating the same formatting
# code in every file (removes duplicate code).
# ==========================================================


def press_enter():
    """Pause the game until the player presses Enter."""
    input("\nPress Enter to continue...")


def print_header(title, width=60, symbol="="):
    """Print a centered title inside a line of symbols.

    Used everywhere a screen needs a big title bar, so every
    menu / room / puzzle screen shares the exact same look.
    """
    print(f"\n{symbol * width}")
    print(title.upper().center(width))
    print(f"{symbol * width}\n")


def print_divider(width=60, symbol="-"):
    """Print a plain divider line, used to separate sections."""
    print(symbol * width)


def get_int_choice(prompt, min_value=None, max_value=None):
    """Ask the player for a whole number and keep asking until
    they give a valid one.

    This replaces the unsafe pattern of calling int(input(...))
    directly, which used to crash the whole game if the player
    typed a letter instead of a number.
    """
    while True:
        raw_choice = input(prompt).strip()

        try:
            value = int(raw_choice)
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue

        if min_value is not None and value < min_value:
            print(f"Please enter a number between {min_value} and {max_value}.\n")
            continue

        if max_value is not None and value > max_value:
            print(f"Please enter a number between {min_value} and {max_value}.\n")
            continue

        return value


def progress_bar(current, total, width=20):
    """Return a simple text progress bar, e.g. [######----] 60%."""
    if total <= 0:
        return "[--------------------] 0%"

    filled = int(width * current / total)
    filled = max(0, min(width, filled))
    percent = int((current / total) * 100)

    return f"[{'#' * filled}{'-' * (width - filled)}] {percent}%"
