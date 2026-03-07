def generala(lista):
    generala=False
    
    if lista[0]==lista[1]==lista[2]==lista[3]==lista[4]:
        generala=True    
        return generala
    else:
        return generala #validar despeus enn otrae funcion si el turno es igiual a 1 o no


def escalera(lista):
    escalera=False
    lista_ordenada = sorted(lista) #ordena de menor a mayor. ojo con .sort() porque modifica la lista original
    
    for i in range(len(lista_ordenada)-1):
        if lista_ordenada[i]+1!=lista_ordenada[i+1]:
            return escalera
        
    escalera=True
    return escalera 


def poker(lista):
    poker=False
    for numero in lista:
        contador=0
        for i in range(len(lista)):
            if numero==lista[i]:
                contador+=1
                if contador >= 4:
                    poker=True
                    
    return poker
            

def full(lista):

    valores_unicos = set(lista) #la convierte en un conjunto (lista sin elementos repetidos)
    if len(valores_unicos) != 2:
        return False
    cantidad = lista.count(lista[0])
    return cantidad in [2, 3] #lo que hace es asegurarse de que la lista tiene 2 valores unicos. En ese caso por descarte uno aparece 2 veces y otro 3.


def numero_ind(lista):
    
    n1=lista.count(1)*1
    n2=lista.count(2)*2
    n3=lista.count(3)*3
    n4=lista.count(4)*4
    n5=lista.count(5)*5
    n6=lista.count(6)*6
    
    return [n1, n2, n3, n4, n5, n6]
            

def tiradas():
    import random
    
    tirada = 1
    decision = ''
    
    d1 = 0; d2 = 0; d3 = 0; d4 = 0; d5 = 0
    
    #arrancamos todas las decisiones en 'si' para que la primera vez tire todos
    des1 = 'si'; des2 = 'si'; des3 = 'si'; des4 = 'si'; des5 = 'si'
    
    #el while es un bloque de preguntas y asignacion de valores. primero van las preguntas y despues se asignan los valores
    while tirada <= 3:
        
        #se saltea en la primera tirada, antes de la primera tirada no hay nada para preguntar
        if tirada != 1:
            print("\nQué dados querés volver a tirar?")
            des1 = input('Dado 1 (si/no): ')
            des2 = input('Dado 2 (si/no): ')
            des3 = input('Dado 3 (si/no): ')
            des4 = input('Dado 4 (si/no): ')
            des5 = input('Dado 5 (si/no): ')
            
            decision = input('Escriba "fin" para plantarse acá, o presione Enter para tirar: ')
            
            #si escribe "fin", rompo el bucle while y no tira mas
            if decision == 'fin':
                break 
                
        print('\n--- Resultados de la Tirada', tirada, '---')
        
        #antes del while pusimos todo esto en si, entonces en la primera tirada se saltea las preguntas y automaticamente los dados toman valor aleatorio
        if des1 == 'si':
            d1 = random.randint(1, 6)
        print('Valor Dado 1 =', d1)
        
        if des2 == 'si':
            d2 = random.randint(1, 6)
        print('Valor Dado 2 =', d2)
        
        if des3 == 'si':
            d3 = random.randint(1, 6)
        print('Valor Dado 3 =', d3)
        
        if des4 == 'si':
            d4 = random.randint(1, 6)
        print('Valor Dado 4 =', d4)
        
        if des5 == 'si':
            d5 = random.randint(1, 6)
        print('Valor Dado 5 =', d5)
        
        tirada += 1
        
    dados = [d1, d2, d3, d4, d5]
    tirada_final = tirada - 1 
    
    return tirada_final, dados



def juego_terminado(listaj1, listaj2):
    
    if len(listaj1) == 10 and len(listaj2) == 10:
        return True
    return False


