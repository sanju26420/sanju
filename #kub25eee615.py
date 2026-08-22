#kub25eee615
#d r sanjay
#22/08/26


nums = [3, 10, 15, 75, 25, 23]

found = False

for num in nums:
    if num % 3 == 0 or num % 5 == 0 or num % 8 == 0:
        print(num)
        found = True

if not found:
    print("none")
    
    
nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

smallest = min(nums)
largest = max(nums)

small_index = nums.index(smallest)
large_index = nums.index(largest)

nums[small_index], nums[large_index] = nums[large_index], nums[small_index]

print(nums)


nums = [-1, 3, 34, -8, -9, 1]

nums[nums.index(-1)] = 100

print(nums)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

avg1 = sum(list1) / len(list1)
avg2 = sum(list2) / len(list2)

print("Average of list 1:", avg1)
print("Average of list 2:", avg2)


num = int(input("Enter a number: "))

if num % 3 == 0:
    num = num + 5

print(num) 



nums = [3, 10, 15, 54, 75, 25, 23]

for num in nums:
    if num % 3 == 0 and num % 5 != 0:
        print(num)



nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

for num in nums:
    if num > 20:
        print(num)

nums = [-1, 3, 34, -8, -9, 1]

for num in nums:
    if num < 0:
        print(num)
        

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(nums))


num = int(input("Enter a number: "))

if num % 3 == 0:
    num = num * 5

print(num)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

if total % 5 == 0:
    print("Sum is divisible by 5")
else:
    print("Sum is not divisible by 5")


nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

for num in nums:
    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num)
            
            
            
 nums = [-1, 3, 34, -8, -9, 1]

# 1. Add an element
nums.append(10)
print("After append:", nums)

# 2. Remove an element
nums.remove(34)
print("After remove:", nums)

# 3. Insert an element
nums.insert(1, 100)
print("After insert:", nums)

# 4. Find length
print("Length:", len(nums))

# 5. Find largest element
print("Largest:", max(nums))

# 6. Find smallest element
print("Smallest:", min(nums))

# 7. Sort the list
nums.sort()
print("Sorted:", nums)

# 8. Reverse the list
nums.reverse()
print("Reversed:", nums)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

average = sum(nums) / len(nums)

print("Average:", average)


num = 1578693
divisors = []

for i in range(1, 11):
    if num % i == 0:
        divisors.append(i)

print("Divisors:", divisors)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 5 == 0:
    num1 = num1 ** 2

if num2 % 5 == 0:
    num2 = num2 ** 2

print(num1)
print(num2)

nums = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

prime = []
even = []
odd = []

for num in nums:

    # Even numbers
    if num % 2 == 0:
        even.append(num)

    # Odd numbers
    else:
        odd.append(num)

    # Prime numbers
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(num)

print("Prime numbers:", prime)
print("Even numbers:", even)
print("Odd numbers:", odd)

           
           
 nums = [-1, 3, 34, -8, -9, 1]

result = []

for num in nums:
    if num >= 0 and num % 3 != 0:
        result.append(num)

print(result)
         
num = 1578693

for i in range(1, 11):
    if num % i == 0:
        num = num - 100
        print(i, "divisible, number =", num)
    else:
        print(i, "not divisible")
        

word = "university"

count = 0
for ch in word:
    if ch in "aeiou":
        count += 1

print(count)



numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# Print 89 using its index
print(numbers[12])

# Add 59 at the 9th index
numbers.insert(9, 59)

print(numbers)


numbers = [-1, 3, 34, -8, -9, 1]

squared = [x ** 2 for x in numbers]

print(squared)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a // b

print("Floor division:", result)



numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89, 7, 8, 54, 621, 57, 621, 57, 24, 3, 5, 6, 4]

unique = list(set(numbers))

print(unique)

unique = list(dict.fromkeys(numbers))
print(unique)









