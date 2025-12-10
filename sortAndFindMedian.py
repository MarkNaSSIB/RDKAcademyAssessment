#!/usr/bin/env python3
"""
By Mark Boutros
Convert pseudocode into working code:

- insertion_sort(numbers): sort an array in ascending order
- sort_and_find_median(numbers): return the median value

Provides:
- Option to enter numbers manually
- Option to use predefined test arrays
"""

# Predefined test arrays to quickly demonstrate behavior
PREDEFINED_TESTS = [
    [1, 2, 3],                    # odd length, simple
    [3, 1, 4, 1, 5],              # odd length, unsorted with duplicates
    [10, -5, 0, 7],               # even length, includes negative
    [2.5, 2.0, 3.5, 4.0, 1.0],    # odd length, floats
]


def insertion_sort(numbers: list[float]) -> list[float]:
    """
    Sort the list in ascending order using insertion sort.

    Returns a new sorted list and does not modify the original list.
    Time complexity: O(n^2) in the worst case, which is fine for inputs expected here.
    """
    sorted_numbers = numbers[:]  # copy to avoid changing the input

    for i in range(1, len(sorted_numbers)):
        key = sorted_numbers[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and sorted_numbers[j] > key:
            sorted_numbers[j + 1] = sorted_numbers[j]
            j -= 1

        sorted_numbers[j + 1] = key

    return sorted_numbers


def sort_and_find_median(numbers: list[float]) -> float:
    """
    Sort the list and return its median.

    For even length n:
        median = (numbers[n/2 - 1] + numbers[n/2]) / 2
    For odd length:
        median = numbers[n//2]
    """
    if not numbers:
        raise ValueError("Cannot compute median of an empty list.")

    sorted_numbers = insertion_sort(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        # even number of elements
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2.0
    else:
        # odd number of elements
        return sorted_numbers[mid]


def read_numbers_from_user() -> list[float]:
    """
    Read numbers from a single line of user input.

    Example input:
        3 1 4 1 5
    """
    raw = input("Enter numbers separated by spaces: ")
    # allow commas too, e.g. "1, 2, 3 4"
    raw = raw.replace(",", " ")
    parts = raw.split()
    numbers: list[float] = []

    for part in parts:
        try:
            numbers.append(float(part))
        except ValueError:
            print(f"Skipping invalid value: {part!r}")

    return numbers


def run_manual_input_flow() -> None:
    """
    Ask the user to enter numbers, then show sorted list and median.
    """
    numbers = read_numbers_from_user()

    if not numbers:
        print("No valid numbers entered.")
        return

    sorted_numbers = insertion_sort(numbers)
    median = sort_and_find_median(numbers)

    print(f"\nInput numbers : {numbers}")
    print(f"Sorted numbers: {sorted_numbers}")
    print(f"Median        : {median}")

    
def run_predefined_test_case() -> None:
    """
    Let the user choose one of the predefined test arrays and show its median.
    """
    print("\nPredefined test arrays:")
    for idx, arr in enumerate(PREDEFINED_TESTS, start=1):
        print(f"  {idx}. {arr}")

    choice = input("Select a test case number (or press Enter to cancel): ").strip()
    if not choice:
        print("No test case selected.")
        return

    try:
        index = int(choice)
    except ValueError:
        print("Invalid selection.")
        return

    if not (1 <= index <= len(PREDEFINED_TESTS)):
        print("Selection out of range.")
        return

    test_array = PREDEFINED_TESTS[index - 1]
    print(f"\nSelected test array: {test_array}")

    sorted_numbers = insertion_sort(test_array)
    median = sort_and_find_median(test_array)

    print(f"Sorted numbers: {sorted_numbers}")
    print(f"Median        : {median}")


def main() -> None:

    #loop for user input
    while True:
        print("\nMedian calculator")
        print("-----------------")
        print("1. Enter numbers manually")
        print("2. Use a predefined test array")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_manual_input_flow()
        elif choice == "2":
            run_predefined_test_case()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Unknown option, please try again.")


if __name__ == "__main__":
    main()
