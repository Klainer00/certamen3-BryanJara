
import csv
def registar(lista:list,ID ):

    
    cafev = 0
    cafes = 0
    cafed = 0
    while True:
        equipo = input('[1]Los Genios de la garrafa\n[2]Los Compiladores Despiertos\n[3]Código Borracho\n[4]Los programadores perezosos\n[5]Ctrl+Alt+Derrota\n')
        if equipo == '1':
            equipo = 'Los Genios de la garrafa'
            print(equipo)
            break
        elif equipo == '2':
            equipo = 'Los Compiladores Despiertos'
            break
        elif equipo == '3':
            equipo = 'Código Borracho'

            break
        elif equipo == '4':
            equipo = 'Los programadores perezosos'
            break
        elif equipo == '5':
            equipo = 'Ctrl+Alt+Derrota'
            break    
        else:
            continue
    while True:
        nombre = input('Nombre: ')
        if nombre != '' and nombre.isalpha():
            break
        else:
            print('error intente nuevamente')
            continue
    while True:
        try:
            edad = int(input('Edad: '))
            if edad != '' and edad > 0:
                break
        except:
            print('error intente nuevamente')
            continue
    while True:
        dia =  input('[1]Viernes \n[2]Sábado\n[3]Domingo\n')
        if dia == '1':
            viernes  =  'Viernes'
            try :
                
                cafev =  int(input('Cantidad de cafe\n'))
                if cafev > 0:
                    break
                else:
                    continue
            except:
                print('intente nuevamente con un vaor mayor a 0')
                continue
        elif dia == '2':
            sabado = 'Sábado'
            try :
                
                cafes =  int(input('Cantidad de cafe\n'))
                if cafes > 0:
                    break
                else:
                    continue
            except:
                print('intente nuevamente con un vaor mayor a 0')
                continue
        elif dia == '3':
            domingo = 'Domingo'
            try :
                
                cafed =  int(input('Cantidad de cafe\n'))
                if cafed > 0:
                    break
                else:
                    continue
            except:
                print('intente nuevamente con un vaor mayor a 0')
                continue

        else:
            continue

    lista.append([ID,nombre,edad,equipo,cafev,cafes,cafed])
def listar(lista:list,ID):
    print(f'id \t Jugador \t\t\t edad \t equipo\t\t\t viernes \t sabado\t domingo')
    for elemento in lista:
        nombre = elemento[0]
        edad = elemento[1]
        equipo = elemento[2]
        cafev = elemento[3]
        cafes = elemento[4]
        cafed = elemento[5]
        print(f'{ID} {nombre}\t\t\t {edad}\t {equipo}\t\t\t {cafev} \t {cafes}\t{cafed}')

def imprimir(lista:list):
    with open(f'archvo.csv', 'w', newline='',encoding='utf-8') as archivo :
        escritor =  csv.writer(archivo,delimiter=';')
        escritor.writerow([f'id Jugador  edad  equipo viernes  sabado domingo'])
          
        escritor.writerows(lista)

   
        

