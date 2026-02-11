#!/usr/bin/env python3

# Povolené knihovny: typing, math

# IB002 Domácí úloha 3.
#
# Vaším úkolem bude implementovat dvě funkce s využitím principu binárního
# vyhledávání. V obou případech musí být časová složitost vašeho algoritmu
# nejvýše logaritmická, tedy být ve třídě O(log n).
#
# Dejte si dobrý pozor na složitosti operací s Pythonovskými seznamy.
# Nezapomeňte, že slicing s[x:y] vytváří kopii části seznamu a má tedy nutně
# časovou složitost lineární vůči velikosti vytvořené kopie.
#
# Obě zadané funkce musí být čisté, tj. nesmí modifikovat zadaný vstup.
#
# V tomto a dalších úkolech budeme používat pojem „pole“ pro zdůraznění
# skutečnosti, že se k Pythonovským seznamům chováme jako k polím,
# tj. zejména zde nevyužíváme jejich schopnosti se rozšiřovat a zkracovat.
#
# (Pythonovské seznamy jsou ve skutečnosti tzv. dynamická pole, což je
#  komplikovanější datová struktura, která si zachovává některé dobré
#  vlastnosti pole, např. konstantní přístup k libovolnému prvku.)


# Část 1.
# Implementujte funkci partition, která rozdělí zadané seřazené pole na tři
# části: část s prvky menšími než zadaný klíč, část s prvky rovnými zadanému
# klíči a část s prvky většími než zadaný klíč.

def find_first_val(current_index: int, numbers: list[int], val: int) -> int:

    if numbers[current_index] > val:
        return current_index
    step = 1

    while numbers[current_index] < val:
        if current_index + step < len(numbers)\
            and numbers[current_index+step] < val:
            current_index += step
            step *= 2
        elif (current_index + step >= len(numbers) or numbers[current_index+step] >= val)\
            and step == 1:
            return current_index + step
        else:
            step = 1
    assert False

def find_last_val(current_index: int, numbers: list[int], val: int) -> int:
    step = 1

    if current_index >= len(numbers) or numbers[current_index] > val:
        return current_index

    while numbers[current_index] == val:
        if current_index + step < len(numbers)\
            and numbers[current_index + step] == val:
            current_index += step
            step *= 2
        elif (current_index + step >= len(numbers) or numbers[current_index + step] > val)\
            and step == 1:
            return current_index+1
        else:
            step = 1

    assert False

        
def partition(numbers: list[int], key: int) -> tuple[int, int]:
    """
    vstup: ‹numbers› – seřazené pole celých čísel
           ‹key›     – celé číslo
    výstup: dvojice ‹left, right› splňující následující podmínky
        left a right jsou celá čísla v rozsahu od 0 do len(numbers) včetně
        prvky na indexech z intervalu [0, left) jsou menší než ‹key›
        prvky na indexech z intervalu [left, right) jsou rovné ‹key›
        prvky na indexech z intervalu [right, len(numbers)) jsou > ‹key›
        (zápis [a, b) znamená polouzavřený interval, tedy včetně a, ale bez b)
    časová složitost: O(log n), kde n je velikost vstupního pole

    Příklady:
    Pro vstup ([1, 3, 3, 7], 3) funkce vrátí dvojici (1, 3).
    Pro vstup ([1, 3, 3, 7, 17, 42, 69, 420], 11) funkce vrátí dvojici (4, 4).
    """

    if len(numbers) == 0:
        return (0, 0)
    first_index = find_first_val(0, numbers, key) 
    last_index = find_last_val(first_index, numbers, key)

    return (first_index, last_index)



# Část 2.
# Implementujte funkci minimum, která najde minimální hodnotu v poli
# různých čísel s jediným lokálním minimem.

def min_recursive(left_index: int, right_index: int, numbers: list[int]) -> int:
    if right_index - left_index <= 1:
        return min(numbers[left_index], numbers[right_index])
    mid = left_index + (right_index - left_index) // 2

    val = numbers[mid]

    if numbers[mid - 1] < val:
        return min_recursive(left_index, mid - 1, numbers)
    elif numbers[mid+1] < val:
        return min_recursive(mid+1, right_index, numbers)
    return val
    
def minimum(numbers: list[int]) -> int:
    """
    vstup: ‹numbers› – pole vzájemně různých čísel, které obsahuje
                       právě jedno lokální minimum
           lokální minimum definujeme jako prvek pole takový,
           že je menší než jeho sousední prvky (má-li nějaké;
           lokální minimum může být i na kraji pole)
    výstup: hodnota minimálního prvku
    časová složitost: O(log n), kde n je velikost vstupního pole

    Příklady:
    Pro vstup [10, 8, 6, 4, 2, 1, 3, 5, 7, 9] funkce vrátí číslo 1.
    Pro vstup [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] funkce vrátí číslo 0.
    """

    return min_recursive(0, len(numbers) - 1, numbers)

# def test_minimum() -> None:
#     assert minimum([0]) == 0
#     assert minimum([10, 8, 6, 4, 2, 1, 3, 5, 7, 9]) == 1
#     assert minimum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
#     assert minimum([9, 8, 7, 6, 5]) == 5

#     print("minimum passed ALL TESTS")

# def test_partition() -> None:
#     assert partition([], 0) == (0, 0)
#     assert partition([1,2,3,5,5], 6) == (5, 5)
#     assert partition([1,2,3,4], 2) == (1,2)
#     assert partition([1,2,3], 0) == (0, 0)
#     assert partition([1, 3, 3, 7], 3) == (1, 3)
#     assert partition([1, 3, 3, 7, 17, 42, 69, 420], 11) == (4, 4)

#     print("partition PASSED ALL TESTS")
# if __name__ == "__main__":
#     test_partition()
#     test_minimum()
