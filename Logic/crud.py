from Domain.cheltuiala import creeaza_cheltuiala, get_nr_ap, get_id


def adauga(lista,
           id_cheltuiala:int, nr_apartament, suma, data, tip,
           undo_list: list, redo_list: list):
    """
    Adauga o cheltuiala intr-o lista.
    :param lista: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii
    :param nr_apartament: numarul apartamentului, nenul
    :param suma:suma cheltuielii
    :param data:data cheltuielii
    :param tip:tipul cheltuielii
    :param undo_list:
    :param redo_list:
    :return: o noua lista cu cheltuiala noua adaugata
    """
    if citire(lista, id_cheltuiala) is not None:
        raise ValueError(f'Exista deja o cheltuiala cu id-ul {id_cheltuiala}')

    cheltuiala = creeaza_cheltuiala(id_cheltuiala, nr_apartament, suma, data, tip)

    undo_list.append(lista)
    redo_list.clear()

    return lista + [cheltuiala]
def citire(lista, id_cheltuiala:int =None):
    """
    Citeste o cheltuiala din "baza de date"
    :param lista: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii
    :param nr_apartament: numarul ap cheltuielii
    :return: -cheltuiala cu id-ul id_cheltuiala
             -lista cu cheltuieli daca id_cheltuiala=None
             -None, daca nu exista o cheltuiala cu id_cheltuiala
    """
    if not id_cheltuiala:
        return lista
    cheltuiala_cu_id=None
    for cheltuiala in lista:
        if get_id(cheltuiala) == id_cheltuiala:
            cheltuiala_cu_id=cheltuiala

    if cheltuiala_cu_id:
        return cheltuiala_cu_id
    return None


def modificare(lista, new_cheltuiala, undo_list, redo_list):
    """
    Modifica o cheltuiala
    :param lista: lista cu cheltuieli
    :param new_cheltuiala: cheltuiala care se va modifica, nr_apartament trebuie sa fie unul existent
    :param undo_list:
    :param redo_list:
    :return: o lista cu cheltuiala modificata
    """
    if citire(lista, get_id(new_cheltuiala)) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {get_id(new_cheltuiala)} pe care sa o actualizam')
    new_cheltuieli=[]
    for cheltuiala in lista:
        if get_id(cheltuiala) != get_id(new_cheltuiala):
            new_cheltuieli.append(cheltuiala)
        else:
            new_cheltuieli.append(new_cheltuiala)

    undo_list.append(lista)
    redo_list.clear()

    return new_cheltuieli

def stergere(lista, id_cheltuiala:int, undo_list, redo_list):
    """
    Sterge o cheltuiala din "baza de date"
    :param lista: lista de cheltuieli
    :param id_cheltuiala: id-ul cheltuielii
    :param nr_apartament: numarul ap cheltuielii
    :param undo_list:
    :param redo_list:
    :return: o lista de cheltuieli fara cheltuiala cu nr ap nr_apartament
    """
    if citire(lista, id_cheltuiala) is None:
        raise ValueError(f'Nu exista o cheltuiala cu id-ul {id_cheltuiala} pe care sa o stergem')
    new_cheltuiala = []
    for cheltuiala in lista:
        if get_id(cheltuiala) != id_cheltuiala:
            new_cheltuiala.append(cheltuiala)

    undo_list.append(lista)
    redo_list.clear()

    return new_cheltuiala