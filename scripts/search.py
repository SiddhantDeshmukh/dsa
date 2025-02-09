# Search algorithms
import time
import random
from typing import List


def book_binary_search(data, target, low, high):
    if low > high:
        return False
    
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return book_binary_search(data, target, low, mid - 1)
        else:
            return book_binary_search(data, target, mid + 1, high)


def binary_search(seq: List, val, low: int, high: int, num_iter: int):
    # Classic search algorithm that bisects 'seq' each time
    # If there are 'n' elements in 'seq', we are guaranteed to find the target
    # 'val' in 2^n + 1 iterations
    # In this implementation, we are cutting the search list in half each time
    # Time complexity: O(log n)
    # NOTE: Only works if 'seq' is sorted!
    num_iter += 1
    
    if val < seq[0] or val > seq[len(seq) - 1]:
        # Outside range, return 'None'
        return None, num_iter

    if low > high:
        # Not found, return 'None'
        return None, num_iter
    else:
        mid = (low + high) // 2
        if seq[mid] == val:  # Base: we found the value
            return mid, num_iter
        elif val < seq[mid]:
            # Look below
            return binary_search(seq, val, low, mid-1, num_iter)
        else:
            # Look above
            return binary_search(seq, val, mid+1, high, num_iter)

def test_binary_search(n_test = 10):
    test_log = ""
    num_success = 0
    total_time = 0
    ranges = [10, 100, 1000, 10_000, 100_000, 1_000_000, 10_000_000]
    with open("../out/binary_search_log.txt", "w") as outfile:
        outfile.write(f"{n_test} tests\n")

    for i in range(n_test):
        test_log += f"\nTest {i+1}\n------------\n"
        # Generate a random sequence and a random value (may be outside)
        range_lim = random.choice(ranges)
        low = random.randint(-range_lim, range_lim)
        high = random.randint(low+1, low + 2*range_lim)
        seq = list(range(low, high+1))
        # There is a small chance the value will be outside the sequence
        if i % 5 == 0:
            # Every 5th test, make the target one of the ends
            val = random.choice([low, high])
        else:
            val = random.randint(low - int(0.01*range_lim), high + int(0.01*range_lim))
        test_log += f"Sequence: [{low}, {high}]\n"
        test_log += f"Search value = {val}\n"

        if i > (n_test - 3):
            # For last few tests, remove the val from the sequence
            test_log += "Search value will be omitted from sequence in this test\n"
            if val in seq:
                seq.remove(val)
        
        test_start_time = time.time()
        val_idx, num_iter = binary_search(seq, val, 0, len(seq)-1, 0)
        if val_idx != None:
            assert seq[val_idx] == val
            num_success += 1
            test_log += f"Target value '{val}' found at index '{val_idx}'" +\
                f" in {num_iter} iterations in {len(seq)}-length sequence.\n"
        else:
            test_log += f"Error: {val} not found in sequence after " +\
                f"{num_iter} iterations!\n"

        test_time = time.time() - test_start_time
        total_time += test_time
        test_log += f"Time elapsed: {test_time:.2e} [s]\n"
        test_log += f"Mean time per iter: {test_time/num_iter:.2e} [s / iter]\n"

    test_log += f"\nFinal results: {num_success} successes in {n_test} trials.\n"
    test_log += f"Total time elapsed: {total_time:.2e}\n"
    with open("../out/binary_search_log.txt", "a") as outfile:
        outfile.write(test_log)

def main():
    test_binary_search(n_test = 100)
    seq = list(range(-3894, 6346))
    target = -3894
    print(book_binary_search(seq, target, 0, len(seq) - 1))
    print(binary_search(seq, target, 0, len(seq) - 1, 0))
    print(binary_search(seq, target, 0, len(seq) - 1, 0))


if __name__ == "__main__":
    main()
