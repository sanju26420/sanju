numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = []

for num in numbers:
    if num % 2 == 0:
        result.append("Even")
    else:
        result.append("Odd")

print(result)
