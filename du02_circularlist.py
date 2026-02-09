#!/usr/bin/env python3

# IB002 Domácí úloha 2.
#
# Jednosměrně zřetězený seznam už znáte – je tvořen uzly (Node), kde každý
# z nich ukazuje na svého následníka. V tomto úkolu se budeme bavit o tzv.
# kruhových zřetězených seznamech, v nichž jsou uzly spojeny do kruhu
# (tedy atribut ‹next› „posledního“ uzlu se odkazuje na „první“ uzel).
# Takové seznamy budou na vstupu funkcí vždy zadány odkazem na jeden
# z uzlů (nikdy tedy nebudou prázdné).
#
# Podobně jako u minulé úlohy, i zde je smyslem procvičit si práci s odkazy.
# Platí tedy stejný zákaz používání vestavěných datových struktur Pythonu.
# Povolená je opět pouze knihovna typing.
#
# V příkladech a ve výstupu z testů znázorňujeme kruhové zřetězené seznamy
# následovně:
#
#  ╭→ 3 → 4 → 5 → 7 ╮
#  ╰────────────────╯
# Toto reprezentuje kruhový seznam o čtyřech uzlech, zadaný odkazem na
# uzel s hodnotou 3. Atribut ‹next› uzlu s hodnotou 7 se odkazuje na
# uzel s hodnotou 3.
#
# Jednoprvkový kruhový seznam znázorníme takto:
#  ╭→ 42 ╮
#  ╰─────╯
#
# Do definice třídy Node nijak nezasahujte.
# Atribut ‹jump› se používá pouze v druhé části, v první části jej nijak
# nemodifikujte.


class Node:
    """Třída Node reprezentuje uzel v kruhovém zřetězeném seznamu.
    Objekty typu Node se inicializují jako ‹Node(hodnota)›, přičemž jejich
    atribut ‹next› se nastaví na právě vytvořený uzel (jde tedy o uzel
    v kruhovém zřetězeném seznamu délky 1).

    Atributy:
        value   hodnota uzlu
        next    odkaz na další uzel seznamu (nikdy nebude ‹None›)
        jump    atribut, který budeme používat ve druhé části
                (v první části jej ignorujte)
    """
    __slots__ = "value", "next", "jump"

    def __init__(self, value: int) -> None:
        self.value = value
        self.next = self
        self.jump: Node | None = None


# Část 1.
# Implementujte funkci reverse, která obrátí zadaný kruhový zřetězený seznam.
def reverse(start: Node) -> None:
    """
    vstup: ‹start› – odkaz na uzel kruhového zřetězeného seznamu
    výstup: žádný,
            v zadaném kruhovém seznamu se přenastaví atributy ‹next› tak,
            aby ukazovaly v opačném směru
            (seznam musí samozřejmě zůstat korektní)
    časová složitost: O(n), kde n je délka vstupního seznamu, tedy lineární
    extra prostorová složitost: O(1), tedy konstantní
        (zejména tedy nesmíte vytvářet nové uzly;
         modifikujte jen jejich atributy ‹next›)

    Příklady:
    Před provedením funkce: ╭→ 1 → 2 → 3 → 4 → 5 ╮
                            ╰────────────────────╯
    Po provedení funkce:    ╭→ 1 → 5 → 4 → 3 → 2 ╮
                            ╰────────────────────╯

    Před provedením funkce: ╭→ 10 → 7 → 1 → 2 → 3 → 4 → 19 ╮
                            ╰──────────────────────────────╯
    Po provedení funkce:    ╭→ 10 → 19 → 4 → 3 → 2 → 1 → 7 ╮
                            ╰──────────────────────────────╯
    """
    prev: Node = start
    current = start.next

    while current != start:
        current_next = current.next
        current.next = prev
        prev = current
        current = current_next

    current.next = prev

    return


# Část 2.
# V této části použijeme atribut ‹jump›. Implementujte funkci set_jump,
# která každému uzlu nastaví tento atribut tak, aby se odkazoval na uzel
# v zadané vzdálenosti od něj.
def pair_nodes(node1: Node, node2: Node, start: Node) -> None:
    while node1.next != start:
        node1.jump = node2
        node1 = node1.next
        node2 = node2.next

    node1.jump = node2


