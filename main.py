
import datetime
from Logic.crud import adauga
from Tests.test_crud import test_adauga, test_citire, test_modificare, test_stergere
from Tests.test_functionalitati import test_adunarea_unei_val, test_stergerea_cheltuieliilor, test_mare_cheltuiala, \
    test_ord_desc, test_sume_pt_ap, test_undo_redo
from Tests.test_lab_7 import test_lab_7, test_stergerea_cheltuieliilor_undo_redo, test_adunare_val_undo_redo, \
    test_ord_desc_undo_redo
from Userinterface.command_line_console import run_in_line_console
from Userinterface.console import run_ui



def meniuri():
    print('1.Meniul vechi')
    print('2.Meniul nou')
    print('x.Exit')


def main():
    cheltuieli = []
    undo_list = []
    redo_list = []
    cheltuieli = adauga(cheltuieli, 2, 10, 300, datetime.date(2021, 3, 4), 'canal', undo_list, redo_list)
    cheltuieli = adauga(cheltuieli, 3, 21, 305, datetime.date(2021, 5, 6), 'canal', undo_list, redo_list)
    cheltuieli = adauga(cheltuieli, 4, 10, 54, datetime.date(2021, 5, 6), 'alte cheltuieli', undo_list, redo_list)
    cheltuieli = adauga(cheltuieli, 5, 23, 540, datetime.date(2021, 3, 7), 'canal', undo_list, redo_list)
    cheltuieli = adauga(cheltuieli, 6, 23, 200, datetime.date(2021, 7, 9), 'intretinere', undo_list, redo_list)
    cheltuieli = adauga(cheltuieli, 7, 11, 30, datetime.date(2021, 6, 2), 'intretinere', undo_list, redo_list)

    while True:
        meniuri()
        optiune = input('Alegeti interfata: ')
        if optiune == '1':
            run_ui(cheltuieli, undo_list, redo_list)
        elif optiune == '2':
            run_in_line_console(cheltuieli)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')


if __name__ == '__main__':
    test_adauga()
    test_citire()
    test_modificare()
    test_stergere()
    test_stergerea_cheltuieliilor()
    test_adunarea_unei_val()
    test_mare_cheltuiala()
    test_ord_desc()
    test_sume_pt_ap()
    test_undo_redo()
    test_lab_7()
    test_stergerea_cheltuieliilor_undo_redo()
    test_adunare_val_undo_redo()
    test_ord_desc_undo_redo()
    main()