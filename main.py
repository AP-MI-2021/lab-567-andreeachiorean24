import datetime
from Logic.crud import adauga
from Tests.test_crud import test_adauga, test_citire, test_modificare, test_stergere
from Userinteface.console import run_ui


def main():
    cheltuieli = []
    cheltuieli = adauga(cheltuieli, 2, 50, 300, datetime.date(2021, 3, 4), 'canal')
    cheltuieli = run_ui(cheltuieli)

if __name__ == '__main__':
    test_adauga()
    test_citire()
    test_modificare()
    test_stergere()
    main()