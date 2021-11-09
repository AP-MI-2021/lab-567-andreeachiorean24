from Domain.cheltuiala import get_suma


def ord_desc(lista, undo_list, redo_list):
    """
     Ordonarea cheltuielilor descrescător după sumă. 
    :param lista: lista cu cheltuieli
    :return: lista ordonata descrescator
    """
    undo_list.append(lista)
    redo_list.clear()
    return sorted(lista, key= get_suma, reverse=True)
