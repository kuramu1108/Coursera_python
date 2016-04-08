numbers = [1, 2, 3, 4, 5, 6, 7]

def square(numbers):
    new = []
    for num in numbers:
        if num % 2 == 1:
            new.append(num ** 2)
    return new

def square_ver2(numbers):
    return [num ** 2 for num in numbers if num % 2 == 1]

print square(numbers)
print square_ver2(numbers)
