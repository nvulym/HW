class Sparse_list():
    def __init__(self):
        self._data = {}  # {ind:num}
        self._len = 0  # max ind

    def __len__(self):
        return self._len

    def __repr__(self):  # вернет строку, содержащую печатаемое формальное представление объекта => список с 0
        temp = [0.] * self._len
        for k, v in self._data.items():
            temp[k] = v
        return str(temp)

    def __iter__(self):
        for i in range(self._len):
            yield self._data.get(i, 0)

    def __setitem__(self, ind, value):
        if isinstance(ind, int) and isinstance(value, (float, int)):
            if ind < 0:
                ind = self._len + ind
            elif ind >= self._len:
                raise IndexError("List index out of range")
            if value != 0:  # список не должен содержать 0
                self._data[ind] = value
            else:
                try:
                    del self._data[ind]
                except KeyError:
                    pass
        elif isinstance(ind, slice):
            start, stop, step = ind.indices(self._len)
            if step == 1:
                if isinstance(value, (int, float)):
                    del self[start:stop]
                    self.insert(start, value)
                elif isinstance(value, (list, Sparse_list)):
                    del self[start:stop]
                    for i in reversed(value):
                        self.insert(start, i)
                else:
                    raise TypeError
            else:
                if isinstance(value, (list, Sparse_list)):
                    if len(range(start, stop, step)) != len(value):
                        raise ValueError('Attempt to assign sequence to extended slice with not same size')
                    else:
                        iter_value = iter(value)
                        for i in range(start, stop, step):
                            del self[i]
                            self.insert(i, next(iter_value))
                else:
                    raise TypeError
        else:
            raise TypeError

    def __getitem__(self, ind):
        if isinstance(ind, int):
            if ind < 0:
                ind = self._len + ind
            elif ind > self._len:
                raise IndexError('List index out of range')
            return self._data.get(ind, 0)
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
        if isinstance(ind, int):
            if ind < 0:
                ind = self._len + ind
            elif ind > self._len:
                raise IndexError('List index out of range')
            try:
                del self._data[ind]
                for i in range(ind+1, self._len):
                    self._data[i-1] = self._data.pop(i)
            except KeyError:
                pass
            self._len -= 1
        elif isinstance(ind, slice):
            start, stop, step = ind.indices(self._len)
            if step > 0:
                start, stop, step = stop - 1, start - 1, -step
            for i in range(start, stop, step):
                del self[i]
        else:
            raise TypeError

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

    def index(self, el, start=None, end=None):  # Возвращает положение первого элемента со значением el
        if not isinstance(el, (int, float)):
            raise TypeError
        elif start >= self._len:
            raise ValueError
        if not end:
            end = self._len - 1
        for i in range(start, end):
            if self._data.get(i, 0) == el:
                return i
        raise ValueError(f'{el} is not in list')

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
        copy_list = Sparse_list()
        copy_list._data = self._data.copy()
        copy_list._len = self._len
        return copy_list

    def insert(self, i, el):   # Вставляет на i-ую позицию значение el
        if not isinstance(i, int):
            raise TypeError
        elif not isinstance(el, (int, float)):
            raise TypeError
        elif i >= self._len:
            self.append(el)
        else:
            if i < 0:
                i = self._len + i
                if i < 0:
                    i = 0
            temp_dict = {}
            for ind, val in self._data.items():
                if ind >= i:
                    temp_dict[ind+1] = val
                else:
                    temp_dict[ind] = val
            self._data = temp_dict
            self._data[i] = el
            self._len += 1

    def reverse(self):  # Разворачивает список
        new_list = {}
        len_ = self._len - 1
        for key, val in self._data.items():
            new_list[len_ - key] = val
        self._data = new_list

    def remove(self, value):   # удаляет первый объект из списка. Если такого элемента нет, то возникает ошибка
        if not isinstance(value, (int, float)):
            raise TypeError
        for i in range(self._len):
            if self._data.get(i, 0) == value:
                self.pop(i)
                return
        raise ValueError(f'{value} not in list')

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
# # del test[2:7:2]
# # print(test)  # [3.0, 10.0, 2.0, 0, 9.0, 7.0]
# test.reverse()
# print(test)  # [7.0, 9.0, 5.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0]
# test[2] = 14.
# print(test)  # [7.0, 9.0, 14.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0]
# print(test.index(14., 1, 8)) # 2
# print(test.index(0, 1, 8))  # 3
# # print(test.index(20., 1, 8))  # ValueError: 20. not in SparseList
# new = [9., 14., 0., 0., 14., 0.]
# test.extend(new)
# print(test)  # [7.0, 9.0, 14.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0, 9.0, 14.0, 0.0, 0.0, 14.0, 0.0]
# print(test.count(0.))  # 6
# print(test.count(9.))  # 2
# print(test.count(20.)) # 0
# print(test.pop(2))  # 14.0
# print(test)  # [7.0, 9.0, 0.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0, 9.0, 14.0, 0.0, 0.0, 14.0, 0.0]
# # print(test.pop(17))  # IndexError: Pop index out of range
# test.remove(14.)
# print(test)  # [7.0, 9.0, 0.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0, 9.0, 0.0, 0.0, 0.0, 14.0, 0.0]
# # test.remove(20.)  # ValueError: 20.0 not in list
# test.insert(3, 50.)
# print(test)  # [7.0, 9.0, 0.0, 50.0, 0.0, 0.0, 2.0, 0.0, 10.0, 3.0, 9.0, 0.0, 0.0, 0.0, 14.0, 0.0]





