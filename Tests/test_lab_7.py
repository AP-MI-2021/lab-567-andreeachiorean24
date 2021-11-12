from datetime import datetime, date

from Domain.cheltuiala import get_suma
from Logic.adunarea_unei_val_pt_data import adunare_val
from Logic.crud import adauga
from Logic.ord_desc_dupa_suma import ord_desc
from Logic.stergerea_cheltuieliilor import sterge_cheltuieli
from Logic.undo_redo import do_undo, do_redo
from Tests.test_crud import get_data


def test_lab_7():
    cheltuieli = []
    undo_list = []
    redo_list = []
    cheltuieli = adauga(cheltuieli, 1, 5, 400, 2021-3-3, 'canal', undo_list, redo_list)
    cheltuieli = adauga(cheltuieli, 2, 6, 34, 2021-3-5, 'alte cheltuieli', undo_list, redo_list)
    cheltuieli = adauga(cheltuieli, 3, 8, 234, 2021-3-7, 'canal', undo_list, redo_list)
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 2
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 1
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 0
    assert do_undo(undo_list, redo_list, cheltuieli) is None
    assert len(cheltuieli) == 0
    cheltuieli = adauga(cheltuieli, 1, 4, 423, 2021-2-3, 'canal', undo_list, redo_list)
    cheltuieli = adauga(cheltuieli, 2, 6, 344, 2021-7-5, 'alte cheltuieli', undo_list, redo_list)
    cheltuieli = adauga(cheltuieli, 3, 2, 266, 2021-5-5, 'alte cheltuieli', undo_list, redo_list)
    assert do_redo(undo_list, redo_list, cheltuieli) is None
    assert len(cheltuieli) == 3
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 2
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 1
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 2
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 3
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 2
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 1
    cheltuieli = adauga(cheltuieli, 4, 6, 266, 2021-4-6, 'alte cheltuieli', undo_list, redo_list)
    assert do_redo(undo_list, redo_list, cheltuieli) is None
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 1
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 0
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 1
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 2
    assert do_redo(undo_list, redo_list, cheltuieli) is None

def test_stergerea_cheltuieliilor_undo_redo():
    cheltuieli = get_data()
    undo_list = []
    redo_list = []
    cheltuieli = sterge_cheltuieli(5, cheltuieli, undo_list, redo_list)
    assert len(cheltuieli) == 2
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 3
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 2
    assert do_redo(undo_list, redo_list, cheltuieli) is None

def test_adunare_val_undo_redo():
    cheltuieli = get_data()
    undo_list = []
    redo_list = []
    cheltuieli = adunare_val(cheltuieli, date(2021, 9, 5), 50, undo_list, redo_list)
    assert get_suma(cheltuieli[0]) == 150
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert get_suma(cheltuieli[0]) == 100
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    assert get_suma(cheltuieli[0]) == 150
    assert do_redo(undo_list, redo_list, cheltuieli) is None

def test_ord_desc_undo_redo():
    cheltuieli = get_data()
    undo_list = []
    redo_list = []
    cheltuieli = ord_desc(cheltuieli, undo_list, redo_list)
    assert get_suma(cheltuieli[0]) == 200
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert get_suma(cheltuieli[0]) == 100
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    assert get_suma(cheltuieli[0]) == 200
    assert do_redo(undo_list, redo_list, cheltuieli) is None









