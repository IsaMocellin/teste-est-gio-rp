def verificar_letra_a(texto):
    contador = texto.lower().count('a')
    if contador > 0:
        return f"A letra 'a' aparece {contador} vezes."
    else:
        return "A letra 'a' não aparece na string."

texto = input("Digite uma string: ")
print(verificar_letra_a(texto))
