# 1. Create a list
numbers = [10, 20, 30, 40, 50]

# 2. Access elements
print(numbers[0])    # 10
print(numbers[-1])   # 50

# 3. Add an element
numbers.append(60)
print(numbers)

# 4. Insert an element at a specific position
numbers.insert(2, 25)
print(numbers)

# 5. Remove an element
numbers.remove(25)
print(numbers)

# 6. Remove an element using its index
numbers.pop(2)
print(numbers)

# 7. Change an element
numbers[0] = 100
print(numbers)

# 8. Find the length
print(len(numbers))

# 9. Sort the list
numbers.sort()
print(numbers)

# 10. Reverse the list
numbers.reverse()
print(numbers)

# 11. Check whether an element exists
if 30 in numbers:
    print("30 is present")

# 12. Slicing
print(numbers[1:4])   # Elements from index 1 to 3

# 13. Loop through a list
for n in numbers:
    print(n)

# 14. Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result)

# 15. Clear the list
numbers.clear()
print(numbers)
