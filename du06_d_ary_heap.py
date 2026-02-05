#!/usr/bin/env python3

# Povolené knihovny: typing, math

# IB002 Domácí úloha 6
#
# Pojem binární haldy, který znáte z přednášky, je možno zobecnit pro
# libovolnou aritu (maximální počet potomků každého vrcholu) d, kde d ≥ 2.
# Tomuto zobecnění říkáme d-ární halda.
#
# Podobně jako binární haldy, i obecné d-ární haldy se dají reprezentovat
# pomocí pole – prvky jsou v něm uloženy „po patrech“.
#
# Příklad minimové 3-ární haldy:
#       2
#     / | \
#    4  7  3
#   /|
#  5 6
# Její reprezentace polem je [2, 4, 7, 3, 5, 6].
#
# V tomto úkolu se budeme zabývat minimovými d-árními haldami s různými
# aritami. Pro stručnost budeme používat jen pojem „halda“.
#
# Do definice třídy DMinHeap nijak nezasahujte.


class DMinHeap:
    """Třída DMinHeap reprezentuje minimovou d-ární haldu.

    Atributy:
        array   pole prvků haldy
        arity   arita haldy (maximální počet potomků každého vrcholu)
    """
    __slots__ = "array", "arity"

    def __init__(self, array: list[int], arity: int):
        self.array = array
        self.arity = arity


# Část 1.
# Implementujte funkci is_correct, která ověří, zda je zadaná halda korektní,
# tj. zda splňuje haldovou podmínku.

def is_correct(heap: DMinHeap) -> bool:
    """
    vstup: ‹heap› – objekt typu DMinHeap
    výstup: ‹True›, pokud prvky ‹heap› splňují haldovou podmínku
            ‹False› jinak
            Funkce nijak nemodifikuje zadaný vstup.
    časová složitost: O(n), kde n je počet prvků v ‹heap.array›
        (Všimněte si, že složitost nesmí nijak záviset na aritě haldy!)
    extra prostorová složitosti: O(1)
        (Do extra prostorové složitost nepočítáme velikost vstupu, ale
         počítáme do ní zásobník rekurze.)

    Příklady:
    Halda DMinHeap([1, 2, 3, 2, 1, 2, 3, 2], 4) je korektní.
    Halda DMinHeap([1, 2, 3, 2, 1, 2, 3, 2], 2) není korektní.
    Halda DMinHeap([1, 2, 3, 4, 2, 3, 4, 4, 4, 5, 4, 5, 3], 3) není korektní.
    Halda DMinHeap([1, 2, 3, 4, 2, 3, 4, 4, 4, 5, 4, 5, 3], 2) je korektní.
    """
    pass  # TODO


# Část 2.
# Implementujte funkci heapify, která opraví haldu směrem dolů od zadaného
# indexu.
def heapify(heap: DMinHeap, index: int) -> None:
    """
    vstup: ‹heap›   objekt typu DMinHeap
           ‹index›  celé číslo; 0 ≤ index < len(heap.array)
                    zadaná halda je korektní od prvku na zadaném
                    indexu směrem dolů, vyjma tohoto prvku samotného
    výstup: funkce opraví haldu směrem dolů od zadaného prvku tak,
            aby tato část haldy byla korektní včetně zadaného prvku;
            prvky, které jsou mimo tuto část haldy (tj. nejsou ani nepřímými
            potomky prvku na zadaném indexu), funkce nijak nemění
    časová složitost: O(d · h), kde d je arita haldy a h je výška podstromu
        začínajícího v zadaném prvku
    extra prostorová složitost: O(h)

    Příklady:
    Máme-li objekt DMinHeap([5, 1, 2, 3, 4], 2) a zavoláme-li heapify
    s indexem 0, pak výsledná halda může mít například tvar [1, 3, 2, 5, 4].

    Máme-li objekt DMinHeap([7, 4, 1, 5, 6, 8, 9, 3, 2, 0, 2, 2], 3)
    a zavoláme-li heapify s indexem 2, pak výsledná halda může mít například
    tvar [7, 4, 0, 5, 6, 8, 9, 3, 2, 1, 2, 2].
    """
    pass  # TODO


# Část 3.
# Implementujte funkci change_arity, která změní aritu haldy a přeskládá
# prvky tak, aby halda zůstala korektní.
#
# Pro testování korektnosti svého přístupu můžete s výhodou použít funkci
# z části 1.

def change_arity(heap: DMinHeap, new_arity: int) -> None:
    """
    vstup: ‹heap›      korektní halda
           ‹new_arity› nová arita; celé číslo ≥ 2
    výstup: žádný; funkce nastaví atribut ‹heap.arity› na hodnotu ‹new_arity›
            a přeskládá prvky v haldě tak, aby byla korektní vzhledem k nové
            aritě
    časová složitost: O(n), kde n je počet prvků haldy
    extra prostorová složitost: O(log n)
    """
    pass  # TODO


# Část 4.
# Implementujte funkci min_three, která vrátí trojici nejmenších prvků haldy.

def min_three(heap: DMinHeap) -> tuple[int, int, int]:
    """
    vstup: ‹heap›  korektní halda; len(heap.array) ≥ 3
    výstup: trojice nejmenších prvků haldy, vzestupně seřazená
            Funkce nijak nemodifikuje zadaný vstup.
    časová složitost: O(d), kde d je arita haldy
    extra prostorová složitost: O(1)

    Příklady:
    Pro vstup DMinHeap([1, 2, 4, 3, 4, 5, 6, 4, 7], 2) má být výstupem
    trojice (1, 2, 3).
    Pro vstup DMinHeap([1, 3, 3, 2, 4, 4, 4, 5, 5, 5, 6, 6, 2], 3) má
    být výstupem trojice (1, 2, 2).
    Pro vstup DMinHeap([1, 1, 1], 42) má být výstupem trojice (1, 1, 1).
    """
    pass  # TODO
