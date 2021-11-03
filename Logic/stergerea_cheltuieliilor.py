from Domain.cheltuiala import get_nr_ap


def sterge_cheltuieli(nr_apartament, lista):
    """
    Ștergerea tuturor cheltuielilor pentru un apartament dat
    :param nr_apartament: nr ap care se sterge
    :param lista: lista de cheltuieli
    :return:lista in care cheltuielile apartamentului dat s-au sters
    """
    new=[]
    for cheltuiala in lista:
        if get_nr_ap(cheltuiala) != nr_apartament:
            new.append(cheltuiala)

    if len(new) == len(lista):
        raise ValueError('Nu exista numarul de ap')
    return new