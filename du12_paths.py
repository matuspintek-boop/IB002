#!/usr/bin/env python3

# Povolené knihovny: typing, math, collections, heapq
# Pro práci s knihovnou heapq je vhodné se podívat na poznámku
# v úvodu programovacího cvičení cv12.
# Z knihovny collections je povolena pouze datová struktura deque
# reprezentující frontu. Pro její import použijte přesně následující řádek:
# from collections import deque

# IB002 Domácí úloha 12
#
# V tomto úkolu budeme pracovat s ohodnocenými orientovanými grafy. Grafy
# budeme opět reprezentovat pomocí seznamů následníků jako v minulé dú.
#
# Grafy v této úloze nám představují dopravní sítě – tedy vrcholy jsou místa,
# mezi kterými se chceme přepravovat a hrany jsou povolené přesuny (existují
# i „jednosměrky“, takže náš graf je orientovaný). Přitom předpokládáme, že náš
# dopravní prostředek má určitou zásobu energie (přestavujte si třeba
# elektromobil s baterií). Ohodnocení v grafu pak znamenají energetickou
# náročnost přesunu po dané hraně – kladné ohodnocení znamená, že se při
# přesunu hranou energie spotřebovává, záporné ohodnocení naopak znamená, že
# energii získáme (např. je po cestě nějaká „dobíjecí stanice“).
#
# Pro zjednodušení uvažujeme následující (trochu nerealistické) předpoklady:
# • zásoba energie našeho dopravního prostředku má neomezenou kapacitu, může se
#   tedy dobít na libovolně vysokou hodnotu;
# • pokud jsme vyčerpali všechnu energii (tj. jsme „na nule“), ještě stále se
#   můžeme pohnout po hraně s nulovým nebo záporným ohodnocením.
#
# V obou částech této úlohy budete řešit stejný problém – pro zadaný počáteční
# vrchol a zadaný počáteční stav energie našeho dopravního prostředku máte
# spočítat, do kterých vrcholů grafu je možno se dostat. Části se liší jen
# vstupními předpoklady ohledně ohodnocení – první část předpokládá jen kladná
# ohodnocení (takže žádné dobíjení energie), druhá část je obecná.
#
# Příklad grafu s vrcholy 0, 1, 2, 3, 4 a hranami:
#   0 → 1 s ohodnocením 9 (tedy přesun z 0 do 1 nás stojí 9 jednotek energie),
#   0 → 2 s ohodnocením 4,
#   1 → 3 s ohodnocením -8 (tedy přesunem z 1 do 3 získáme 8 jednotek energie),
#   2 → 3 s ohodnocením -2,
#   3 → 4 s ohodnocením 3.
#
# Je-li počáteční vrchol 0 a počáteční stav energie 4, pak se můžeme dostat do
# vrcholů 0, 2 a 3.
# Dostat se do vrcholu 0 je triviální – v něm totiž začínáme.
# Do vrcholu 2 se dostaneme cestou 0 → 2.
# Do vrcholu 3 se dostaneme cestou 0 → 2 → 3 (ve vrcholu 2 sice budeme mít
# nulovou energii, ale předpoklad výše říká, že se můžeme dál pohnout po hraně
# s ohodnocením -2).
# Do vrcholu 1 nebo 4 se dostat nemůžeme.
#
# Kdyby byl počáteční stav energie 5, pak se navíc umíme dostat do vrcholu 4,
# a to cestou 0 → 2 → 3 → 4.
#
# Kdyby byl počáteční stav energie 9, pak se navíc umíme dostat do vrcholu 1,
# a to cestou 0 → 1.
#
# Definici třídy Graph nijak nemodifikujte.


class Graph:
    """Třída Graph reprezentuje orientovaný graf, jehož hrany jsou ohodnoceny
    celými čísly.

    Atributy:
        size    počet vrcholů grafu
                (vrcholy jsou očíslované 0, 1, ..., size - 1)
        succs   seznam dvojic (ohodnocení hrany, následník)
    """
    __slots__ = 'size', 'succs'

    def __init__(self, size: int):
        self.size = size
        self.succs: list[list[tuple[int, int]]] = \
            [[] for _ in range(size)]


# Zde je několik testovacích grafů, ke kterým se vztahují příklady
# v dokumentaci níže. Vykreslit si je můžete funkcí draw_graph.

def example_graph1() -> Graph:
    graph = Graph(5)
    graph.succs[0] = [(3, 1), (4, 3)]
    graph.succs[1] = [(5, 3), (2, 2), (1, 4)]
    graph.succs[2] = [(2, 0)]
    graph.succs[3] = [(2, 2), (1, 4)]
    graph.succs[4] = [(7, 2), (3, 0)]
    return graph


def example_graph2() -> Graph:
    graph = Graph(5)
    graph.succs[0] = [(9, 1), (4, 2)]
    graph.succs[1] = [(-8, 3)]
    graph.succs[2] = [(-2, 3)]
    graph.succs[3] = [(3, 4)]
    # vertex 4 has no successors
    return graph


