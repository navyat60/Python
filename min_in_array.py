def find_min_element(arr):
    if not arr:
        return None
    min_element = arr[0]
    for element in arr:
        if element < min_element:
            min_element = element
    return min_element
array = [1, 2, 3, 4, 5]
min_element = find_min_element(array)
print("Array:", array)
print("Minimum element:", min_element)
