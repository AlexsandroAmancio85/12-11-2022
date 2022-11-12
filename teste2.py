notas_acumulo = 0

for i in range(1, 5, 1):
    nota = float(input(f"digite a {i} nota: "))

    notas_acumulo += nota

media = notas_acumulo / 4

print(f"sua nota e igual a: {media}")