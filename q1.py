maior = 0

for i in range(3):
    numero = int(input("digite um numero qualquer: "))

    if numero > maior:
        maior = numero

print(maior)