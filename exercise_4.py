#Determine the nth term of the fibonacci serie given 0 1 1 2 3 5 8 . . .


def fibonacci(numbers):
    first_term = 0
    second_term = 1
    if numbers == 1:
        return first_term
    if numbers == 2 or numbers == 3:
        return second_term
    for number in range(numbers):
        third_term = first_term + second_term
        first_term = second_term
        second_term = third_term
    return third_term
for number in range(1, 15):
    print(fibonacci(number))