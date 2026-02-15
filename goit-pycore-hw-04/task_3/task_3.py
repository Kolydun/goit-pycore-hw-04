import sys
from pathlib import Path

from colorama import init, Fore

init(autoreset=True)


def print_tree(path: Path, indent: int = 0) -> None:
    if indent == 0:
        dir_name = path.name + "/" if path.name else str(path) + "/"
        print(Fore.CYAN + dir_name)

    try:
        entries = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        return

    for entry in entries:
        prefix = "  " * (indent + 1)
        if entry.is_dir():
            print(Fore.CYAN + prefix + entry.name + "/")
            print_tree(entry, indent + 1)
        else:
            print(Fore.GREEN + prefix + entry.name)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python task_3.py <path_to_directory>")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Error: Path does not exist: {path}")
        sys.exit(1)
    if not path.is_dir():
        print(f"Error: Path is not a directory: {path}")
        sys.exit(1)

    print_tree(path)


if __name__ == "__main__":
    main()
