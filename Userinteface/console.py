from Domain.cheltuiala import get_str, creeaza_cheltuiala
from Logic.crud import adauga, modificare, stergere
import datetime

from Logic.stergerea_cheltuieliilor import sterge_cheltuieli


def show_menu():
    print('1. CRUD')
    print('2. Ștergerea tuturor cheltuielilor pentru un apartament ')
    print('3. Iesire ')


def readDate():
    givenString = input('Dati data, cu elementele separate printr-o liniuta: ')
    numbersAsString = givenString.split('-')
    year = int(numbersAsString[0])
    month = int(numbersAsString[1])
    day = int(numbersAsString[2])
    return datetime.date(year, month, day)


def handle_add(cheltuieli):
    try:
        id_cheltuiala=int(input('Dati id-ul cheltuielii'))
        nr_apartament=int(input('Dati nr apartament'))
        suma=float(input('Dati suma cheltuielii'))
        data=readDate()
        tip=input('Dati tipul:')
        return adauga(cheltuieli, id_cheltuiala, nr_apartament, suma, data, tip)
    except ValueError as ve:
        print('Eroare:', ve)

    return cheltuieli


def handle_update(cheltuieli):
    try:
        id_cheltuiala = int(input('Dati id-ul cheltuielii care se actualizeaza'))
        nr_apartament = int(input('Dati nr apartament care se actualizeaza'))
        suma = float(input('Dati noua suma a cheltuielii'))
        data = readDate()
        tip = input('Dati noul tip:')
        return modificare(cheltuieli, creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tip))
    except ValueError as ve:
        print('Eroare:', ve)
    return cheltuieli

def handle_delete(cheltuieli):
    try:
        id_cheltuiala = int(input('Dati id-ul cheltuielii care se va sterge'))
        cheltuieli = stergere(cheltuieli, id_cheltuiala)
        print('Stergerea a fost efectuata cu succes')
    except ValueError as ve:
        print('Eroare:', ve)
    return cheltuieli


def handle_crud(cheltuieli):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('b. Revenire')
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli=handle_add(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli)
        elif optiune == '3':
            cheltuieli=handle_delete(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida')
    return cheltuieli


def handle_show_all(cheltuieli):
    for cheltuiala in cheltuieli:
        print(get_str(cheltuiala))


def handle_stergere_pt_ap(cheltuieli):
    try:
        nr_apartament = int(input('Dati nr ap pt care se sterg cheltuieliile'))
        return sterge_cheltuieli(nr_apartament, cheltuieli)
    except ValueError as ve:
        print('Eroare:', ve)
    return cheltuieli

def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli=handle_crud(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_stergere_pt_ap(cheltuieli)
        elif optiune == '3':
            break
        else:
            print('Optiune invalida')
    return cheltuieli