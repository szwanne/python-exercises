#Determine the sum of even numbers
# def sum_of_even(numbers):
#     count = 0
#     for number in numbers:
#         count = count  + number
#         # print(count)
#     return count

# print(sum_of_even(range(0,10)))

# def sum_of_even(numbers):
#     if numbers % 2 == 0:
#         count = 0
#         for number in numbers:
#             count = count + numbers[number]
#         return count


def sum_of_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += num
            print(num)
    return count
    
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]
print(sum_of_even(numbers))
