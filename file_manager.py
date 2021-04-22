from collections.abc import Mapping
from os.path import abspath, join
import os


class DictLike(Mapping):
    def __init__(self, path):
        if not os.path.isdir(path):
            raise FileNotFoundError(f'Such {path} is not found')
        self._path = abspath(path)
        self._content = {}  # key - filename in dir or dirname, value - content of file => {name:True/False}
        for i in os.listdir(self._path):  # listdir делает список всех файлов папки
            self._content[i] = not os.path.isdir(os.path.join(self._path, i))  # в словаре содержимого создается ключ с
            # названием файла или папки, а значение - файл (True), папка (False)

    def __repr__(self):
        files = '; '.join(k for k, file_ in self._content.items() if file_)
        dirs = '; '.join(k for k, file_ in self._content.items() if not file_)
        return f'Files:\n {files}\n\nDirs:\n{dirs}'

    def __len__(self):
        return len(self._content)

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise TypeError
        if key in self._content:
            path = join(self._path, key)
            if os.path.isdir(path):
                return DictLike(path)
            elif os.path.isfile(path):
                with open(path, 'r') as f:
                    return f.read()
        else:
            pass

    def __iter__(self):
        yield from (i for i in self._content)

    def __contains__(self, key):
        if not isinstance(key, str):
            raise TypeError
        return key in self._content.keys()


path = 'D:\PythonProject\HW\OOP\\test_dir'
f = DictLike(path)
print(f._content)  # {'file_1': True, 'file_2': True, 'test_dir_2': False}
print(f)
# Files:
#  file_1; file_2
# Dirs:
# test_dir_2
print(len(f))  # 3
for i in f:
    print(i)
# file_1
# file_2
# test_dir_2
print('file_1' in f) # True
file_1 = f['file_1']
print(file_1)  # file content 1

