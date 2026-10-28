def find_largest_even(numbers):
    largest = None

    for num in numbers:
        if num % 2 == 0:
            if largest == None:
                largest = num
            elif num > largest:
                largest = num

    return largest

<<<<<<< HEAD
data = [17, 12, 8, 20, 3, 18, 30]
=======
data = [7, 12, 8, 20, 3, 18, 30]
>>>>>>> 05a7963d3be4766352e82982fb016562301e2138

result = find_largest_even(data)

print("Largest even number is: " + str(result))