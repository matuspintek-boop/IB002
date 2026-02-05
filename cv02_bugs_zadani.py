#!/usr/bin/env python3


from typing import Any


# Tento program obsahuje velke mnozstvi chyb ruznych typu.
#
# Vasim ukolem je projit kod a opravit jej tak,
# abyste vsechny chyby odstranili.
#
# Testy nemodifikujte, jsou jen pro kontrolu a to, ze vsechny
# projdou neznamena, ze je vas kod bez chyby.
#
# Opravujte jen funkce, ktere maji v komentari TODO.


# TODO: opravit tuto funkci
def is_string_palindrom(string: str) -> bool:
    """Testuje, zdali je zadany retezec (string) palindrom
    a to bez pouziti funkce reverse. Vraci True v pripade,
    ze je palindrom, jinak False.
    """
    if string is None:
        return False

    i = 0
    while i <= len(string):
        if string[i] == string[len(string) - i]:
            continue
        else:
            return False
    return True


class Node:
    """Trida Node slouzi pro reprezentaci objektu v jednosmerne
    spojovanem seznamu.

    Atributy:
        value   reprezentuje ulozenou hodnotu/objekt
        next    reference na nasledujici prvek v seznamu
    """

    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Node | None = None


class LinkedList:
    """Trida LinkedList reprezentuje spojovany seznam.

    Atributy:
        first   reference na prvni prvek seznamu
    """

    def __init__(self) -> None:
        self.first: Node | None = None


# TODO: opravit tuto funkci
def insert(linked_list: LinkedList, value: Any) -> Node:
    """Funkce insert vklada na konec seznamu (linked_list) novy uzel
    s danou hodnotou (value). Vraci referenci na novy uzel seznamu.
    """
    node = Node(value)

    tmp = linked_list.first.next
    while tmp is not None:
        tmp = tmp.next

    if linked_list.first is None:
        linked_list.first = node
    else:
        tmp.next = node

    return node


# TODO: opravit tuto funkci
def delete_key(linked_list: LinkedList, key: Any) -> bool:
    """Funkce delete_key smaze prvni vyskyt klice (key) v seznamu
    (linked_list). Vrati False pokud klic nebyl nalezen, True jinak.
    """
    node = linked_list.first

    while node.next is not None:
        node = node.next
        previous = node
        if node.value == key:
            break

    if node is None:
        return False

    previous.next = node

    return True


# TODO: opravit tuto funkci
def multiply_numbers(bound: int, numbers: list[int]) -> int:
    """Funkce vypocita soucin cisel v poli numbers, jejichz hodnota
    je z intervalu 1 az bound (vcetne). Pokud se v poli zadna takova
    cisla nenachazeji, vrati 1.

    Parametry:
        bound   horni hranice intervalu pro hodnotu cisel,
                ktera se zapocitavaji do vysledku
        numbers pole cisel k pocitani soucinu
    """
    array = [0 for i in range(bound)]
    for i in range(len(numbers)):
        array[numbers[i]] += 1
    val = 1
    for i in range(len(array)):
        for j in range(array[i]):
            val *= i
    return val


# TODO: opravit tuto funkci
def has_correct_parentheses(string: str) -> bool:
    """Funkce otestuje, zdali zadany retezec obsahuje spravne
    ozavorkovani, tedy pred kazdou uzaviraci zavorkou musi byt prislusna
    oteviraci. Resi se pouze zavorky ( ). Vraci True v pripade spravneho
    ozavorkovani, jinak False.
    """
    opened = 0
    for i in range(len(string)):
        if string[i] == '(':
            opened += 1
        if string[i] == ')':
            opened -= 1
        if opened == 0:
            return True

    return False


# TODO: opravit tuto funkci
def sequence_sum(sequence: list[int]) -> int:
    """Funkce secte "sumu" posloupnosti (sequence) a to tak, ze pokud je
    cislo vetsi nez predchazejici (sequence[n] > sequence[n-1]), tak ho
    pricte k "sume", pokud je sequence[n] < sequence[n-1], tak ho odecte
    a pokud je stejne, tak ho preskoci. Prvni cislo se nezapocita.
    """
    strange_sum = 0
    for i in range(len(sequence)):
        if sequence[i] > sequence[i - 1]:
            strange_sum += sequence[i]
        if sequence[i] < sequence[i - 1]:
            strange_sum -= sequence[i]
    return strange_sum


