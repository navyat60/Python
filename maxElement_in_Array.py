def find_max_element(arr):
    if not arr:
        return None
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element
array = [1, 2, 3, 4, 5]
max_element = find_max_element(array)

print("Array:", array)
print("Maximum element:", max_element)
