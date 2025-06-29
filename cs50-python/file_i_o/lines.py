import sys
import os

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("#") or stripped == "":
            continue
        count += 1

    print(count)

if __name__ == "__main__":
    main()
