import os
from listaenlazada import ListaEnlazada

polinomio1 = ListaEnlazada()
polinomio2 = ListaEnlazada()
resultado_suma = ListaEnlazada()
resultado_resta = ListaEnlazada()
reusltdo_evaluacion = ListaEnlazada()

while True:
    print("Menu")
    print("1. Ingresar Polinomio 1")
    print("2. Ingresar Polinomio 2")
    print("3. Adicion")
    print("4. Substraccion")
    print("5. Evaluar")
    print("6. Salir")
    opcion = int(input('ingrese una opcion: '))

    if opcion == 1:
        print("Lista: ")
        polinomio1.imprimir_lista()
        coeficiente = int(input("Ingrese el coeficiente a agregar:"))
        polinomio1.insertar_final(coeficiente)
        polinomio1.imprimir_lista()
    elif opcion == 2:
        print("Lista: ")
        polinomio2.imprimir_lista()
        coeficiente = int(input("Ingrese el coeficiente a agregar:"))
        polinomio2.insertar_final(coeficiente)
        polinomio2.imprimir_lista()
    elif opcion == 3:
        resultado_suma = polinomio1.sumar(polinomio1, polinomio2)
        resultado_suma.imprimir_lista()
    elif opcion == 4:
        resultado_resta = polinomio1.restar(polinomio1, polinomio2)
        resultado_resta.imprimir_lista()
    elif opcion == 5:
        evaluar = int(input("Ingrese el numero a evaluar:"))
        print("1. Polinomio 1")
        print("2. polinomio 2")
        opcion = int(input("Ingrese el polinomio"))
        if opcion == 1:
            resultado_evaluacion = polinomio1.evaluar_polinomio(evaluar)
        elif opcion == 2:
            resultado_evaluacion = polinomio2.evaluar_polinomio(evaluar)
            print(resultado_evaluacion)
    elif opcion == 6:
        break
    else:
        continue
