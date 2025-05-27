#Determining the the greatest common denominator
def gcf(number_1, number_2):
    if number_1 > number_2:
        number_1, number_2 = number_2, number_1

    for i in range (number_1, 0, -1):
        if number_1 % i == 0 and number_2 % i == 0:
            return i

number_1 = 260
number_2 = 80
print(str(gcf(number_1, number_2)))