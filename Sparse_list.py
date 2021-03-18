class Sparse_list:
    def __init__(self):
        self._data = {}  # {ind:num}
        self._len = 0  # max ind

    def __len__(self):
        return self._len

    def __repr__(self):  # вернет строку, содержащую печатаемое формальное представление объекта => список с 0
        temp_list = [0.] * self._len
        for key, val in self._data.items():
            temp_list[key] = val
        return str(temp_list)

    def __setitem__(self, ind, value):
        if not isinstance(ind, int) and not isinstance(value, (float, int)):
            raise TypeError
        elif ind >= self._len:
            raise IndexError("List index out of range")
        elif ind < -self._len:
            raise IndexError("List assignment index out of range")
        elif -self._len <= ind < 0:
            ind = self._len + ind
        if value == 0:  # список не должен содержать 0
            try:
                del self._data[ind]
            except KeyError:
                pass
        else:
            self._data[ind] = value

    def __getitem__(self, ind):
        if isinstance(ind, int):
            if ind > self._len or -self._len > ind:
                raise IndexError('List index out of range')
            elif ind < 0:
                ind = self._len + ind
            return self._data.get(ind, default = 0)
        elif isinstance(ind, slice):
            out_dict = Sparse_list()
            for i in range(*ind.indices(self._len)):
                try:
                    out_dict._data[out_dict._len] = self._data[i]
                    out_dict._len += 1
                except KeyError:
                    out_dict._len += 1
            return out_dict
        else:
            raise TypeError

    def __delitem__(self, item):
        if isinstance(item, slice):
            indices_to_remove = range(*item.indices(self._len))
        elif item < 0:
            indices_to_remove = (self._len + item, )
        else:
            indices_to_remove = (item, )
        if not indices_to_remove:
            raise KeyError

        indices_removed = 0
        removing_tail = indices_to_remove[-1] == self._len - 1

        for current_ind in sorted(self._data.keys()):
            if current_ind < indices_to_remove[0]:
                continue
            elif indices_removed < len(indices_to_remove) and current_ind > indices_to_remove[indices_removed]:
                indices_removed += 1
            if indices_removed and not removing_tail:
                self._data[current_ind - indices_removed] = self._data[current_ind]
            del self._data[current_ind]
        self._len -= len(indices_to_remove)

    def append(self, el):  # Добавляет элемент в конец списка
        if not isinstance(el, (float, int)):
            raise ValueError
        elif el == 0:
            self._len += 1
        else:
            self._data[self._len] = el
            self._len += 1

    def clear(self):  # Очищает список
        self._data = {}
        self._len = 0

    def pop(self, index=None):  # Удаляет элемент с позиции i и возвращает его
        if not self._len:
            raise IndexError('Empty list')
        if not index:
            try:
                val = self._data[self._len - 1]
                del self._data[self._len - 1]
                return val
            except KeyError:
                self._len -= 1
                return 0
        if isinstance(index, int):
            if self._len >= index > -self._len:
                try:
                    val = self._data[index]
                    del self._data[index]
                    return val
                except:
                    self._len -= 1
                    return 0
            else:
                raise IndexError('Pop index out of range')
        else:
            raise TypeError

    def extend(self, L): # Расширяет список, добавляя в конец все элементы списка L
        for i in L:
            self.append(i)

    def index(self, el, start=0, end=None):  # Возвращает положение первого элемента со значением el
        if not isinstance(el, (int, float)):
            raise TypeError
        elif start >= self._len:
            raise ValueError
        elif not end:
            end = self._len - 1
        elif el == 0:
            if len(self) == len(self._data):
                raise ValueError
            else:
                for i in range(start, end):
                    try:
                        self._data[i]
                    except KeyError:
                        return i
                raise ValueError(f'{el} not in SparseList')
        else:
            for k, v in self._data.items():
                if start <= k < end:
                    if v == el:
                        return k
            else:
                raise ValueError(f'{el} not in SparseList')

    def count(self, value):  # Возвращает количество элементов со значением value
        if not isinstance(value,(int, float)):
            raise TypeError
        elif value == 0:
            return len(self) - len(self._data)
        else:
            count = 0
            for i in self._data.values():
                if value == i:
                    count += 1
            return sum(v == value for v in self._data.values())

    def copy(self):  # Поверхностная копия списка
        copy_list = SparseList()
        copy_list._data = self._data.copy()
        copy_list._len = self._len
        return copy_list

    def insert(self, i, el):   # Вставляет на i-ую позицию значение el
        if not isinstance(i, int):
            raise TypeError
        elif not isinstance(el, (float, int)):
            raise TypeError
        elif i >= self._len:
            self.append(el)
        else:
            ...


    def reverse(self):  # Разворачивает список
        new_list = {}
        len_ = self._len - 1
        for key, val in self._data.items():
            new_list[len_ - key] = val
        self._data = new_list

    def remove(self, value):   # удаляет первый объект из списка. Если такого элемента нет, то возникает ошибка
        if value == self._data.values():
            return
        for _index, _value in self._data.items():
            if value == _value:
                del self._data[_index]
                return
        raise ValueError(f'{value} not in SparseList')

test = Sparse_list()
test.append(3.)
test.append(10.)
test.append(0.)
test.append(2.)
test.append(0.)
test.append(0.)
test.append(5.)
test.append(9.)
test.append(7.)
print(test)  # [3.0, 10.0, 0.0, 2.0, 0.0, 0.0, 5.0, 9.0, 7.0]
test.reverse()
print(test)  # [7.0, 9.0, 5.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0]
test[2] = 14.
print(test)  # [7.0, 9.0, 14.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0]
print(test.index(14., 1, 8)) # 2
print(test.index(0, 1, 8))  # 3
# print(test.index(20., 1, 8))  # ValueError: 20. not in SparseList
new = [9., 14., 0., 0., 14., 0.]
test.extend(new)
print(test)  # [7.0, 9.0, 14.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0, 9.0, 14.0, 0.0, 0.0, 14.0, 0.0]
print(test.count(0.))  # 6
print(test.count(9.))  # 2
print(test.count(20.)) # 0
print(test.pop(2))  # 14.0
print(test)  # [7.0, 9.0, 0.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0, 9.0, 14.0, 0.0, 0.0, 14.0, 0.0]
# print(test.pop(17))  # IndexError: Pop index out of range
del test[1:8:1]
print(test)  # [7.0, 0.0, 0.0, 0.0, 2.0, 14.0, 0.0, 14.0]
test.remove(14.)
print(test)  # [7.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 14.0]
# print(test.remove(20.)) NE VUDAET OSHIBKU






