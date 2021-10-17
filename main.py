
def factorial(n: int) -> int:
    """Calculeaza si returneaza factorialul unui numar """
    fact=1
    for i in range(1,n+1):
        fact*=i

    return fact


def get_n_choose_k(n: int, k: int) -> int:
    """Calculeaza combinari de n luate cate k """
    return (factorial(n)/(factorial(k) * factorial(n-k)))


def test_get_n_choose_k():
    """Testeaza functia get_n_choose_k
    """
    assert get_n_choose_k(10, 0) == 1.0
    assert get_n_choose_k(5,1) == 5.0
    assert get_n_choose_k(5,4) == 5.0
    assert get_n_choose_k(5, 4) == get_n_choose_k(5,1)
    assert get_n_choose_k(7,2) == get_n_choose_k(7,5)

def input_get_n_choose_k():
    print("Functia calculeaza combinari de n luate cate k.")
    n = int(input("n="))
    k = int(input("k="))
    print(f"Exista {get_n_choose_k(n, k)} combinari de {n} luate cate {k}.")


def is_palindrome(n : int) -> bool:
    """Verifica daca numarul dat este un palindrom"""
    oglindit = 0
    lungime = len(str(n))

    for i in range(lungime // 2):
        oglindit*=10
        oglindit+=n%10
        n//=10

    if lungime % 2 == 1:
        n//=10

    return n == oglindit


def test_is_palidnrome():
    """Testeaza is_palindrome
    """
    assert is_palindrome(1234321) == True
    assert is_palindrome(52525) == True
    assert is_palindrome(1234) == False
    assert is_palindrome(5) == True
    assert is_palindrome(101) == True


test_get_n_choose_k()
test_is_palidnrome()
