from Domain.cheltuiala import get_str, creeaza_cheltuiala
from Logic import adunarea_unei_val_pt_data
from Logic.adunarea_unei_val_pt_data import adunare_val
from Logic.crud import adauga, modificare, stergere
import datetime

from Logic.det_cea_mai_mare_chelt import mare_cheltuiala
from Logic.ord_desc_dupa_suma import ord_desc
from Logic.stergerea_cheltuieliilor import sterge_cheltuieli
from Logic.sume_lunare_pt_ap import sume_pt_ap


def show_menu():
    print('1. CRUD')
    print('2. Ștergerea tuturor cheltuielilor pentru un apartament ')
    print('3. Adunarea unei valori la toate cheltuielile dintr-o dată citită.')
    print('4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.')
    print('5. Ordonarea cheltuielilor descrescător după sumă. ')
    print('6. Afișarea sumelor lunare pentru fiecare apartament.')
    print('7. Iesire ')


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
def handle_adaugare_pt_data(cheltuieli):
    try:
        data = readDate()
        valoare = float(input('Dati valoarea care se adauga'))
        cheltuieli=adunare_val(cheltuieli, data, valoare)
    except ValueError as ve:
        print('Eroare:', ve)
    return cheltuieli


def handle_cea_mai_mare_cheltuiala(cheltuieli):
    new = mare_cheltuiala(cheltuieli)
    for tip in new:
        print(f'Pentru tipul: {tip} avem cheltuiala: {get_str(new[tip])}')


def handle_ord(cheltuieli):
    lista = ord_desc(cheltuieli)
    print('Cheltuieliile au fost ordonate')
    return lista


def handle_sume_lunare(cheltuieli):
    new = sume_pt_ap(cheltuieli)
    for luna in new:
        print(f'Pentru Luna {luna} avem lista de sume: {new[luna]}')





def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli=handle_crud(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_stergere_pt_ap(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_adaugare_pt_data(cheltuieli)
        elif optiune == '4':
            cheltuieli = handle_cea_mai_mare_cheltuiala(cheltuieli)
        elif optiune == '5':
            cheltuieli = handle_ord(cheltuieli)
        elif optiune == '6':
            cheltuieli = handle_sume_lunare(cheltuieli)
        elif optiune == '7':
            break
        else:
            print('Optiune invalida')
    return cheltuieli