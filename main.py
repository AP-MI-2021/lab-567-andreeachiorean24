def is_palindrome(n):
    """
    :param n: numar intreg
    :return: True daca numarul este palindrom sau False daca numarul nu este palindrom
    """
    copie = n
    """"
    calculam inversul numarului
    """
    nou = 0
    while (copie > 0):
        """
        extragem ultima cifra
        """
        digit = copie % 10
        nou = nou * 10 + digit
        copie = copie // 10

    """
    comparam numarul nou cu cel original
    """
    if n==nou:
        return True
    return False
def test_is_palindrome():
    assert is_palindrome(121)==True
    assert is_palindrome(234)==False
    assert is_palindrome(565)==True
def get_cmmmc(list):
    lcm = list[0]
    for i in range(1, len(list)):
        """
        alegem numarul mai mare
        """
        if lcm > list[i]:
            max = lcm
        else:
            max= list[i]

        while (True):
            if ((max % lcm == 0) and (max % list[i] == 0)):
                lcm = max
                break
            max += 1

    return lcm
def test_get_cmmmc():
    assert get_cmmmc(2,3)
    assert get_cmmmc(4,7,5)
def isprime(nr):
    """
    determinam daca numarul este prim
    :param nr: nr intreg
    :return: True daca numarul este prim sau False in caz contrar
    """
    if nr < 2:
        return False
    for i in range(2, nr):
        if nr % i == 0:
            return False

    return True
def issuperprime(nr):
    """
    determinam daca numarul este superprim
    :param nr: numar intreg
    :return: True daca numarul este superprime sau False in caz contrar
    """
    while nr > 0:
        if not isprime(nr):
            return False
        nr=nr//10
    return True
def test_is_superprime():
    assert issuperprime(233)==True
    assert issuperprime(237)==False

def main():

    while True:
        print('1.Verificam daca numarul este palindrom')
        print('2.Calculam cmmmc')
        print('3.Determinam daca numarul este superprim')
        print('4.Iesire')
        optiune=input('Alegeti o optiune')
        if optiune=='1':
            """
               citim un numar de la tastatura
               """
            n = int(input("Enter any number : "))
            if (is_palindrome(n)):
                print("True " + str(n)
                      )
            else:
                print("False")
        elif optiune=='2':
            """
                introducem numarul de numere
                """
            nr = int(input("Enter number of elements : "))

            """
            am creat o lista
            """
            lst = []

            for i in range(0, nr):
                element = int(input())
                """
                adaugam elementul
                """
                lst.append(element)

            # print the list
            print(lst)

            cmmmc = get_cmmmc(lst)
            print("Cel mai mic multiplu comun este: " + str(cmmmc))
        elif optiune=='3':
            nr2 = int(input("Introduceti numar: "))
            print(issuperprime(nr2))
        elif optiune=='4':
            break
        else:
            print("Optiune gresita")

test_is_palindrome()
test_is_superprime()
test_is_superprime()
if __name__ == '__main__':
    main()