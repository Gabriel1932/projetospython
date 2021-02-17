matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
scol = slin = 0
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]: '))
print("-=" * 30)
for l in range(0, 3):
    for c in range (0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
for l in range(0, 3):
    scol += matriz[l][2]
print(f"a soma do itens da terceira coluna é {scol}.")
for c in range (0, 3):
    slin += matriz[1][c]
print(f'a soma da linha numero 2 é {slin}.')
