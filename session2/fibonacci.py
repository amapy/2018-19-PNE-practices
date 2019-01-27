def fibonacci(n):
    n = int(n)

    fib_series = [0, 1, ]

    i = 0

    for i in range(n):

        fib_series.append(fib_series[i] + fib_series[i + 1])
        i += 1

    print("The", n,"-th term from the fibonacci series is: ", fib_series[n - 1])


n = int(input("Please, introduce the n-th term of the fibonacci series you want to obtain: "))

fibonacci(n)