# TODO: opravit tuto funkci
def find_substring(string: str, substring: str) -> int:
    """Funkce hleda podretezec (substring) v retezci (string).
    Pokud se podretezec v retezci nachazi, vrati index prvniho vyskytu.
    Jinak vraci -1.
    """
    if len(substring) > len(string):
        return -1

    j = 1
    i = 1
    while i < len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return i - j
            j += 1
    i += 1
    return -1


# Testy implementace
def test_palindrom() -> None:
    print("Test 1: je \"abccba\" palindrom?")
    try:
        res = is_string_palindrom("abccba")
        if res:
            print("OK.")
        else:
            print("NOK, \"abccba\" je palindrom, ale program vraci False.")
    except IndexError as exc:
        print("NOK: pristup mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 2: je \"abcba\" palindrom?")
    try:
        res = is_string_palindrom("abcba")
        if res:
            print("OK.")
        else:
            print("NOK, \"abcba\" je palindrom, ale program vraci False.")
    except IndexError as exc:
        print("NOK: pristup mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 3: je \"abcabc\" palindrom?")
    try:
        res = is_string_palindrom("abcabc")
        if res:
            print("NOK, \"abcabc\" neni palindrom, ale program vraci True.")
        else:
            print("OK.")
    except IndexError as exc:
        print("NOK: pristup mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))


def test_list() -> None:
    try:
        list1 = LinkedList()
        list1.first = None
        print("Test 4: vkladani 1. prvku do listu.")
        tmp1 = insert(list1, 1)
        if tmp1.value == 1 and list1.first == tmp1 and tmp1.next is None:
            print("OK.")
        else:
            print("NOK, vlozeni prvniho prvku neprobehlo v poradku,",
                  "zkontrolujte, zdali je spravne nastavena hodnota",
                  "a reference next.")
    except AttributeError as exc:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    try:
        print("Test 5: vkladani 2. prvku do listu.")
        list2 = LinkedList()
        tmp21 = insert(list2, 1)
        tmp22 = insert(list2, 2)
        if (tmp22.value == 2 and list2.first == tmp21 and
                tmp22.next is None and tmp21.next == tmp22):
            print("OK.")
        else:
            print("NOK, vlozeni druheho prvku neprobehlo v poradku,",
                  "zkontrolujte, zdali je spravne nastavena hodnota",
                  "a reference next.")
    except AttributeError as exc:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    try:
        print("Test 6.1: odstraneni 2. prvku z listu.")
        list3 = LinkedList()
        tmp3 = insert(list3, 1)
        insert(list3, 2)
        if delete_key(list3, 2) and tmp3.next is None:
            print("OK.")
        else:
            print("NOK, neodstranili jste prvek,",
                  "muze to byt dano i spatnym vkladanim.")
    except AttributeError as exc:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    try:
        print("Test 6.2: odstraneni prvku z prazdneho listu.")
        list3 = LinkedList()
        if delete_key(list3, 2):
            print("NOK, odstranili jste prvek z prazdneho listu",
                  "nebo vratili True")
        else:
            print("OK.")
    except AttributeError as exc:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    try:
        print("Test 6.3: odstraneni chybejiciho prvku z listu.")
        list3 = LinkedList()
        insert(list3, 1)
        insert(list3, 2)
        if delete_key(list3, 4):
            print("NOK, odstranili jste prvek, ktery v listu nebyl",
                  "nebo vratili True")
        else:
            print("OK.")
    except AttributeError as exc:
        print("NOK: spatna prace s pameti.")
        print("Chybova hlaska Pythonu: {}".format(exc))


def test_multiply_numbers() -> None:
    print("Test 7: multiply_numbers(1, [1, 1, 1])")
    try:
        res = multiply_numbers(1, [1, 1, 1])
        if res != 1:
            print("NOK: {} != 1".format(res))
        else:
            print("OK.")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 8: multiply_numbers(2, [3, 3, 3])")
    try:
        res = multiply_numbers(2, [3, 3, 3])
        if res != 1:
            print("NOK: {} != 1".format(res))
        else:
            print("OK.")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 9: multiply_numbers(3, [1, 1, 2])")
    try:
        res = multiply_numbers(3, [1, 1, 2])
        if res != 2:
            print("NOK: {} != 2".format(res))
        else:
            print("OK.")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 10: multiply_numbers(3, [1, 4, 3])")
    try:
        res = multiply_numbers(3, [1, 4, 3])
        if res != 3:
            print("NOK: {} != 3".format(res))
        else:
            print("OK.")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 11: multiply_numbers(4, [3, 3, 3, 2])")
    try:
        res = multiply_numbers(4, [3, 3, 3, 2])
        if res != 54:
            print("NOK: {} != 54".format(res))
        else:
            print("OK.")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 12: multiply_numbers(3, [3, 3, 4])")
    try:
        res = multiply_numbers(3, [3, 3, 4])
        if res != 9:
            print("NOK: {} != 9".format(res))
        else:
            print("OK.")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))


