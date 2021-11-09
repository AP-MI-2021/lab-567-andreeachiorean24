from Domain.cheltuiala import get_suma, get_data, get_nr_ap


def sume_pt_ap(lista):
    """
    Afișarea sumelor lunare pentru fiecare apartament.
    :param lista:o lista de cheltuieli
    :return:un dictionar cu sumele afisate lunar pt fiecare ap
    """
    new = {}
    for cheltuiala in lista:
        data = get_data(cheltuiala)
        luna = data.month
        if luna in new:
            new[luna].append(get_suma(cheltuiala))
        else:
            new[luna] = []
            new[luna].append(get_suma(cheltuiala))
    return new


