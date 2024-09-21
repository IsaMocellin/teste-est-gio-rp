def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

def is_in_fibonacci(n):
    fib_seq = fibonacci(n)
    if n in fib_seq:
        return f'O número {n} pertence à sequência de Fibonacci.'
    else:
        return f'O número {n} não pertence à sequência de Fibonacci.'

numero = int(input("Digite um número: "))
print(is_in_fibonacci(numero))
