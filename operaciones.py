lista_tareas = []

def agregar_tarea():
    tarea = input("Ingrese una nueva tarea: ")
    lista_tareas.append(tarea)
    print("Tarea agregada con éxito!!")

def mostrar_tarea():
    if lista_tareas:
        print("Lista de tareas: ")
        for indice, tarea in enumerate(lista_tareas, 1):
            print("{0}. {1}".format(indice, tarea))
    else:
        print("La lista de tareas está vacía.")

def eliminar_tarea():
    mostrar_tarea()
    if len(lista_tareas) > 0:
        try:
            numero_tarea = int(input("Ingrese el número de tarea que desea eliminar: "))

            if 1 <= numero_tarea <= len(lista_tareas):
                tarea_eliminada = lista_tareas.pop(numero_tarea - 1)
                print("Tarea '{0}' eliminada con éxito.".format(tarea_eliminada))
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Ingrese un número válido.")
    else:
        print("La lista de tareas está vacía.")

def mostrar_opciones(flag_opcion):
    if flag_opcion == 1:
        print("-------------------------------")
        print("*** Lista de Tareas *** \n",
              "1. Agregar Tarea \n",
              "2. Mostrar Tarea \n",
              "3. Eliminar Tarea \n",
              "4. Salir")
    elif flag_opcion == 2:
        print("-------------------------------")
        print("*** Calculadora *** \n",
              "1. Sumar \n",
              "2. Restar \n",
              "3. Multiplicar \n",
              "4. Dividir \n",
              "5. Salir")

def calculadora(flag_calculo):
    numero_1=int(input("Ingrese el primer numero: "))
    numero_2=int(input("Ingrese el segundo numero: "))

    if flag_calculo=="suma":
        calculo=numero_1+numero_2
    elif flag_calculo=="resta":
        calculo=numero_1-numero_2
    elif flag_calculo=="multiplicacion":
        calculo=numero_1*numero_2
    elif flag_calculo=="division":
        calculo=numero_1/numero_2
    
    print("el resultado de la {0} es {1}".format(flag_calculo, calculo))

while True:
    print("-------------------------------")
    print("\nBienvenido a la sección de tareas básicas!\n",
          "1. Lista de Tareas\n",
          "2. Calculadora\n")

    elegir = int(input("Ingrese una opción de lo que quiere realizar: "))

    if elegir == 1:
        while True:
            mostrar_opciones(flag_opcion=1)

            print("-------------------------------")

            opcion = int(input("Ingrese una opción: "))

            print("-------------------------------")

            if opcion == 1:
                agregar_tarea()
            elif opcion == 2:
                mostrar_tarea()
            elif opcion == 3:
                eliminar_tarea()
            elif opcion == 4:
                print("Gracias por usar la Lista de Tareas. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

    elif elegir == 2:
        while True:
            mostrar_opciones(flag_opcion=2)

            print("-------------------------------")

            opcion = int(input("Ingrese una opción: "))

            print("-------------------------------")

            if opcion == 1:
                calculadora("suma")
            elif opcion == 2:
                calculadora("resta")
            elif opcion == 3:
                calculadora("multiplicacion")
            elif opcion == 4:
                calculadora("division")
            elif opcion == 5:
                print("Gracias por usar la Calculadora. ¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

    else:
        print("No se encuentra esta opción. Por favor, elija una opción válida.")