from Domain.cheltuiala import creeaza_cheltuiala, get_nr_ap, get_id


def adauga(lista,
           id_cheltuiala:int, nr_apartament, suma, data, tip):
    """
    Adauga o cheltuiala intr-o lista.
    :param lista: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii
    :param nr_apartament: numarul apartamentului, nenul
    :param suma:suma cheltuielii
    :param data:data cheltuielii
    :param tip:tipul cheltuielii
    :return: o noua lista cu cheltuiala noua adaugata
    """
    cheltuiala = creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tip)
    return lista + [cheltuiala]
def citire(lista, id_cheltuiala:int =None):
    """
    Citeste o cheltuiala din "baza de date"
    :param lista: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii
    :param nr_apartament: numarul ap cheltuielii
    :return: cheltuiala cu nr ap nr_apartament sau lista cu cheltuieli daca nr_apartament=None
    """
    cheltuiala_cu_id=None
    for cheltuiala in lista:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_cu_id=cheltuiala

    if cheltuiala_cu_id:
        return cheltuiala_cu_id
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
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)
    return new_cheltuieli

def stergere(lista, id_cheltuiala:int):
    """
    Sterge o cheltuiala din "baza de date"
    :param lista: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii
    :param nr_apartament: numarul ap cheltuielii
    :return: o lista de cheltuieli fara cheltuiala cu nr ap nr_apartament
    """
    new_cheltuiala = []
    for cheltuiala in lista:
        if get_id(cheltuiala) != id_cheltuiala:
            new_cheltuiala.append(cheltuiala)
    return new_cheltuiala