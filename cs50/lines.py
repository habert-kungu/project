# Even so, in a file called lines.py,
import sys


def count_lines(filename):
    line_count = 0
    with open(filename, "r") as file:
        for line in file:
            strip_line = line.strip()
            if strip_line and not strip_line.startswith("#"):
                line_count += 1
        return line_count


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many Arguments")

    if len(sys.argv) < 2:
        sys.exit("Too few Arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a python file ")
    print(f"The LOC of the file is {count_lines(filename)}")


if __name__ == "__main__":
    main()
