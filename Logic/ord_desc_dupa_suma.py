from Domain.cheltuiala import get_suma


def ord_desc(lista, undo_list, redo_list):
    """
     Ordonarea cheltuielilor descrescător după sumă. 
    :param lista: lista cu cheltuieli
    :param undo_list: Lista de liste de cheltuieli, modificata in urma apelarii fiecarei functionalitati
    :param redo_list: Lista de liste, modificata in urma apelarii fiecarei Undo, sau devine lista vida cand apelam o alta functionalitate
    :return: lista ordonata descrescator
    """
    undo_list.append(lista)
    redo_list.clear()

    return sorted(lista, key= get_suma, reverse=True)
