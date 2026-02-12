#!/usr/bin/env python3

# Povolené knihovny: typing, math

# IB002 Domácí úloha 4
#
# Trojková (ternární) soustava je poziční číselná soustava o základu 3,
# která používá číslice 0, 1, 2. Tedy např. číslo 42 ve trojkové soustavě
# zapíšeme jako (1120)₃.
#
# Vaším úkolem bude implementovat funkci, která pro zadané parametry
# ‹length› a ‹total› vrátí vzestupně seřazený Pythonovský seznam všech
# kladných celých čísel, která mají ve trojkové soustavě právě ‹length›
# číslic a jejichž součet trojkových číslic je právě ‹total›. Přitom
# uvažujeme pouze zápis čísla bez zbytečných levostranných nul, tedy
# např. číslo 42 má ve trojkové soustavě právě čtyři číslice, ne více.
#
# Příklady:
# Pro vstup ‹length = 3› a ‹total = 5› bude výstupem seznam:
#   [17, 23, 25]
# ve trojkové soustavě bychom totiž tato čísla zapsali jako:
#   (122)₃, (212)₃, (221)₃
#
# Pro vstup ‹length = 4› a ‹total = 2› bude výstupem seznam:
#   [28, 30, 36, 54]
# ve trojkové soustavě bychom totiž tato čísla zapsali jako:
#   (1001)₃, (1010)₃, (1100)₃, (2000)₃
#
# Počty čísel splňujících zadanou podmínku se dají zapsat do takovéto
# tabulky:
#
#          │                    total
#   length │  1   2   3   4   5   6   7   8   9  10  11  ...
#   ───────┼────────────────────────────────────────────
#      1   │  1   1   0   0   0   0   0   0   0   0   0
#      2   │  1   2   2   1   0   0   0   0   0   0   0
#      3   │  1   3   5   5   3   1   0   0   0   0   0
#      4   │  1   4   9  13  13   9   4   1   0   0   0
#      5   │  1   5  14  26  35  35  26  14   5   1   0
#     ...
#
# Při podrobnějším zkoumání této tabulky si můžete všimnout jisté
# pravidelnosti; snadno pak dopočítáte další řádky. Hodnoty v tabulce
# jednak můžete využít pro částečnou kontrolu toho, že vaše řešení
# počítá správně, jednak budou hrát roli v časové složitosti řešení.
#
# Smyslem tohoto úkolu je procvičit si rekurzi. Vstupy v testech budou
# takové, aby rozumně použitá rekurze nenarazila na žádný limit.
#
# Kritickou částí tohoto úkolu je časová složitost řešení. Pro splnění
# požadavků je třeba si jednak dobře rozmyslet, ve kterých chvílích
# je vhodné rekurzi ukončit, jednak si dát pozor na to, co přesně
# děláte s Pythonovskými seznamy a jakou mají tyto operace složitost.
#
# Při analýze časové složitosti jako obvykle zanedbáváme přesnou složitost
# aritmetických operací s čísly, tj. považujeme ji za konstantní.
#
# Nezapomeňte, že si můžete definovat pomocné funkce. V tomto úkolu je
# to určitě velmi vhodné.

def ternary_sum_rec(current_num: int, current_len: int, current_total: int,
                    length: int, total: int, data: list[int]) -> None:
    # for safety, early exit
    if current_total > total:
        return
    
    if length - current_len == 0 and total - current_total == 0:
        data.append(current_num)
    elif length - current_len == 0 and total - current_total > 0:
        return
    elif 2*(length - current_len) < total - current_total:
        return
    for i in range(min(2, total - current_total)+1):
        ternary_sum_rec(current_num*3 + i, current_len+1, current_total+i, length, total, data)
def ternary_sum(length: int, total: int) -> list[int]:
    """
    vstup: ‹length› – kladné celé číslo
           ‹total› – kladné celé číslo
    výstup: vzestupně seřazený seznam všech kladných celých čísel,
            která mají ve trojkové soustavě právě ‹length› číslic
            a součet jejichž trojkových číslic je právě ‹total›
    časová složitost: O(T(length, total) · length),
        kde T(length, total) je hodnota z tabulky naznačené výše
    """
    data: list[int] = []

    if length == 0:
        return data

    ternary_sum_rec(1, 1, 1, length, total, data)
    ternary_sum_rec(2, 1, 2, length, total, data)

    return data


# def test_ternary_sum() -> None:
#     assert len(ternary_sum(1,1)) == 1
#     assert len(ternary_sum(1,2)) == 1
#     assert len(ternary_sum(1,3)) == 0
#     assert len(ternary_sum(0, 0)) == 0
#     assert len(ternary_sum(4,5)) == 13
#     assert len(ternary_sum(5, 5)) == 35
#     assert len(ternary_sum(5, 11)) == 0

# if __name__ == "__main__":
#     test_ternary_sum()