from Domain.cheltuiala import get_suma


def ord_desc(lista):
    """
     Ordonarea cheltuielilor descrescător după sumă. 
    :param lista: lista cu cheltuieli
    :return: lista ordonata descrescator
    """
    return sorted(lista, key= get_suma, reverse=True)
