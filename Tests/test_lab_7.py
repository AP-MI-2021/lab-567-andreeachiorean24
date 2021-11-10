from Logic.crud import adauga
from Logic.undo_redo import do_undo, do_redo


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
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 1
    cheltuieli = adauga(cheltuieli, 4, 6, 266, 2021-4-6, 'alte cheltuieli', undo_list, redo_list)
    assert do_redo(undo_list, redo_list, cheltuieli) is None
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 1
    cheltuieli = do_undo(undo_list, redo_list, cheltuieli)
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    cheltuieli = do_redo(undo_list, redo_list, cheltuieli)
    assert len(cheltuieli) == 2
    assert do_redo(undo_list, redo_list, cheltuieli) is None







