from Domain.cheltuiala import creeaza_cheltuiala, get_nr_ap


def adauga(lista,
           nr_apartament: int, suma, data, tip):
    """
    Adauga o cheltuiala intr-o lista.
    :param lista: lista de cheltuieli
    :param nr_apartament: numarul apartamentului, nenul
    :param suma:suma cheltuielii
    :param data:data cheltuielii
    :param tip:tipul cheltuielii
    :return: o noua lista cu cheltuiala noua adaugata
    """
    cheltuiala = creeaza_cheltuiala(nr_apartament, suma, data, tip)
    return lista + [cheltuiala]
def citire(lista, nr_apartament: int=None):
    """
    Citeste o cheltuiala din "baza de date"
    :param lista: lista de cheltuieli
    :param nr_apartament: numarul ap cheltuielii
    :return: cheltuiala cu nr ap nr_apartament sau lista cu cheltuieli daca nr_apartament=None
    """
    cheltuiala_cu_nr_ap=None
    for cheltuiala in lista:
        if get_nr_ap(cheltuiala) == nr_apartament:
            cheltuiala_cu_nr_ap=cheltuiala

    if cheltuiala_cu_nr_ap:
        return cheltuiala_cu_nr_ap
    return lista

def modificare(lista, new_cheltuiala):
    """
    Modifica o cheltuiala
    :param lista: lista cu cheltuieli
    :param new_cheltuiala: cheltuiala care se va modifica, nr_apartament trebuie sa fie unul existent
    :return: o lista cu cheltuiala modificata
    """
    new_cheltuieli=[]
    for cheltuiala in lista:
        if get_nr_ap(cheltuiala) != get_nr_ap(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)
    return new_cheltuieli

def stergere(lista, nr_apartament: int):
    """
    Sterge o cheltuiala din "baza de date"
    :param lista: lista de cheltuieli
    :param nr_apartament: numarul ap cheltuielii
    :return: o lista de cheltuieli fara cheltuiala cu nr ap nr_apartament
    """
    new_cheltuiala = []
    for cheltuiala in lista:
        if get_nr_ap(cheltuiala) != nr_apartament:
            new_cheltuiala.append(cheltuiala)
    return new_cheltuiala