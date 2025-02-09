# All about recursion
# Loops are great, but sometimes you need to just recurse!

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

def main():
    # Factorial
    # factorial_test_cases = [2, 3, 5, 10, 16]
    # for tc in factorial_test_cases:
    #     print(f"{tc}! = {factorial(tc)}")

    # English ruler (writes to '../out/english_ruler.txt')
    draw_english_ruler(3, 4)
    pass

if __name__ == "__main__":
    main()

