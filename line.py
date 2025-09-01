def line():
    A = float(input('Ingrese el coeficiente A: '))
    print(f'El coeficiente A de su ecuación de la recta es: {A}')
    B = float(input('Ingrese el coeficiente B: '))
    print(f'El coeficiente B de su ecuación de la recta es: {B}')
    X1 = float(input('Ingrese el coeficiente X1: '))
    print(f'El coeficiente X1 de su ecuación de la recta es: {X1}')
    X2 = float(input('Ingrese el coeficiente X2: '))
    print(f'El coeficiente X2 de su ecuación de la recta es: {X2}')
    Y1 = A * X1 + B
    Y2 = A * X2 + B  
    P1 = (X1, Y1)
    P2 = (X2, Y2)
    import math
    distancia = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2 )
    print(f'\nPara la siguiente ecuación:')
    print(f'\tY = {A}X + {B}')
    print('\nDados los siguientes puntos:')
    print(f'\tP1 {P1}')
    print(f'\tP2 {P2}')
    print(f'\nLa distancia entre ellos es: {distancia}')
    return distancia
    print("TO DO")

line()

