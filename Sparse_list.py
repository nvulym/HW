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

    def __delitem__(self, ind):
        pass

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

    def index(self, el, start=None, end=None): # Возвращает положение первого элемента со значением el
        if not isinstance(el, (int, float)):
            raise TypeError
        if not start:
            start = 0
        if not end:
            end = self._len - 1
        for i in range(start, end):
            if self._data.get(i, 0) == el:
                return i
        else:
            raise ValueError(f'{el} is not in list')

    def count(self, el):  # Возвращает количество элементов со значением el
        if isinstance(el, (int, float)):
            if el == 0:
                return self._len - len(self._data)
            for value in self._data.values():
                count = 0
                if value == element:
                    count += 1
            return count
        else:
             raise TypeError

    def copy(self):  # Поверхностная копия списка
        copy_list = SparseList()
        copy_list._data = self._data.copy()
        copy_list._len = self._len
        return copy_list

    def insert(self, i, el):   # Вставляет на i-ую позицию значение el
        pass

    def reverse(self):  # Разворачивает список
        new_list = {}
        len_ = self._len - 1
        for key, val in self._data.items():
            new_list[len_ - key] = val
        self._data = new_list

    def remove(self, el):   # удаляет первый объект из списка. Если такого элемента нет, то возникает ошибка
        pass
        # if not isinstance(el,(int, float)):
        #     raise TypeError
        # del self[self.index(el)]

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
del test[1:6:3]
print(test)  # [3.0, 0.0, 2.0, 0.0, 5.0, 9.0, 7.0]
test.reverse()
print(test)  # [7.0, 9.0, 5.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0]
test[2] = 14.
print(test)  # [7.0, 9.0, 14.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0]
print(test.index(14., 1, 8)) # 2
new = [9., 14., 0., 0., 14., 0.]
test.extend(new)
print(test)  # [7.0, 9.0, 14.0, 0.0, 2.0, 0.0, 3.0, 9.0, 14.0, 0.0, 0.0, 14.0, 0.0]
print(test.count(0.))  # 5
test.pop(2)
print(test)  # [7.0, 9.0, 0.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0, 9.0, 14.0, 0.0, 0.0, 14.0, 0.0]
test.pop(17)
print(test)  # IndexError: Pop index out of range
test.remove(10.)  # NE RABOTAET
print(test)





