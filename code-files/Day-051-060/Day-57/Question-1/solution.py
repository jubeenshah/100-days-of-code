
dictFib = {}
def fib(N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N in dictFib:
        return dictFib[N]
    dictFib[N] = fib(N-1) + fib(N-2)
    print(N,dictFib)
    return dictFib[N]
fib(70)       