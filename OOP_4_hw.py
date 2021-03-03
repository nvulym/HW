class Molecule:
    def __init__(self):
        self._atoms = {}
        self._bonds = {}

    def add_atom(self, atom, *, map_=None):
        if map_ is None:
            map_ = max(self._atoms, default=0) + 1
        elif not isinstance(map_, int):
            raise TypeError
        elif map_ < 1:
            raise ValueError
        elif map_ in self._atoms:
            raise KeyError
        if not isinstance(atom, str):
            raise TypeError
        elif atom not in ('C', 'N', 'Cl', 'Br', 'F', 'I', 'O', 'S'):
            raise ValueError
        self._atoms[map_] = atom
        self._bonds[map_] = {}

    def add_bond(self, map1, map2, bond):
        if not isinstance(bond, int):
            raise TypeError
        if bond not in (1, 2, 3):
            raise ValueError

        # есть ли в селф.атом , что мап1 не равно мап2, что уже есть связь м\у этими атомами, что одноатомн мол-ла
        neigh1 = self._bonds[map1]
        neigh2 = self._bonds[map2]

        if neigh1 is neigh2:  # что мап1 не равно мап2
            raise KeyError
        if map1 in neigh2:  # что уже есть связь м\у этими атомами
            raise KeyError

        neigh1[map2] = bond
        neigh2[map1] = bond

    def print_atom(self):
        return self._atoms

    def print_bond(self):
        return self._bonds

    # добавить метод : del_atom(map_), del_bond(map1, map2)
    def dell_atom(self, map_):
        self._atoms.pop(map_)  # удаляет атом по номеру, если есть в словаре
        for neigh in self._bonds[map_]:
            self._bonds[neigh].pop(map_)

    def dell_bond(self, map1, map2):
        del self._bonds[map1][map2]
        del self._bonds[map2][map1]

    def __iter__(self):
        # возвращает генератор
        return iter(self._atoms)

    def iter_bonds(self):
        # должен быть генератором возвращающим пару (1,2) (2,1)
        for map1 in self._bonds.keys():
            for map2 in self._bonds[map1]:
                yield (map1,map2)

mol = Molecule()
mol.add_atom(atom = 'C', map_ = 1)
mol.add_atom(atom = 'C', map_ = 2)
mol.add_bond(1, 2, 1)
mol.add_atom(atom = 'C', map_ = 3)
mol.add_bond(2, 3, 1)
mol.add_atom(atom = 'Cl', map_ = 4)
mol.add_bond(1, 4, 1)
# print('Atoms before', mol.print_atom())
# print('Bonds before', mol.print_bond())
# mol.dell_atom(map_=8)
# print('Atoms after', mol.print_atom())
# print('Bonds after', mol.print_bond())
# print('Atoms before', mol.print_atom())
# print('Bonds before', mol.print_bond())
# mol.dell_bond(map1=1, map2=4)
# print('Atoms after', mol.print_atom())
# print('Bonds after', mol.print_bond())

for bonds in mol.iter_bonds():
    print(bonds)
    # (1, 2)
    # (1, 4)
    # (2, 1)
    # (2, 3)
    # (3, 2)
    # (4, 1)