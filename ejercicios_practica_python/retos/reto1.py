"""
Eliminar del array elementos duplicados y ordenar array [1,2,5,3,2,3,4,5,1,1,6,6,7]
"""
arr = [1,2,5,3,2,3,4,5,1,1,6,6,7]

arrAux = []

for i in arr:
    if(i in arrAux):
        print("Ya lo contiene")
    else:
        arrAux.append(i)
arrAux.sort()
print(arrAux)

