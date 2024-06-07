def find_maximun(numbers):
    if not numbers:
        return None
    
    maximum = numbers[0]
    
    for number in numbers:
        if number > maximum:
            maximum = number
            
    return maximum

numbers_list = [3,5,7,200,8,1,9,4]
maximum_number = find_maximun(numbers_list)
print(f"The largest number in the list is: {maximum_number}")