#Determine the sum of even numbers
def sum_of_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += num
            print(num)
    return count
    
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
print(sum_of_even(numbers))
