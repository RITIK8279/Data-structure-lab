arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

value = int(input("Enter value to insert: "))
index = int(input("Enter index: "))

if 0 <= index <= len(arr):
    arr.insert(index, value)
    print("After Insertion:", arr)
else:
    print("Invalid index")

index = int(input("Enter index to delete: "))

if 0 <= index < len(arr):
    arr.pop(index)
    print("After Deletion:", arr)
else:
    print("Invalid index")

value = int(input("Enter value to search: "))

if value in arr:
    print("Found at index:", arr.index(value))
else:
    print("Value not found")
