def are_alternating_signs(lst: list[int]) -> bool:
    """
        verifica daca toate elementele unei lista au semne alternative
    :param lst: lista de nr
    :return: bool: true daca toate elementele listei au semne alternative, false contrar
    """
    if len(lst) > 0:
        semn_anterior = not (lst[0] >= 0)

    for x in lst:
        semn = (x >= 0)
        if semn == semn_anterior:
            return False
        semn_anterior = semn

    return True


def test_are_alternating_signs():
    assert are_alternating_signs([-1, 12, -2, 7]) == True
    assert are_alternating_signs([]) == True
    assert are_alternating_signs([3, 2 , -1 , 5]) == False
    assert are_alternating_signs([5]) == True


def get_longest_alternating_signs(lst: list[int]) -> list[int]:
    """
        determina cea mai lunga secventa de nr cu semn alternativ
    :param lst: lista de nr
    :return: cea mai lunga secventa de nr cu semn alternativ
    """
    subsecventaMax = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if are_alternating_signs(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = lst[i:j + 1]
    return subsecventaMax


def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([-1, 4, 7, -2, -7, 1, 17, -1, 8, -9]) == [17, -1, 8, -9]
    assert get_longest_alternating_signs([]) == []
    assert get_longest_alternating_signs([5]) == [5]
    assert get_longest_alternating_signs([47, -52, -31, -47, 21, -3, 1, -5]) == [-47, 21, -3, 1, -5]


def isprime(x):
    """
     determina daca un nr. este prim
     :param x: un numar intreg
     :return: True, daca x este prim sau False in caz contrar
     """
    if x >= 2:
        for i in range(2, x//2 + 1):
            if x % i == 0:
                return False
        return True
    return False


def testIsPrime():
    assert isprime(-1) is False
    assert isprime(0) is False
    assert isprime(1) is False
    assert isprime(2) is True
    assert isprime(3) is True
    assert isprime(4) is False
    assert isprime(5) is True


def only_prime_digits(n: int) -> bool:
    """verifica daca un numar are toate cifrele prime
    Args:
        n (int): Numarul verificat
    Returns:
        bool: True daca are toate cifrele prime, False in caz contrar
    """
    while n:
        if not isprime(n % 10):
            return False
        n //= 10

    return True


def test_only_prime_digits():
    assert only_prime_digits(553) == True
    assert only_prime_digits(28) == False
    assert only_prime_digits(0) == True
    assert only_prime_digits(2795) == False


def are_list_prime_digits(lst: list[int]) -> bool:
     """Verifica daca toate numerele unei liste sunt formate din cifre prime
       Args:
           lst (list[int]): Lista verificata
       Returns:
          bool: True daca toate numerele au toate cifrele prime, False in caz contrar
     """
     for x in lst:
           if not only_prime_digits(x):
               return False

     return True


def test_are_list_prime_digits():
    assert are_list_prime_digits([557, 23, 752]) == True
    assert are_list_prime_digits([28, 49, 51, 23]) == False


def get_longest_prime_digits(lst: list[int]) -> list[int]:
    """Returneaza cea mai lunga subsecventa in care nr sunt formate din cifre prime
        Args:
            lst (list[int]): Lista de nr
        Returns:
            list[int]: Subsecventa
        """
    subsecventaMax2 = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if are_list_prime_digits(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMax2):
                subsecventaMax2 = lst[i:j + 1]
    return subsecventaMax2


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([41,98,333,27,53,72, 45, 81]) == [333,27,53,72]
    assert get_longest_prime_digits([41,82,53,98,62]) == [53]


def are_numbers_prime(lst: list[int]) -> bool:
    """Verifica daca o lista este formata doar din numere prime
    Args:
        lst (list[int]): Lista verificata
    Returns:
        bool: True daca toate numerele din lista sunt prime, False in caz contrar
    """
    for x in lst:
        if not isprime(x):
            return False

    return True


def test_are_numbers_prime():
    assert are_numbers_prime([1,2,5,6]) == False
    assert are_numbers_prime([17, 13, 2, 7]) == True
    assert are_numbers_prime([]) == True
    assert are_numbers_prime([97]) == True


def citireLista():
    lst = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        lst.append(int(input("l[" + str(i) + "]=")))
    return lst


def printMenu():
    print("1. Citire lista")
    print("2. Determinare cea mai lungă subsecvență cu prop. ca numerele au semne alternante")
    print("3. Determinare cea mai lungă subsecvență cu prop. ca toate numerele sunt formate din cifre prime")
    print("4. Determinare cea mai lungă subsecvență cu prop. ca toate numerele sunt prime")
    print("5. Iesire")


def main():
    test_get_longest_alternating_signs()
    test_are_alternating_signs()
    test_only_prime_digits()
    test_get_longest_alternating_signs()
    test_are_list_prime_digits()
    test_get_longest_prime_digits()
    testIsPrime()
    test_are_numbers_prime()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citireLista()
        elif optiune == "2":
            print(get_longest_alternating_signs(lst))
        elif optiune == "3":
            print(get_longest_prime_digits(lst))
        elif optiune == "4":
            print(are_numbers_prime(lst))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Reincercati!")

main()