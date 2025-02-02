def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will print 0

my_list_with_zero = [1,0,3,4,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average is: {average_zero}") #This is the correct average, no problem

my_list_with_string = [1,2,3,"4",5]
average_string = calculate_average(my_list_with_string) #This will throw an error
print(f"The average is: {average_string}")