import datetime

from Domain.cheltuiala import creeaza_cheltuiala, get_nr_ap, get_id
from Logic.crud import adauga, citire, modificare, stergere


def get_data():
    return [
        creeaza_cheltuiala(2, 5, 100, datetime.date(2021, 9, 5), 'canal'),
        creeaza_cheltuiala(3, 4, 120, datetime.date(2021, 6, 4), 'canal'),
        creeaza_cheltuiala(4, 6, 200, datetime.date(2021, 5, 3), 'alte cheltuieli'),
    ]

def test_adauga():
    cheltuieli = get_data()
    params = (100, 50, 250, datetime.date(2021, 9, 7), 'intretinere')
    c_new = creeaza_cheltuiala(*params)
    new_cheltuieli = adauga(cheltuieli, *params)
    assert len(new_cheltuieli) == len(cheltuieli) + 1

    assert c_new in new_cheltuieli

def test_citire():
    cheltuieli = get_data()
    some_c = cheltuieli[2]
    assert citire(cheltuieli, get_id(some_c)) == some_c
    assert citire(cheltuieli, None) == cheltuieli

def test_modificare():
    cheltuieli = get_data()
    c_modificata = creeaza_cheltuiala(2, 50, 200, datetime.date(2021, 2, 4), 'alte cheltuieli')
    modificata = modificare(cheltuieli, c_modificata)
    assert c_modificata in modificata
    assert c_modificata not in cheltuieli
    assert len(modificata) == len(cheltuieli)

def test_stergere():
    cheltuieli = get_data()
    de_sters = 3
    c_stearsa = citire(cheltuieli, de_sters)
    stearsa = stergere(cheltuieli, de_sters)
    assert c_stearsa not in stearsa
    assert c_stearsa in cheltuieli
    assert len(stearsa) == len(cheltuieli) - 1

