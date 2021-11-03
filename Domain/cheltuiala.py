def creeaza_cheltuiala(id_cheltuiala:int, nr_apartament, suma, data, tip):
    """
    Creeaza un dictionar cu o cheltuiala
    :param id_cheltuiala:id-ul cheltuielii, unic
    :param nr_apartament:numarul apartamentului, nenul
    :param suma:suma cheltuielii
    :param data:data cheltuielii
    :param tip:tipul cheltuielii
    :return:o cheltuiala
    """
    return[
        id_cheltuiala,
        nr_apartament,
        suma,
        data,
        tip,
    ]
def get_id(cheltuiala):
    """
    Getter pt id-ul cheltuielii
    :param cheltuiala: cheltuiala
    :return:id-ul dat ca parametru
    """
    return cheltuiala[0]
def get_nr_ap(cheltuiala):
    """
    Getter pt nr apartamentului
    :param cheltuiala: cheltuiala
    :return: nr apartamentului dat ca parametru
    """
    return cheltuiala[1]
def get_suma(cheltuiala):
    """
    Getter pt suma cheltuielii
    :param cheltuiala:  cheltuiala
    :return: suma cheltuielii data ca parametru
    """
    return cheltuiala[2]
def get_data(cheltuiala):
    """
    Getter pt data cheltuielii
    :param cheltuiala: cheltuiala
    :return: data cheltuielii data ca parametru
    """
    return cheltuiala[3]

def get_tip(cheltuiala):
    """
    Getter pt tipul cheltuielii
    :param cheltuiala: cheltuiala
    :return: tipul cheltuielii dat ca parametru: intretinere, canal, alte cheltuieli
    """
    return cheltuiala[4]

def get_str(cheltuiala):
    return  f'cheltuiala cu id-ul {get_id(cheltuiala)}, din apartamentu {get_nr_ap(cheltuiala)}, cu suma de {get_suma(cheltuiala)}, din data de {get_data(cheltuiala)}, tipul {get_tip(cheltuiala)}'