import ctypes


class SeriesArray:
    def __init__(self, *argv):
        """
        initial method
        """
        self._volume = 1
        self._num_el = 0
        self._arr = self._create_arr(self._volume)
        self.name = None

    def _create_arr(self, volume):
        """
        creates low level array of specified volume
        :param volume: int
        :return: ctypes object
        """
        return (volume * ctypes.py_object)()

    def copy_arr(self):
        """
        makes a total copy of this array
        :return: SeriesArray
        """
        cp_arr = SeriesArray()
        for i in range(self._num_el):
            cp_arr.append(self._arr[i])
        return cp_arr

    def __setitem__(self, index, value):
        """
        
        :param index: 
        :param value: 
        :return: 
        """
        if index >= self._num_el or index < 0:
            raise IndexError('index out of range')
        self._arr[index] = value

    def __contains__(self, item):
        """
        checks if array contains specified item
        :param item: obj
        :return: boolean
        """
        for i in range(self._num_el):
            if self._arr[i] == item:
                return True
        else:
            return False

    def __iter__(self):
        """
        iterator
        :return: _Iterator
        """
        return _Iterator(self._arr, self._num_el)

    def __len__(self):
        """
        :returns number of elements in array
        :return: int
        """
        return self._num_el

    def __getitem__(self, index):
        """
        :returns the item at specified index
        :param index: int
        :return: obj
        """
        if index >= self._num_el or index < 0:
            raise IndexError('index out of range')
        return self._arr[index]

    def _resize(self, volume):
        """
        resizes the array to specified volume
        :param volume: int
        :return: None
        """
        new_arr = self._create_arr(volume)
        for i in range(self._num_el):
            new_arr[i] = self._arr[i]
        self._arr = new_arr
        self._volume = volume

    def _isFull(self):
        """
        checks if array is full
        :return: boolean
        """
        return self._num_el == self._volume

    def append(self, item):
        """
        appends item to the end of array
        :param item: obj
        :return: None
        """
        if not self._isFull():
            self._arr[self._num_el] = item
            self._num_el += 1
        else:
            self._resize(self._volume * 2)
            self.append(item)

    def remove(self, item):
        """
        removes first instance of specified item
        :param item: obj
        :return: None
        """
        if item not in self._arr:
            raise ValueError("value not found")
        for i in range(self._num_el):
            if self._arr[i] == item:
                for k in range(i, self._num_el - 1):
                    self._arr[k] = self._arr[k + 1]
                self._arr[self._num_el - 1] = None
                self._num_el -= 1
                break

    def insert(self, item, index):
        """
        inserts an element at specified index
        :param item: obj
        :param index: int
        :return: None
        """
        if not isinstance(index, int):
            raise IndexError('invalid index')
        if self._isFull():
            self._resize(self._volume * 2)
        for i in range(self._num_el, index, -1):
            self._arr[i] = self._arr[i - 1]
        self._arr[index] = item
        self._num_el += 1

    def map(self, func):
        """
        map method
        :param func: python function
        :return: None
        """
        for i in range(self._num_el):
            self._arr[i] = func(self._arr[i])

    def __str__(self):
        """
        string representation of array
        :return: str
        """
        s = ""
        for i in range(self._num_el):
            s += str(self._arr[i]) + ", "

        return "[" + s[:-2] + "]"


class _Iterator:
    def __init__(self, arr, num_el):
        self._num_el = num_el
        self._arr = arr
        self._curr_indx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curr_indx < self._num_el:
            el = self._arr[self._curr_indx]
            self._curr_indx += 1
            return el
        else:
            raise StopIteration


if __name__ == '__main__':
    pass