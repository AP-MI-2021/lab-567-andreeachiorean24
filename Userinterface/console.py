from Domain.cheltuiala import get_str, creeaza_cheltuiala
from Logic import adunarea_unei_val_pt_data
from Logic.adunarea_unei_val_pt_data import adunare_val
from Logic.crud import adauga, modificare, stergere
import datetime

from Logic.det_cea_mai_mare_chelt import mare_cheltuiala
from Logic.ord_desc_dupa_suma import ord_desc
from Logic.stergerea_cheltuieliilor import sterge_cheltuieli
from Logic.sume_lunare_pt_ap import sume_pt_ap
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1. CRUD')
    print('2. Ștergerea tuturor cheltuielilor pentru un apartament ')
    print('3. Adunarea unei valori la toate cheltuielile dintr-o dată citită.')
    print('4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.')
    print('5. Ordonarea cheltuielilor descrescător după sumă. ')
    print('6. Afișarea sumelor lunare pentru fiecare apartament.')
    print('u. Undo')
    print('r. Redo')
    print('7. Iesire ')


def readDate():
    givenString = input('Dati data, cu elementele separate printr-o liniuta: ')
    numbersAsString = givenString.split('-')
    year = int(numbersAsString[0])
    month = int(numbersAsString[1])
    day = int(numbersAsString[2])
    return datetime.date(year, month, day)


def handle_add(cheltuieli, undo_list, redo_list):
    try:
        id_cheltuiala=int(input('Dati id-ul cheltuielii'))
        nr_apartament=int(input('Dati nr apartament'))
        suma=float(input('Dati suma cheltuielii'))
        data=readDate()
        tip=input('Dati tipul:')
        new_cheltuiala = creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tip)
        cheltuieli = adauga(cheltuieli, id_cheltuiala, nr_apartament, suma, data, tip, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)

    return cheltuieli
def handle_update(cheltuieli, undo_list, redo_list):
    try:
        id_cheltuiala = int(input('Dati id-ul cheltuielii care se actualizeaza'))
        nr_apartament = int(input('Dati nr apartament care se actualizeaza'))
        suma = float(input('Dati noua suma a cheltuielii'))
        data = readDate()
        tip = input('Dati noul tip:')
        new_cheltuiala = creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tip)
        cheltuieli = modificare(cheltuieli, creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tip, undo_list, redo_list))
    except ValueError as ve:
        print('Eroare:', ve)
    return cheltuieli

def handle_delete(cheltuieli, undo_list, redo_list):
    try:
        id_cheltuiala = int(input('Dati id-ul cheltuielii care se va sterge'))
        cheltuieli = stergere(cheltuieli, id_cheltuiala, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes')
    except ValueError as ve:
        print('Eroare:', ve)
    return cheltuieli


def handle_crud(cheltuieli, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('b. Revenire')
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli=handle_add(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli = handle_update(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli=handle_delete(cheltuieli, undo_list, redo_list)
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


def handle_stergere_pt_ap(cheltuieli, undo_list, redo_list):
    try:
        nr_apartament = int(input('Dati nr ap pt care se sterg cheltuieliile'))
        cheltuieli = sterge_cheltuieli(nr_apartament, cheltuieli, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
    return cheltuieli
def handle_adaugare_pt_data(cheltuieli, undo_list, redo_list):
    try:
        data = readDate()
        valoare = float(input('Dati valoarea care se adauga'))
        cheltuieli=adunare_val(cheltuieli, data, valoare, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
    return cheltuieli


def handle_cea_mai_mare_cheltuiala(cheltuieli):
    new = mare_cheltuiala(cheltuieli)
    for tip in new:
        print(f'Pentru tipul: {tip} avem cheltuiala: {get_str(new[tip])}')


def handle_ord(cheltuieli, undo_list, redo_list):
    cheltuieli = ord_desc(cheltuieli, undo_list, redo_list)
    print('Cheltuieliile au fost ordonate')
    return cheltuieli


def handle_sume_lunare(cheltuieli):
    new = sume_pt_ap(cheltuieli)
    for luna in new:
        print(f'Pentru Luna {luna} avem lista de sume: {new[luna]}')


def handle_undo(cheltuieli, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, cheltuieli)
    if undo_result is not None:
        return undo_result
    return cheltuieli


def handle_redo(cheltuieli, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, cheltuieli)
    if redo_result is not None:
        return redo_result
    return cheltuieli


def run_ui(cheltuieli, undo_list, redo_list):
    while True:
        handle_show_all(cheltuieli)

        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            cheltuieli=handle_crud(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            cheltuieli = handle_stergere_pt_ap(cheltuieli, undo_list, redo_list)
        elif optiune == '3':
            cheltuieli = handle_adaugare_pt_data(cheltuieli, undo_list, redo_list)
        elif optiune == '4':
            handle_cea_mai_mare_cheltuiala(cheltuieli)
        elif optiune == '5':
            cheltuieli = handle_ord(cheltuieli, undo_list, redo_list)
        elif optiune == '6':
            handle_sume_lunare(cheltuieli)
        elif optiune == 'u':
            cheltuieli = handle_undo(cheltuieli, undo_list, redo_list)
        elif optiune == 'r':
            cheltuieli = handle_redo(cheltuieli, undo_list, redo_list)
        elif optiune == '7':
            break
        else:
            print('Optiune invalida')
    return cheltuieli