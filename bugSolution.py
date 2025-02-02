def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        raise TypeError("List must contain at least one number.")
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1,0,3,4,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average is: {average_zero}")

my_list_with_string = [1,2,3,"4",5]
try:
    average_string = calculate_average(my_list_with_string) 
    print(f"The average is: {average_string}")
except TypeError as e:
    print(f"Error: {e}")