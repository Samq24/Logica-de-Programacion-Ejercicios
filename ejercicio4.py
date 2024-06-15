def sort_list(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

numbers_list = [3, 5, 7, 200, 8, 1, 9, 4]
sorted_list = sort_list(numbers_list)
print(f"The sorted list is: {sorted_list}")