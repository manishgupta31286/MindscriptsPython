"""
Python Array (List) Operations Demo
Demonstrates: indexing, sorting, reverse, insert, update, pop, delete, clear, 
slicing, total, min, max, and average operations
"""

# Create a sample array
arr = [5, 2, 8, 1, 9, 3, 7]
print("Original Array:", arr)
print("\n" + "="*50)

# 1. INDEXING - Access elements by position
print("\n1. INDEXING")
print("First element (index 0):", arr[0])
print("Last element (index -1):", arr[-1])
print("Element at index 2:", arr[2])

# 2. SORTING - Arrange elements in order
print("\n2. SORTING")
arr_sorted = sorted(arr)  # Creates new sorted array
print("Sorted array (ascending):", arr_sorted)
arr_copy = arr.copy()
arr_copy.sort()  # Sorts in-place
print("Sorted in-place:", arr_copy)
arr_desc = sorted(arr, reverse=True)
print("Sorted (descending):", arr_desc)

# 3. REVERSE - Reverse the array
print("\n3. REVERSE")
arr_copy = arr.copy()
arr_copy.reverse()  # Reverse in-place
print("Reversed array:", arr_copy)
arr_reversed = arr[::-1]  # Using slicing
print("Using slicing [::-1]:", arr_reversed)

# 4. INSERT - Add element at specific position
print("\n4. INSERT")
arr_copy = arr.copy()
arr_copy.insert(2, 99)  # Insert 99 at index 2
print("After inserting 99 at index 2:", arr_copy)
arr_copy.insert(0, 100)  # Insert at beginning
print("After inserting 100 at index 0:", arr_copy)

# 5. UPDATE - Modify element at specific position
print("\n5. UPDATE")
arr_copy = arr.copy()
print("Before update:", arr_copy)
arr_copy[0] = 50  # Change first element
arr_copy[3] = 88  # Change element at index 3
print("After updating index 0 to 50 and index 3 to 88:", arr_copy)

# 6. POP - Remove and return element
print("\n6. POP")
arr_copy = arr.copy()
popped = arr_copy.pop()  # Remove last element
print("Popped last element:", popped)
print("Array after pop():", arr_copy)
popped_at_index = arr_copy.pop(1)  # Remove element at index 1
print("Popped element at index 1:", popped_at_index)
print("Array after pop(1):", arr_copy)

# 7. DELETE - Remove element by value (using remove) or by index (using del)
print("\n7. DELETE")
arr_copy = arr.copy()
arr_copy.remove(2)  # Remove first occurrence of value 2
print("After removing value 2:", arr_copy)
arr_copy = arr.copy()
del arr_copy[3]  # Delete element at index 3
print("After del arr_copy[3]:", arr_copy)
arr_copy = arr.copy()
del arr_copy[1:3]  # Delete elements from index 1 to 2
print("After del arr_copy[1:3]:", arr_copy)

# 8. CLEAR - Remove all elements
print("\n8. CLEAR")
arr_copy = arr.copy()
print("Before clear:", arr_copy)
arr_copy.clear()
print("After clear():", arr_copy)

# 9. SLICING - Extract portion of array
print("\n9. SLICING")
arr_copy = arr.copy()
print("Original array:", arr_copy)
print("arr_copy[1:4] (index 1 to 3):", arr_copy[1:4])
print("arr_copy[:3] (first 3 elements):", arr_copy[:3])
print("arr_copy[3:] (from index 3 to end):", arr_copy[3:])
print("arr_copy[::2] (every 2nd element):", arr_copy[::2])
print("arr_copy[::-1] (reversed):", arr_copy[::-1])
print("arr_copy[-3:] (last 3 elements):", arr_copy[-3:])

# 10. TOTAL - Sum of all elements
print("\n10. TOTAL (SUM)")
print("Array:", arr)
total = sum(arr)
print("Sum of all elements:", total)

# 11. MIN - Minimum value
print("\n11. MIN")
print("Array:", arr)
min_val = min(arr)
print("Minimum value:", min_val)

# 12. MAX - Maximum value
print("\n12. MAX")
print("Array:", arr)
max_val = max(arr)
print("Maximum value:", max_val)

# 13. AVERAGE - Mean of all elements
print("\n13. AVERAGE")
print("Array:", arr)
average = sum(arr) / len(arr)
print(f"Average value: {average:.2f}")

print("\n" + "="*50)
