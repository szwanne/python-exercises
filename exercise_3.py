#Determine the sum of odd numbers

def sum_of_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += num
            print(count)
    return count
numbers = range(0, 10)
print(sum_of_odd(numbers))