def test_brackets() -> None:
    print("Test 13: zavorkovani na \"()\"")
    try:
        if has_correct_parentheses("()"):
            print("OK.")
        else:
            print("NOK, \"()\" je spravne uzavorkovani a funkce vrati False")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 14: zavorkovani na \")(\"")
    try:
        if has_correct_parentheses(")("):
            print("NOK, \")(\" neni spravne uzavorkovani a funkce vrati True")
        else:
            print("OK.")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 15: zavorkovani na \"aaa\"")
    try:
        if has_correct_parentheses("aaa"):
            print("OK.")
        else:
            print("NOK, \"aaa\" je spravne uzavorkovani a funkce vrati False")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 16: zavorkovani na \"((\"")
    try:
        if has_correct_parentheses("(("):
            print("NOK, \"((\" neni spravne uzavorkovani a funkce vrati True")
        else:
            print("OK.")
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))


def test_sequence_sum() -> None:
    print("Test 17: sequence_sum([1, 2, 3])")
    try:
        res = sequence_sum([1, 2, 3])
        if res == 5:
            print("OK.")
        else:
            print("NOK, sequence_sum([1, 2, 3]) je 5 a vam vyslo", res)
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 18: sequence_sum([1, 2, 1])")
    try:
        res = sequence_sum([1, 2, 1])
        if res == 1:
            print("OK.")
        else:
            print("NOK, sequence_sum([1, 2, 1]) je 1 a vam vyslo", res)
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 18: sequence_sum([1,2,2])")
    try:
        res = sequence_sum([1, 2, 2])
        if res == 2:
            print("OK.")
        else:
            print("NOK, sequence_sum([1, 2, 2]) je 2 a vam vyslo", res)
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))


def test_find() -> None:
    print("Test 19: je v \"abc\" podretezec \"abc\"?")
    try:
        res = find_substring("abc", "abc")
        if res == 0:
            print("OK.")
        else:
            print("NOK, podretezec je na pozici 0, vy vracite", res)
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 20: je v \"abc\" podretezec \"b\"?")
    try:
        res = find_substring("abc", "b")
        if res == 1:
            print("OK.")
        else:
            print("NOK, podretezec je na pozici 1, vy vracite", res)
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 21: je v \"abcb\" podretezec \"abb\"?")
    try:
        res = find_substring("abcb", "abb")
        if res == -1:
            print("OK.")
        else:
            print("NOK, podretezec zde neni, vy vracite", res)
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 22: je v \"ab\" podretezec \"bb\"?")
    try:
        res = find_substring("ab", "bb")
        if res == -1:
            print("OK.")
        else:
            print("NOK, podretezec zde neni, vy vracite", res)
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))

    print("Test 23: je v \"ababcb\" podretezec \"abcb\"?")
    try:
        res = find_substring("ababcb", "abcb")
        if res == 2:
            print("OK.")
        else:
            print("NOK, podretezec je na pozici 2, vy vracite", res)
    except IndexError as exc:
        print("NOK: pristupovani mimo pole.")
        print("Chybova hlaska Pythonu: {}".format(exc))


if __name__ == '__main__':
    test_palindrom()
    test_list()
    test_multiply_numbers()
    test_brackets()
    test_sequence_sum()
    test_find()

    print("Testy netestuji vse. Pokud vam tedy prosly vsude na OK,")
    print("neznamena to, ze mate bezchybnou implementaci. To, ze")
    print("je nejaky test NOK ale znamena, ze mate neco spatne.")
