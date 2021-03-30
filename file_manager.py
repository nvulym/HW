from collections.abc import Mapping
import os

class Dictlike(Mapping):
    def __init__(self, path):
        if not os.path.isdir(path):
            raise FileNotFoundError(f'Such {path} is not found')
        self.path = path
        self._content = {}  # key - filename in dir or dirname, value - content of file => {name:True/False}
        for i in os.listdir(self.path):  # listdir делает список всех файлов папки
            self._content[i] = not os.path.isdir(os.path.join(self.path, i))  # в словаре содержимого создается ключ с
            # названием файла или папки, а значение - файл (True), папка (False)

    def __repr__(self):
        files = '; '.join(k for k, file_ in self._content.items() if file_)
        dirs = '; '.join(k for k, file_ in self._content.items() if not file_)
        return f'Files:\n {files}\n\nDirs:\n{dirs}'

    def __len__(self):
        return len(self._content)

    def __getitem__(self, name_file):
        path_ = os.path.join(self.path, name_file)
        if not os.path.exists(path_):
            raise FileNotFoundError(f'Such {path_} is not found')
        if self._content[name_file]:
            return type(path_)
        # with open(path_) as f:
        #     return f.read()

    def __iter__(self):
        for i in self._content:
            yield i


f = Dictlike('OOP')
print(f)
# Files: alg_24.3.py; Molecule.py; OOP_3.1.py; OOP_3.py; OOP_4.py
# Dirs: .git
print(len(f))  # 6
for i in f:
    print(i)
    # .git
    # alg_24.3.py
    # Molecule.py
    # OOP_3.1.py
    # OOP_3.py
    # OOP_4.py
print('alg_24.3.py' in f)  # True
