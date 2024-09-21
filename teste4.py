def completar_sequencia():
    #ímpares
    sequencia_a = [1, 3, 5, 7]
    proximo_a = sequencia_a[-1] + 2
    print(f"a) Próximo número: {proximo_a}")

    #potências de 2
    sequencia_b = [2, 4, 8, 16, 32, 64]
    proximo_b = sequencia_b[-1] * 2
    print(f"b) Próximo número: {proximo_b}")

    #quadrados perfeitos
    sequencia_c = [0, 1, 4, 9, 16, 25, 36]
    proximo_c = (len(sequencia_c)) ** 2
    print(f"c) Próximo número: {proximo_c}")

    #quadrados perfeitos de pares
    sequencia_d = [4, 16, 36, 64]
    proximo_d = (2 * (len(sequencia_d) + 1)) ** 2
    print(f"d) Próximo número: {proximo_d}")

    #sequência de Fibonacci
    sequencia_e = [1, 1, 2, 3, 5, 8]
    proximo_e = sequencia_e[-1] + sequencia_e[-2]
    print(f"e) Próximo número: {proximo_e}")

    #sequência alternada
    sequencia_f = [2, 10, 12, 16, 17, 18, 19]
    proximo_f = 20
    print(f"f) Próximo número: {proximo_f}")

completar_sequencia()
