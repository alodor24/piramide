def crear_piramide(rows):
    for i in range(rows):
        print('*' * (i + 1))

if __name__ == "__main__":
    rows = int(input('Ingrese la cantidad de filas que desea para la piramide: '))
    crear_piramide(rows)