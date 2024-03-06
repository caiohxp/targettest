def fib(n, first, second):

    if n == first:
        print('O número pertence a sequencia')
    elif n < first:
        print('O número não pertence a sequencia')
        return
    else:
        fib(n, second, first + second)

n = int(input())
fib(n, 0, 1)