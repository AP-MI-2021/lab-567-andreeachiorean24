import datetime

from Domain.cheltuiala import get_nr_ap, get_suma, get_tip
from Logic.adunarea_unei_val_pt_data import adunare_val
from Logic.crud import adauga
from Logic.stergerea_cheltuieliilor import sterge_cheltuieli
from Tests.test_crud import get_data

def test_stergerea_cheltuieliilor():
    nr_apartament = 4
    cheltuieli = get_data()
    new_lista = sterge_cheltuieli(nr_apartament, cheltuieli)
    assert len(new_lista) == len(cheltuieli) - 1

    try:
        ap_gresit = 7
        new_lista = sterge_cheltuieli(ap_gresit, cheltuieli)
        assert False
    except ValueError:
        assert True


def test_adunarea_unei_val():
    cheltuieli = get_data()
    data = datetime.date(2021, 9, 5)
    valoare = 50
    new_lista = adunare_val(cheltuieli, data, valoare)
    assert len(new_lista) == len(cheltuieli)
    try:
        data_gresita = datetime.date(2020, 9, 7)
        new_lista = adunare_val(cheltuieli, data_gresita, valoare)
        assert False
    except ValueError:
        assert True