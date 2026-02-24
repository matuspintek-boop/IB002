#   #!/usr/bin/env python3

# Povolené knihovny: typing, math

from typing import TextIO

# IB002 Domácí úloha 7
#
# V tomto úkolu budeme pracovat s binárními stromy, kterým budeme říkat
# „levé minimové stromy“. Levé minimové stromy mají následující vlastnosti:
#
# * všechny listy levého minimového stromu jsou ve stejné hloubce;
# * levý minimový strom je zarovnaný doleva, což znamená, že:
#    a) pokud má některý uzel jen jednoho potomka, pak je to levý potomek;
#    b) pokud má některý uzel oba potomky, pak ten levý je kořenem perfektního
#       stromu (tj. úplného stromu se zaplněným posledním patrem);
# * klíče vnitřních uzlů jsou minima jejich podstromů
#   (skutečné hodnoty jsou tedy uloženy pouze v listech).
#
# Příklady levých minimových stromů:
#
#           1
#         /   \
#        2     1
#       / \   /
#      2   3 1
#
#         1
#      /     \
#     1       3
#    / \     /
#   2   1   3
#   ∧   ∧   ∧
#  2 3 1 4 3 5
#
# Příklady binárních stromů, které nejsou levými minimovými stromy:
#
#           1
#         /   \
#        2     1
#       / \
#      2   3
#  (porušuje první podmínku)
#
#           1
#         /   \
#        2     1
#       / \     \
#      2   3     1
#  (porušuje odrážku a) z druhé podmínky)
#
#           1
#         /   \
#        2     1
#       /     /
#      2     1
#  (porušuje odrážku b) z druhé podmínky)
#
#           1
#         /   \
#        2     0
#       / \   /
#      2   3 1
#  (porušuje třetí podmínku)
#
# Do následujících definic tříd nijak nezasahujte.
# Pro vykreslování stromů máte na konci tohoto souboru k dispozici
# funkci draw_tree.


class Node:
    """Třída Node reprezentuje uzel binárního stromu.

    Atributy:
        key     klíč uzlu
        left    odkaz na levý potomek uzlu nebo ‹None›
        right   odkaz na pravý potomek uzlu nebo ‹None›
    """
    __slots__ = "key", "left", "right"

    def __init__(self, key: int,
                 left: 'Node | None' = None,
                 right: 'Node | None' = None):
        self.key = key
        self.left = left
        self.right = right


class BinTree:
    """Třída BinTree reprezentuje binární strom.

    Atributy:
        root    odkaz na kořenový uzel stromu nebo ‹None›
    """
    __slots__ = "root"

    def __init__(self, root: Node | None = None):
        self.root = root


# Část 1.
# Implementujte funkci build_min_tree, která vybuduje levý minimový strom
# se zadanými hodnotami v listech. Strom musí být co nejnižší.

def build_min_tree(leaves: list[int]) -> BinTree:
    """
    vstup: ‹leaves› – pole celých čísel
    výstup: korektní levý minimový strom, který má co nejmenší výšku
            a v listech obsahuje hodnoty z pole ‹leaves› ve stejném pořadí
            zleva doprava; funkce nijak nemodifikuje zadaný vstup
    časová složitost: O(n), kde n je délka pole ‹leaves›

    Příklad: Pro vstupy [2, 3, 1] a [2, 3, 1, 4, 3, 5] mají odpovídajícími
    výstupy být stromy uvedené výše.
    """
    nodes = [Node(key, None, None) for key in leaves]

    while len(nodes) > 1:
        temp = []
        for i in range(0, len(nodes), +2):
            if i < len(nodes) - 1:
                second_key = nodes[i+1].key
            else:
                second_key = nodes[i].key

            min_key = min(nodes[i].key, second_key)

            new_node = Node(min_key, nodes[i], None)
            if i + 1 < len(nodes):
                new_node.right = nodes[i+1]
            temp.append(new_node)
        nodes = temp

    return BinTree(nodes[0])


# Část 2.
# Implementujte následující tři predikáty, které reprezentují výše uvedené tři
# podmínky levého minimového stromu. Každý predikát má jako vstupní podmínku
# platnost předchozích predikátů. Predikáty nemodifikují vstupní stromy.
def is_leaf(node: Node) -> bool:
    return node.left is None and node.right is None

