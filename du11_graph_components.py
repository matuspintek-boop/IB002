#!/usr/bin/env python3

# Povolené knihovny: typing, math, collections
# Z knihovny collections je povolena pouze datová struktura deque
# reprezentující frontu. Pro její import použijte přesně následující řádek:
# from collections import deque

# IB002 Domácí úloha 11
#
# V tomto úkolu se podíváme na hledání silně souvislých komponent v grafu.
# Doporučujeme, abyste si předtím, než začnete programovat, připomněli,
# co to silně souvislé komponenty v grafu jsou a jaké známe algoritmy pro
# jejich počítání.
#
# Grafy budeme v tomto úkolu reprezentovat pomocí seznamů následníků.
# Každý graf ‹g› má tedy vrcholy očíslované 0, ..., g.size - 1 (včetně).
#
# Definici třídy Graph nijak nemodifikujte.


class Graph:
    """Třída Graph reprezentuje orientovaný graf pomocí seznamů následníků.

    Atributy:
        size    počet vrcholů grafu
                (vrcholy jsou očíslované 0, 1, ..., size - 1)
        succs   seznamy následníků
                (succs[v] obsahuje následníky vrcholu ‹v›)
    """
    __slots__ = 'size', 'succs'

    def __init__(self, size: int):
        self.size = size
        self.succs: list[list[int]] = [[] for _ in range(size)]


# Následují dvě ukázky grafů, ke kterým se budeme odkazovat v příkladech
# výstupů funkcí. Prvním z nich je graf, který jsme viděli v 11. kapitole
# sbírky.

def example_graph1() -> Graph:
    graph = Graph(10)
    graph.succs[0] = [2, 3, 6]
    graph.succs[1] = [4, 8]
    graph.succs[2] = [5]
    graph.succs[3] = [7, 8]
    graph.succs[4] = [8]
    graph.succs[5] = [6]
    graph.succs[6] = [2]
    graph.succs[7] = [6, 9]
    graph.succs[8] = [0]
    graph.succs[9] = [7]
    return graph


def example_graph2() -> Graph:
    graph = Graph(8)
    graph.succs[0] = [5, 1, 4]
    graph.succs[1] = [0, 6]
    graph.succs[2] = [7, 2]
    graph.succs[3] = [7]
    # vertex 4 has no successors
    graph.succs[5] = [5]
    graph.succs[6] = [7]
    graph.succs[7] = [6]
    return graph


# Pro všechny části níže platí, že zadané funkce nesmí nijak modifikovat
# vstupní graf.


# Část 1.
# Implementujte funkci strongly_connected_components, která najde všechny
# silně souvislé komponenty zadaného grafu.

def strongly_connected_components(graph: Graph) -> list[list[int]]:
    """
    vstup: ‹graph› – orientovaný graf (objekt typu ‹Graph›)
    výstup: seznam všech silně souvislých komponent grafu;
            každá komponenta je reprezentována seznamem svých vrcholů
            na pořadí prvků v seznamech nezáleží
    časová složitost: O(|V| + |E|)

    Příklady:
      Pro první ukázkový graf může být výsledkem např. tento seznam:
        [[1], [4], [0, 3, 8], [7, 9], [2, 5, 6]]
      Pro druhý ukázkový graf může být výsledkem např. tento seznam:
        [[0, 1], [2], [3], [4], [5], [6, 7]]
    """
    pass  # TODO


# Část 2.
# O silně souvislé komponentě grafu řekneme, že je «terminální» (někdy také
# spodní, koncová, listová), pokud z ní nevedou žádné hrany do jiných
# komponent.
# Implementujte funkci terminal_sccs, která najde všechny terminální silně
# souvislé komponenty zadaného grafu.

def terminal_sccs(graph: Graph) -> list[list[int]]:
    """
    vstup: ‹graph› – orientovaný graf (objekt typu ‹Graph›)
    výstup: seznam všech terminálních silně souvislých komponent grafu;
            každá komponenta je reprezentována seznamem svých vrcholů
            na pořadí prvků v seznamech nezáleží
    časová složitost: O(|V| + |E|)

    Příklady:
      Pro první ukázkový graf může být výsledkem např. tento seznam:
        [[2, 5, 6]]
      Pro druhý ukázkový graf může být výsledkem např. tento seznam:
        [[4], [5], [6, 7]]
    """
    pass  # TODO


# Část 3.
# O silně souvislé komponentě grafu řekneme, že je «iniciální» (někdy také
# počáteční, horní, kořenová), pokud do ní nevedou žádné hrany z jiných
# komponent.
# Implementujte funkci initial_sccs, která najde všechny iniciální silně
# souvislé komponenty zadaného grafu.

def initial_sccs(graph: Graph) -> list[list[int]]:
    """
    vstup: ‹graph› – orientovaný graf (objekt typu ‹Graph›)
    výstup: seznam všech iniciálních silně souvislých komponent grafu;
            každá komponenta je reprezentována seznamem svých vrcholů
            na pořadí prvků v seznamech nezáleží
    časová složitost: O(|V| + |E|)

    Příklady:
      Pro první ukázkový graf musí být výsledkem tento seznam:
        [[1]]
      Pro druhý ukázkový graf může být výsledkem např. tento seznam:
        [[0, 1], [2], [3]]
    """
    pass  # TODO


# Následující funkci můžete použít pro vykreslení grafu při vlastním
# testování.

def draw_graph(graph: Graph, filename: str) -> None:
    with open(filename, 'w') as file:
        file.write("digraph G {\n"
                   "node [color=lightblue2, style=filled]\n")
        for vertex in range(graph.size):
            for succ in graph.succs[vertex]:
                file.write(f'"{vertex}" -> "{succ}"\n')
        file.write("}\n")
