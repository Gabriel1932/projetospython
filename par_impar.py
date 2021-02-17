list_prim = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
list_par = []
list_imp = []

for x in list_prim :
    if (x % 2 == 0):
        list_par.append(x)
    else:
        list_imp.append(x)

    continue
print('lista de numeros pares ->',list_par,"lista de numeros impar ->",list_imp) 