def check_leaf_depth_rec(item: Node) -> int:
    if is_leaf(item):
        return 1
    else:
        if item.right is None:
            assert item.left is not None
            depth = check_leaf_depth_rec(item.left)
            if depth > -1:
                return depth + 1
            return -1
        elif item.left is None:
            depth = check_leaf_depth_rec(item.right)
            if depth > -1:
                return depth + 1
            return -1
    depth_l = check_leaf_depth_rec(item.left)
    depth_r = check_leaf_depth_rec(item.right)
    if depth_l == depth_r and depth_r > -1:
        return depth_r + 1
    return -1

def check_leaf_depth(tree: BinTree) -> bool:
    """
    vstup: ‹tree› – binární strom
    výstup: ‹True›, pokud mají všechny listy stromu stejnou hloubku;
            ‹False› jinak
    časová složitost: O(n), kde ‹n› je počet uzlů stromu
    extra prostorová složitost: O(h), kde ‹h› je výška stromu
        (Do extra prostorové složitost nepočítáme velikost vstupu, ale
         počítáme do ní zásobník rekurze.)
    """
    if tree.root is None:
        return True

    return check_leaf_depth_rec(tree.root) > -1

def check_complete_tree(item: Node) -> bool:
    if item.left is None and item.right is None:
        return True
    if item.right is None or item.left is None:
        return False
    else:
        return check_complete_tree(item.left) and check_complete_tree(item.right)

def check_left_align_rec(item: Node) -> bool:
    if item.left is None and item.right is None:
        return True
    elif item.left is not None and item.right is None:
        return check_left_align_rec(item.left)
    elif item.right is not None and item.left is not None:
        return check_complete_tree(item.left) and check_left_align_rec(item.right)
    return False

def check_left_align(tree: BinTree) -> bool:
    """
    vstup: ‹tree› – binární strom, jehož všechny listy mají stejnou hloubku
                    (tj. předpokládáme, že platí ‹check_leaf_depth(tree)›)
    výstup: ‹True›, pokud je strom zarovnaný doleva (dle popisu nahoře);
            ‹False› jinak
    časová složitost: O(n), kde ‹n› je počet uzlů stromu
    extra prostorová složitost: O(h), kde ‹h› je výška stromu
        (Do extra prostorové složitost nepočítáme velikost vstupu, ale
         počítáme do ní zásobník rekurze.)
    """
    if tree.root is None:
        return True
    return check_left_align_rec(tree.root)


def check_min_rec(item: Node) -> bool:
    if item.left is None and item.right is None:
        return True
    elif item.right is None:
        assert item.left is not None
        if not check_min_rec(item.left):
            return False
        return item.key == item.left.key
    else:
        assert item.left is not None
        if not (check_min_rec(item.left) and check_min_rec(item.right)):
            return False
        assert item.left is not None and item.right is not None
        return item.key == min(item.left.key, item.right.key)

def check_min(tree: BinTree) -> bool:
    """
    vstup: ‹tree› – binární strom, jehož všechny listy mají stejnou hloubku
                    a který je doleva zarovnaný dle podmínek nahoře
                    (tj. předpokládáme, že platí ‹check_leaf_depth(tree)›
                     i ‹check_left_align(tree)›)
    výstup: ‹True›, pokud je klíčem každého vnitřního uzlu minimum
                    jeho podstromu;
            ‹False› jinak
    časová složitost: O(n), kde ‹n› je počet uzlů stromu
    extra prostorová složitost: O(h), kde ‹h› je výška stromu
        (Do extra prostorové složitost nepočítáme velikost vstupu, ale
         počítáme do ní zásobník rekurze.)
    """

    if tree.root is None:
        return True

    return check_min_rec(tree.root)
    


# Následující funkci můžete použít pro vykreslení stromu při vlastním
# testování. Použití: draw_tree(strom, název souboru).
# Výstupem je soubor ve formátu GraphViz.

def draw_tree(tree: BinTree, filename: str) -> None:
    with open(filename, 'w') as file:
        file.write("digraph BinTree {\n"
                   "node [color=lightblue2, style=filled]\n")
        if tree.root is not None:
            draw_node(tree.root, file)
        file.write("}\n")


def draw_node(node: Node, file: TextIO) -> None:
    file.write(f'"{id(node)}" [label="{node.key}"]\n')
    for child, side in (node.left, 'L'), (node.right, 'R'):
        if child is None:
            nil = f"{side}{id(node)}"
            file.write(f'"{nil}" [label="", color=white]\n'
                       f'"{id(node)}" -> "{nil}"\n')
        else:
            file.write(f'"{id(node)}" -> "{id(child)}"\n')
            draw_node(child, file)


# if __name__ == "__main__":
#     draw_tree(build_min_tree([2, 3, 1, 4, 3, 5]), "./buildtree.dot")