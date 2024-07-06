def calculate_average(numbers):
    if not numbers:
        return None
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers_list = [3, 5, 7, 200, 8, 1, 9, 4]
average = calculate_average(numbers_list)
print(f"The average of the list is: {average}")