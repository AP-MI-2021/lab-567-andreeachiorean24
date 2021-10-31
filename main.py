import datetime
from Logic.crud import adauga
from Tests.test_crud import test_adauga, test_citire, test_modificare, test_stergere
from Userinteface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = adauga(cheltuieli, 2, 10, 300, datetime.date(2021, 3, 4), 'canal')
    cheltuieli = adauga(cheltuieli, 3, 21, 305, datetime.date(2021, 5, 6), 'canal')
    cheltuieli = adauga(cheltuieli, 4, 10, 54, datetime.date(2021, 8, 6), 'alte cheltuieli')
    cheltuieli = adauga(cheltuieli, 5, 23, 540, datetime.date(2021, 3, 7), 'canal')
    cheltuieli = adauga(cheltuieli, 6, 23, 200, datetime.date(2021, 7, 9), 'intretinere')
    cheltuieli = adauga(cheltuieli, 7, 11, 30, datetime.date(2021, 6, 2), 'intretinere')
    cheltuieli = run_ui(cheltuieli)

if __name__ == '__main__':
    test_adauga()
    test_citire()
    test_modificare()
    test_stergere()
    main()