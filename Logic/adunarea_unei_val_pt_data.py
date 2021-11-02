from Domain.cheltuiala import get_data, get_suma, get_id, get_nr_ap, get_tip, creeaza_cheltuiala


def adunare_val(lista, data, valoare):
    """
     Adunarea unei valori la toate cheltuielile dintr-o dată citită.
    :param lista: lista cu cheltuieli
    :param data:data citita
    :param valoare:valoarea care se adauga
    :return:lista noua la care s a adaugat valoarea
    """
    verificare=False
    if valoare<0:
        raise ValueError('Valoarea trebuie sa fie un nr pozitiv')
    new_list=[]
    for cheltuiala in lista:
        if get_data(cheltuiala)== data:
            verificare = True
            suma_noua=get_suma(cheltuiala) + valoare
            id = get_id(cheltuiala)
            nr_ap = get_nr_ap(cheltuiala)
            tip = get_tip(cheltuiala)
            new_list.append(creeaza_cheltuiala(id, nr_ap, suma_noua, data, tip))
        else:
            new_list.append(cheltuiala)
    if verificare == False:
        raise ValueError('Nu exista data citita')
    return new_list
