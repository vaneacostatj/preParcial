#realizar un sw simple que administre la bd de un negocio de empanadas 
#ingrese una empanada -> menu
  #id
  #nombre
  #precio
  #popularidad
  #fecha de vencimiento 
#mostrar todas las empanadas registradas -> push de objetos
#filtro por id
#editar por id (precio)
#eliminar por id
# 0 termina el programa 

#listas {} corchetes []

option = 1
empanadas = [] 
while option != 0:       
    print('Empanadas el Canival')
    print('Opción 1 =  Ingresar una empanada')
    print('Opción 2 =  Mostrar todas las empanada')
    print('Opción 3 =  Busca una empanada')
    print('Opción 4 =  Editar una empanada')
    print('Opción 5 =  Eliminar una empanada')
    print('Opción 0 para salir')
    option = int(input('Escoja una opción: '))

    if(option == 1):
        empanada = { }
        empanada['id'] = len(empanadas) + 1
        empanada['nombre'] = input('Ingresa un nombre')
        empanada['precio'] = float(input('Ingresa el precio'))
        empanada['popularidad'] = int(input('Digite la popularidad de la empanada: '))
        empanada['fechaVencimiento'] = int(input('Digite la fecha de vencimiento: '))
        empanadas.append(empanada)
        print('Empanada registrada')

    elif(option == 2):
        for empanada in empanadas:
            print(empanada)
    
    elif(option == 3):
        _id = int(input('Digite el id de la empanada que desea editar: '))
        for empanada in empanadas:
            if empanada['id'] == _id :
                print(empanada)
        print('La empanada no esta dentro del inventario')

    elif(option == 4):
        _id = int(input('Digite el id de la empanada que desea editar: '))
        for empanada in empanadas:
            if empanada['id'] == _id :
                print(f"el precio de la empanada es: {empanada['precio']}")
                empanada['precio'] = float(input('Ingresa el nuevo precio: '))

    elif(option == 5):
        pass
    elif(option == 0):
        pass
    else:
        print('Opción invalida')


#hacer el eliminar 
#agregar elementos a una lista
#manipular lista (buscar editar eliminar)
# recorrer una lista al reves
# 
# 
# 
#     