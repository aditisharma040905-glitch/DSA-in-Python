# Day 1 - Big O Notation Examples

# O(1) - Constant Time
def get_first_element(arr):
    # Accessing by index doesn't depend on array size
    return arr[0] if arr else None

# O(n) - Linear Time
def print_all_elements(arr):
    # Visits each element once
    for element in arr:
        print(element)

# O(n^2) - Quadratic Time
def print_pairs(arr):
    # Nested loop over the same list
    for i in arr:
        for j in arr:
            print(i, j)

if __name__ == "__main__":
    nums = [1, 2, 3]
    print("First element:", get_first_element(nums))
    print("All elements:")
    print_all_elements(nums)
    print("All pairs:")
    print_pairs(nums)
