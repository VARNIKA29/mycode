# Count and Sum of the array 
def count_and_sum_duplicates(arr):
    element_count = {}
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    duplicate_elements = {k: v for k, v in element_count.items() if v > 1}

    for element, count in duplicate_elements.items():
        print(f"Element {element} is a duplicate {count - 1} times")
        print(f"Sum of duplicates for element {element}: {element * (count - 1)}")

    total_duplicate_count = sum(duplicate_elements.values()) - len(duplicate_elements)
    total_duplicate_sum = sum([k * (v - 1) for k, v in duplicate_elements.items()])

    print(f"\nTotal number of duplicate elements: {total_duplicate_count}")
    print(f"Total sum of duplicate elements: {total_duplicate_sum}")

# Example usage:
array = [1, 2, 3, 2, 4, 5, 3, 6, 2, 7, 3, 8, 3, 9]
count_and_sum_duplicates(array)
