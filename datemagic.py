"""Create one ISO-formatted folder for every day in the current month."""

from calendar import monthrange
from datetime import date
from pathlib import Path


def ask_target_directory() -> Path:
    """Ask for an existing directory, defaulting to the current directory."""
    default = Path.cwd()
    while True:
        answer = input(f"Target directory [{default}]: ").strip()
        target = Path(answer or default).expanduser()
        if target.exists() and target.is_dir():
            return target
        print(f"'{target}' does not exist or is not a directory. Please try again.")


def ask_format() -> str:
    """Ask the user to select the only supported naming format."""
    print("\nDate naming format:")
    print("1) YYYY-MM-DD (ISO 8601)")
    while True:
        choice = input("Choose a format [1]: ").strip() or "1"
        if choice == "1":
            return "%Y-%m-%d"
        print("Please choose 1: YYYY-MM-DD.")


def ask_confirmation() -> bool:
    """Require an explicit yes before creating folders."""
    while True:
        answer = input("\nCreate these folders? [y/N]: ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"", "n", "no"}:
            return False
        print("Please answer yes or no.")


def main() -> None:
    """Preview and create folders for every day in the current local month."""
    target = ask_target_directory()
    date_format = ask_format()
    today = date.today()
    days_in_month = monthrange(today.year, today.month)[1]
    folder_names = [
        date(today.year, today.month, day).strftime(date_format)
        for day in range(1, days_in_month + 1)
    ]

    print(f"\nCurrent month: {today.strftime('%B %Y')}")
    print(f"Target: {target}")
    print("Planned folders:")
    for name in folder_names:
        print(f"  {name}")

    if not ask_confirmation():
        print("No folders were created.")
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

    print(f"\nCreated: {created}")
    print(f"Skipped: {skipped}")


if __name__ == "__main__":
    main()
