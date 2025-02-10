# All about recursion
# Loops are great, but sometimes you need to just recurse!
import os
from typing import List, Tuple

def factorial(n):
    # NOTE: the book I was using uses 'if n == 0: return 1', but this is an
    # unnecessary call imo because you can just return at 'n = 1' since the
    # factorial "space" doesn't extend to 0
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


def draw_interval(central_length: int) -> str:
    # Interval consists of a central tick with length "central_length" bounded
    # by two other intervals each with length "central_length - 1"
    # "central_length" = 1 is the base case where we just draw a tick
    # It's sort of like doing a bisector and seeing the self-symmetry emerge
    interval = ""
    if central_length == 1:
        return "-"
    else:
        interval += draw_interval(central_length - 1)
        interval += "\n"
        interval += f"{'-' * central_length}\n"
        interval += draw_interval(central_length - 1)
        return interval

def draw_english_ruler(num_inches: int, major_length: int):
    # Draws a ruler (to file)
    ruler = ""
    ruler_file = "../out/english_ruler.txt"
    # 0 line
    ruler += f"{'-'*major_length}" + " 0\n"

    for i in range(num_inches):
        ruler += draw_interval(major_length-1) + "\n"
        ruler += f"{'-' * major_length}" + f" {i+1}\n"

    with open(ruler_file, "w", encoding="utf-8") as outfile:
        outfile.write(ruler)

def has_any_prefix(path: str, prefixes: List) -> bool:
    # Check if the 'path' starts with any prefix in 'prefixes'
    for prefix in prefixes:
        if path.startswith(prefix):
            return True
    return False

def bytes_to_human_readable(size: int) -> str:
    # Convert into human-readable format based on 10^3's
    chunk_size = 1024
    # Figure out "order of magnitude"
    units = ["B", "K", "M", "G", "T", "P", "E", "Z", "Y"]
    i = (size.bit_length() - 1) // 10
    value = size / (chunk_size**i)

    return f"{value:.2f}{units[i]}"

def disk_usage(path: str, skip_prefixes=[]) -> Tuple[str, int]:
    # Figuring out paths and file sizes in a directory (hierarchical structure)
    # is a classic recursion task
    # Given a 'path' to a directory, find the cumulative disk space used by
    # that entry and nested entries
    usage_str = ""
    total = 0
    filesize = os.path.getsize(path)
    usage_str += f"{bytes_to_human_readable(filesize)}\t{path}\n".lstrip()
    if not os.path.isdir(path):
        # avoid directory metadata (4 kb each time)
        total += filesize

    # Recurse over directories
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if not has_any_prefix(filename, skip_prefixes):
                child_str, child_size = disk_usage(f"{path}/{filename}",
                                                   skip_prefixes=skip_prefixes)
                usage_str += child_str
                total += child_size

    return usage_str, total


def main():
    # Factorial
    # factorial_test_cases = [2, 3, 5, 10, 16]
    # for tc in factorial_test_cases:
    #     print(f"{tc}! = {factorial(tc)}")

    # English ruler (writes to '../out/english_ruler.txt')
    # draw_english_ruler(3, 4)

    # Disk usage with this project directory
    path = "/home/sad/dev/dsa"
    disk_usage_str, total_filesize = disk_usage(path, skip_prefixes=['.'])
    with open("../out/disk_usage.txt", "w", encoding="utf-8") as outfile:
        outfile.write(disk_usage_str)
        outfile.write(f"Total size: {bytes_to_human_readable(total_filesize)}\n")
    pass

if __name__ == "__main__":
    main()