def guardar_csv(planilla_j1, planilla_j2):
    categorias = ['E', 'F', 'P', 'G', '1', '2', '3', '4', '5', '6']
    with open('jugadas.csv', 'w') as f:
        f.write("jugada,j1,j2\n")
        for cat in categorias:
            p1 = planilla_j1.get(cat, 0)
            p2 = planilla_j2.get(cat, 0)
            f.write(f"{cat},{p1},{p2}\n")

def main(): 

    #usamos diccionarios para relacionar los puntos obtenidos con su correspondiente categoria
    planilla_j1 = {}
    planilla_j2 = {}
    
    categorias_numeros = ['1', '2', '3', '4', '5', '6']
    categorias_mayores = ['E', 'F', 'P', 'G']
    
    print("--- BIENVENIDOS A LA GENERALA ---")

    while not juego_terminado(planilla_j1, planilla_j2):
        for j in range(1, 3):
            if j == 1:
                planilla_actual = planilla_j1
            else:
                planilla_actual = planilla_j2
            
            #si el jugador ya lleno sus 10 categorias salteamos su turno
            if len(planilla_actual) == 10:
                continue

            print(f"\nTURNO DEL JUGADOR {j}")
            tirada_final, dados = tiradas()
            
            #servido: lograr la jugada en el primer tiro sin volver a tirar ningun dado
            es_servido = (tirada_final == 1) #devuelve booleano
            
            print(f"Dados finales del Jugador {j}: {dados}")

            #chequeo de victoria por generala real
            if generala(dados) and es_servido:
                print(f"¡GENERALA REAL! El Jugador {j} gana automáticamente.")
                planilla_actual['G'] = 80 
                guardar_csv(planilla_j1, planilla_j2)
                
                total_j1 = sum(planilla_j1.values()) 
                total_j2 = sum(planilla_j2.values()) 
                
                print("\n--- FIN DEL JUEGO ---")
                print(f"Puntaje Final J1: {total_j1}")
                print(f"Puntaje Final J2: {total_j2}")
                return

            #mostrar opciones y elegir categoria
            disponibles = [c for c in (categorias_numeros + categorias_mayores) if c not in planilla_actual] #con append me llevaba 4 lineas de codigo lo escribo asi para resumir 
            print(f"Categorías pendientes: {disponibles}")
            
            eleccion = input("Elija categoría para anotar: ").upper()
            while eleccion not in disponibles:
                eleccion = input("Invalida o ya usada. Elija de nuevo: ").upper()

            #calcular puntos. arranca en 0 por si elige una categoria pero no tiene la jugada
            puntos = 0 
            
            if eleccion == 'G':
                if generala(dados): 
                    puntos = 50
            elif eleccion == 'P':
                if poker(dados): 
                    puntos = 40 + (5 if es_servido else 0)
            elif eleccion == 'F':
                if full(dados): 
                    puntos = 30 + (5 if es_servido else 0)
            elif eleccion == 'E':
                if escalera(dados):
                    puntos = 20 + (5 if es_servido else 0)
            elif eleccion in categorias_numeros:
                totales_num = numero_ind(dados)
                puntos = totales_num[int(eleccion) - 1]

            #guardar en la planilla y actualizar el archivo csv
            planilla_actual[eleccion] = puntos
            guardar_csv(planilla_j1, planilla_j2)
            print(f"Anotado: {puntos} puntos en la categoría {eleccion}.")

    #fin del juego por planillas completas
    total_j1 = sum(planilla_j1.values()) #el values me da una lista con los valores (osea los puntos) de cada categoria
    total_j2 = sum(planilla_j2.values()) #sum da la suma de todos los elementos de la lista values
    
    print("\n--- FIN DEL JUEGO ---")
    print(f"Puntaje Final J1: {total_j1}")
    print(f"Puntaje Final J2: {total_j2}")
    
    if total_j1 > total_j2: 
        print("¡Gana el Jugador 1!")
    elif total_j2 > total_j1: 
        print("¡Gana el Jugador 2!")
    else: 
        print("¡Empate!")

if __name__ == "__main__":
    main()