def set_jump(start: Node, jump_size: int) -> None:
    """
    vstup: ‹start›     – odkaz na uzel kruhového zřetězeného seznamu
           ‹jump_size› – celé číslo ≥ 1
    výstup: žádný,
            všem uzlům v zadaném kruhovém seznamu se nastaví atribut
            ‹jump› tak, aby se odkazoval na uzel, který je o ‹jump_size›
            pozic za aktuálním uzlem
            (je-li ‹jump_size› 1, pak ‹x.jump› bude totéž, co ‹x.next›,
             je-li ‹jump_size› 2, pak ‹x.jump› bude totéž, co ‹x.next.next›,
             atd.)
    časová složitost: O(n), kde n je délka vstupního seznamu, tedy lineární
        (všimněte si zejména, že časová složitost nemá nijak záviset
         na hodnotě parametru ‹jump_size›, a to přesto, že tento parametr
         může být libovolné kladné číslo;
         lineární časová složitost neznamená, že zadaný seznam smíte projít
         jen jednou; můžete jej procházet vícekrát, ale ten počet průchodů
         musí být konstantní, tj. nezávislý na velikosti vstupu;
         časovou složitost aritmetických operací zanedbáváme – tedy se k ní
         chováme, jako by byla konstantní)
    extra paměťová složitost: O(1), tedy konstantní
        (zejména tedy nesmíte vytvářet nové uzly;
         modifikujte jen jejich atributy ‹jump›)

    Příklady:
    Pro vstup ╭→ 1 → 2 → 3 → 4 → 5 ╮ a jump_size = 3 budou atributy ‹jump›
              ╰────────────────────╯ nastaveny takto:

    atribut ‹jump› uzlu s hodnotou 1 se bude odkazovat na uzel s hodnotou 4
    atribut ‹jump› uzlu s hodnotou 2 se bude odkazovat na uzel s hodnotou 5
    atribut ‹jump› uzlu s hodnotou 3 se bude odkazovat na uzel s hodnotou 1
    atribut ‹jump› uzlu s hodnotou 4 se bude odkazovat na uzel s hodnotou 2
    atribut ‹jump› uzlu s hodnotou 5 se bude odkazovat na uzel s hodnotou 3

    Pro vstup ╭→ 10 → 7 → 1 → 2 → 3 → 4 → 19 ╮ a jump_size = 100 budou
              ╰──────────────────────────────╯ atributy ‹jump› nastaveny takto:

    atribut ‹jump› uzlu s hodnotou 10 se bude odkazovat na uzel s hodnotou 1
    atribut ‹jump› uzlu s hodnotou 7 se bude odkazovat na uzel s hodnotou 2
    atribut ‹jump› uzlu s hodnotou 1 se bude odkazovat na uzel s hodnotou 3
    atribut ‹jump› uzlu s hodnotou 2 se bude odkazovat na uzel s hodnotou 4
    atribut ‹jump› uzlu s hodnotou 3 se bude odkazovat na uzel s hodnotou 19
    atribut ‹jump› uzlu s hodnotou 4 se bude odkazovat na uzel s hodnotou 10
    atribut ‹jump› uzlu s hodnotou 19 se bude odkazovat na uzel s hodnotou 7
    """
    backup_start = start

    length = 1

    current = start.next
    while current != start:
        length += 1
        current = current.next

    jump_size %= length

    if jump_size == 0:
        return
    
    sibling = start

    while jump_size > 0:
        sibling = sibling.next
        jump_size -= 1

    pair_nodes(start, sibling, start)

    return


def create_circular_list(data: list[int]) -> Node:
    nodes: list[Node] = [Node(i) for i in data]
    for index, node in enumerate(nodes):
        node.next = nodes[(index+1)%len(nodes)]

    return nodes[0]

def print_nodes(node: Node) -> None:
    print(node.value)    
    if node.jump is not None:
        print(node.jump.value)
    else:
        print("No jump")
    start: Node = node
    node = node.next

    while node != start:
        print(node.value)
        if node.jump is not None:
            print(node.jump.value)
        else:
            print("No jump")
        node = node.next



# def test_circular_list() -> None:

#     nodes = create_circular_list([1,2,3,4,5])
#     reverse(nodes)
#     print_nodes(nodes)


# def test_set_jump() -> None:
#     nodes = create_circular_list([10,7,1,2,3,4,19])
#     set_jump(nodes, 100)
#     print_nodes(nodes)



# if __name__ == "__main__":
#     test_circular_list()
#     print("-------------")
#     test_set_jump()