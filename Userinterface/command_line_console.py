from Domain.cheltuiala import creeaza_cheltuiala, get_str
from Logic.crud import adauga, stergere


def show_menu():
    print('Adaugam cheltuieli in lista cu functia "add" si introducem valori adecvate')
    print('Stergem cheltuieli din lista de cheltuieli cu functia "delete" si introducem un id al unei cheltuieli')
    print('Afisam toate cheltuielile din lista de cheltuieli cu functia "show_all"')
    print('Toate comenzile le apelam pe o singura linie si separate prin ";" ,iar campurile prin "," ')
    print('')

def add(lista, id_ap, nr_ap, suma, data, tip):
    try:
        id_ap = int(id_ap)
    except ValueError as ve:
        print('Eroare: ', ve)
    try:
        nr_ap = int(nr_ap)
    except ValueError as ve:
        print('Eroare: ', ve)
    try:
        suma = int(suma)
    except ValueError as ve:
        print('Eroare: ', ve)
    try:
        new_cheltuiala = creeaza_cheltuiala(id_ap, nr_ap, suma, data, tip)
        lista = adauga(lista, id_ap, nr_ap, suma, data, tip, [], [])
    except ValueError as ve:
        print('Eroare:', ve)
    return lista


def delete(lista, id_ap):
    try:
        id_ap = int(id_ap)
    except ValueError as ve:
        print('Eroare: ', ve)
        return lista
    try:
        lista = stergere(lista, id_ap, [], [])
    except ValueError as ve:
        print('Eroare:', ve)
    return lista

def show_all(lista):
    for cheltuiela in lista:
        print(get_str(cheltuiela))

def run_in_line_console(lista):
    while True:
        show_menu()
        optiune = input('Introduceti comenzile:')
        optiuni = optiune.split(';')
        for comenzi in optiuni:
            optiune2 = comenzi.split(',')
            if optiune2[0] == 'add':
                id_ap = optiune2[1]
                nr_ap = optiune2[2]
                suma = optiune2[3]
                data = optiune2[4]
                tip = optiune2[5]
                lista = add(lista, id_ap, nr_ap, suma, data, tip)
            if optiune2[0] == 'delete':
                id_ap = optiune2[1]
                lista = delete(lista, id_ap)
            if optiune2[0] == 'show_all':
                show_all(lista)
