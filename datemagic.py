"""Opret en ISO-formateret mappe for hver dag i den aktuelle måned."""

from calendar import monthrange
from datetime import date
from pathlib import Path


def ask_target_directory() -> Path:
    """Spørg efter en eksisterende mappe; brug den aktuelle mappe som standard."""
    default = Path.cwd()
    while True:
        answer = input(f"Målmappe [{default}]: ").strip()
        target = Path(answer or default).expanduser()
        if target.exists() and target.is_dir():
            return target
        print(f"'{target}' findes ikke eller er ikke en mappe. Prøv igen.")


def ask_format() -> str:
    """Lad brugeren vælge det eneste understøttede navneformat."""
    print("\nDatoformat:")
    print("1) YYYY-MM-DD (ISO 8601)")
    while True:
        choice = input("Vælg format [1]: ").strip() or "1"
        if choice == "1":
            return "%Y-%m-%d"
        print("Vælg 1: YYYY-MM-DD.")


def ask_confirmation() -> bool:
    """Kræv en tydelig bekræftelse, før mapperne oprettes."""
    while True:
        answer = input("\nOpret disse mapper? [j/nej]: ").strip().lower()
        if answer in {"j", "ja", "y", "yes"}:
            return True
        if answer in {"", "n", "nej", "no"}:
            return False
        print("Svar ja eller nej.")


def main() -> None:
    """Vis og opret mapper for hver dag i den aktuelle lokale måned."""
    target = ask_target_directory()
    date_format = ask_format()
    today = date.today()
    days_in_month = monthrange(today.year, today.month)[1]
    month_names = (
        "januar", "februar", "marts", "april", "maj", "juni",
        "juli", "august", "september", "oktober", "november", "december",
    )
    folder_names = [
        date(today.year, today.month, day).strftime(date_format)
        for day in range(1, days_in_month + 1)
    ]

    print(f"\nAktuel måned: {month_names[today.month - 1]} {today.year}")
    print(f"Målmappe: {target}")
    print("Planlagte mapper:")
    for name in folder_names:
        print(f"  {name}")

    if not ask_confirmation():
        print("Der blev ikke oprettet nogen mapper.")
        return

    created = 0
    skipped = 0
    for name in folder_names:
        folder = target / name
        if folder.exists():
            skipped += 1
            continue
        try:
            folder.mkdir()
        except FileExistsError:
            # Another process may have created it after the existence check.
            skipped += 1
        else:
            created += 1

    print(f"\nOprettet: {created}")
    print(f"Sprunget over: {skipped}")


if __name__ == "__main__":
    main()
