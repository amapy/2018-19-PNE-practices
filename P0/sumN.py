def sum(n):

    n = int(n)

    sum_numbers = 0

    for i in range(n + 1):

        sum_numbers += i

    print("The sum is: ", sum_numbers)
    return

n = int(input("Please, introduce a number to calculate the addition from 1: "))

sum(n)
