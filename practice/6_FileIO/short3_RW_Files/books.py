import csv


def main():
    with open("alice.txt", "r", encoding="utf-8") as f:
        contents = f.readlines()

    chapter1 = contents[31:250]
    with open("chapter1.txt", "w", encoding="utf-8", newline="") as f:
        f.writelines(chapter1)


if __name__ == "__main__":
    main()
