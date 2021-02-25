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

    def show_atom(self):
        return self._atoms

    def show_bond(self):
        return self._bonds

    # добавить метод : del_atom(map_), del_bond(map1, map2)
    def dell_atom(self, map_):
        if not isinstance(map_, int):
            raise TypeError
        elif map_ in self._atoms:
            self._atoms.pop(map_)  # удаляет атом по номеру, если есть в словаре
            for neigh in self._bonds[map_]:
                self._bonds[neigh].pop(map_)
            self._bonds.pop(map_)  # удаляет связи, которые были связаны с этим атомом


    def dell_bond(self, map1, map2):
        if not isinstance((map1, map2), int):
            raise TypeError

        self._bonds.pop(map1)
        self._bonds.pop(map2)

mol = Molecule()
mol.add_atom(atom = 'C', map_ = 1)
mol.add_atom(atom = 'C', map_ = 2)
mol.add_bond(1, 2, 1)
mol.add_atom(atom = 'C', map_ = 3)
mol.add_bond(2, 3, 1)
mol.add_atom(atom = 'Cl', map_ = 4)
mol.add_bond(1, 4, 1)
print('Atoms before', mol.show_atom())
print('Bonds before', mol.show_bond())
mol.dell_atom(map_=0)
print('Atoms after', mol.show_atom())
print('Bonds after', mol.show_bond())