def example_graph3() -> Graph:
    graph = Graph(10)
    graph.succs[0] = [(5, 1), (7, 2), (21, 8)]
    graph.succs[1] = [(7, 5), (100, 7)]
    graph.succs[2] = [(3, 3), (-5, 1)]
    graph.succs[3] = [(4, 4)]
    graph.succs[4] = [(-9, 2), (100, 5)]
    graph.succs[5] = [(100, 6)]
    # vertex 6 has no successors
    # vertex 7 has no successors
    graph.succs[8] = [(0, 6), (-20, 9)]
    graph.succs[9] = [(0, 0)]
    return graph


# Pro všechny části níže platí, že zadané funkce nesmí nijak modifikovat
# vstupní graf.

# Část 1.
# V této části předpokládáme, že všechny hrany jsou ohodnoceny pouze kladnými
# čísly.

def reachable(graph: Graph, start: int, initial_energy: int) -> list[int]:
    """
    vstup: ‹graph› – ohodnocený orientovaný graf (objekt typu ‹Graph›)
                     všechna ohodnocení hran jsou kladná celá čísla
           ‹start› – počáteční vrchol
           ‹initial_energy› – počáteční množství energie (kladné celé číslo)
    výstup: seznam všech vrcholů zadaného grafu, do nichž je možné se dostat
            z počátečního vrcholu a se zadanou počáteční energií;
            na pořadí vrcholů v seznamu nezáleží
    časová složitost: O((|V| + |E|) · log |V|)
    extra prostorová složitost: O(|V| + |E|)

    Příklady:
    Pro graf example_graph1() s počátečním vrcholem 0 platí:
    • pro počáteční energii 1 nebo 2 je výsledkem [0];
    • pro počáteční energii 3 je výsledkem [0, 1];
    • pro počáteční energii 4 je výsledkem [0, 1, 3, 4];
    • pro počáteční energii 5 nebo vyšší je výsledkem seznam všech vrcholů.

    Pro graf example_graph1() s počátečním vrcholem 3 platí:
    • pro počáteční energii 1 je výsledkem [3, 4];
    • pro počáteční energii 2 nebo 3 je výsledkem [2, 3, 4];
    • pro počáteční energii 4, 5 nebo 6 je výsledkem [0, 2, 3, 4];
    • pro počáteční energii 7 nebo vyšší je výsledkem seznam všech vrcholů.
    """
    return []  # TODO


# Část 2.
# V této části dovolíme, aby ohodnocení hran byla libovolná celá čísla.

def reachable_with_charging(graph: Graph, start: int, initial_energy: int) \
        -> list[int]:
    """
    vstup: ‹graph› – ohodnocený orientovaný graf (objekt typu ‹Graph›)
                     ohodnocení hran jsou celočíselná
           ‹start› – počáteční vrchol
           ‹initial_energy› – počáteční množství energie (kladné celé číslo)
    výstup: seznam všech vrcholů zadaného grafu, do nichž je možné se dostat
            z počátečního vrcholu a se zadanou počáteční energií;
            na pořadí vrcholů v seznamu nezáleží
    časová složitost: O(|V| · (|V| + |E|))
    extra prostorová složitost: O(|V|)

    Příklady:
    Příklady z předchozí části dopadnou stejně i zde.

    Pro graf example_graph2() a počáteční vrchol 0 platí:
    • pro počáteční energii 1, 2 nebo 3 je výsledkem [0];
    • pro počáteční energii 4 je výsledkem [0, 2, 3];
    • pro počáteční energii 5, 6, 7 nebo 8 je výsledkem [0, 2, 3, 4];
    • pro počáteční energii 9 je výsledkem seznam všech vrcholů.

    Pro graf example_graph3() a počáteční vrchol 0 platí:
    • pro počáteční energii 1, 2, 3 nebo 4 je výsledkem [0];
    • pro počáteční energii 5 nebo 6 je výsledkem [0, 1];
    • pro počáteční energii 7 nebo 8 je výsledkem [0, 1, 2];
    • pro počáteční energii 9 je výsledkem [0, 1, 2, 5];
    • pro počáteční energii 10, 11, 12 nebo 13 je výsledkem
      [0, 1, 2, 3, 5];
    • pro počáteční energii 14, 15, 16, 17, 18 19 nebo 20 je výsledkem
      [0, 1, 2, 3, 4, 5, 6, 7];
    • pro počáteční energii 21 a vyšší je výsledkem seznam všech vrcholů.

    Pro tentýž graf s počátečním vrcholem 8 stačí 1 jednotka energie k tomu,
    aby byly dosažitelné všechny vrcholy.
    """
    return []  # TODO


# Následující funkci můžete použít pro vykreslení grafu při vlastním testování.

def draw_graph(graph: Graph, filename: str) -> None:
    with open(filename, 'w') as file:
        file.write("digraph G {\n"
                   "node [color=lightblue2, style=filled]\n")
        for vertex in range(graph.size):
            for weight, succ in graph.succs[vertex]:
                file.write(f'"{vertex}" -> "{succ}" [label="{weight}"]\n')
        file.write("}\n")
