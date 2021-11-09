import datetime

from Domain.cheltuiala import get_nr_ap, get_suma, get_tip, creeaza_cheltuiala
from Logic.adunarea_unei_val_pt_data import adunare_val
from Logic.crud import adauga
from Logic.det_cea_mai_mare_chelt import mare_cheltuiala
from Logic.ord_desc_dupa_suma import ord_desc
from Logic.stergerea_cheltuieliilor import sterge_cheltuieli
from Logic.sume_lunare_pt_ap import sume_pt_ap
from Logic.undo_redo import do_undo, do_redo
from Tests.test_crud import get_data

def test_stergerea_cheltuieliilor():
    nr_apartament = 4
    cheltuieli = get_data()
    new_lista = sterge_cheltuieli(nr_apartament, cheltuieli, [], [])
    assert len(new_lista) == len(cheltuieli) - 1

    try:
        ap_gresit = 7
        new_lista = sterge_cheltuieli(ap_gresit, cheltuieli, [], [])
        assert False
    except ValueError:
        assert True


def test_adunarea_unei_val():
    cheltuieli = get_data()
    data = datetime.date(2021, 9, 5)
    valoare = 50
    new_lista = adunare_val(cheltuieli, data, valoare, [], [])
    assert len(new_lista) == len(cheltuieli)
    try:
        data_gresita = datetime.date(2020, 9, 7)
        new_lista = adunare_val(cheltuieli, data_gresita, valoare, [], [])
        assert False
    except ValueError:
        assert True

def test_mare_cheltuiala():
    cheltuieli = get_data()
    new = mare_cheltuiala(cheltuieli)
    assert len(new) == 2
    assert get_suma(new['canal']) == 120
    assert get_suma(new['alte cheltuieli']) == 200
def test_ord_desc():
    cheltuieli = get_data()
    new = ord_desc(cheltuieli, [], [])
    assert len(new) == len(cheltuieli)
    assert get_suma(new[0]) == 200
    assert get_suma(new[2]) == 100

def test_sume_pt_ap():
    cheltuieli = get_data()
    new_s = sume_pt_ap(cheltuieli)
    new = {}
    new[9] = [100]
    new[5] = [120, 200]
    assert len(new) == len(new_s)

def test_undo_redo():
    cheltuieli = get_data()
    params = creeaza_cheltuiala(8, 3, 40, datetime.date(2021, 3, 5), 'canal')
    undo_list = []
    redo_list = []
    new = adauga(cheltuieli, *params, undo_list, redo_list)
    new = do_undo(undo_list, redo_list, new)
    assert new == cheltuieli
    new = do_undo(undo_list, redo_list, new)
    assert new == None
    new = do_redo(undo_list, redo_list, new)
    assert len(new) == len(cheltuieli) + 1