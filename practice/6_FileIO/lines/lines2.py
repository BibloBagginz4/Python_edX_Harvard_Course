import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Error: One file name expected in command-line")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Error: Not a (.py) file")

    try:
        with open(filename, encoding="utf-8") as file:
            count = 0
            for line in file:
                stripped = line.strip()

                if not stripped:
                    continue

                if stripped.startswith("#"):
                    continue

                count += 1

    except FileNotFoundError:
        sys.exit("Error: File was not found.")

    print(count)


if __name__ == "__main__":
    main()
