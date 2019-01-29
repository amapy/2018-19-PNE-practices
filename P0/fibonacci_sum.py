def fibonacci(n):
    n = int(n)

    fib_series = [0, 1, ]

    i = 0

    for i in range(n):

        fib_series.append(fib_series[i] + fib_series[i + 1])
        addition = fib_series[i] + fib_series[i + 1]
        i += 1

    print("The sum of the terms from the first to term", n, "is: ", addition - 1)


n = int(input("Please, introduce the n-th term of the fibonacci series for obtaining the sum from the beginning: "))

fibonacci(n)
