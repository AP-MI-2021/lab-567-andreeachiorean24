from Domain.cheltuiala import get_suma, get_tip


def mare_cheltuiala(lista):
    """
     Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială.
    :param lista:lista de cheltuieli
    :return:dictionarul cu cea mai mare cheltuiala pt fiecare tip
    """
    new={}
    for cheltuiala in lista:
        tip = get_tip(cheltuiala)
        suma = get_suma(cheltuiala)
        if tip in new:
            if suma > get_suma(new[tip]):
                new[tip] = cheltuiala
        else:
            new[tip] = cheltuiala
    return new







