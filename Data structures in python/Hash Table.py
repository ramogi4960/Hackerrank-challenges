""" Let's implement hash tables """


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None, ] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def __setitem__(self, key, value):
        index = self.__hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def __getitem__(self, item):
        index = self.__hash(item)
        if not self.data_map[index]:
            return 'The index has not item'
        else:
            for x in self.data_map[index]:
                if x[0] == item:
                    return x[1]

    def keys(self):
        for item in self.data_map:
            if not item:
                print('None')
            else:
                for i in item:
                    print(f"key:{i[0]}, Value:{i[1]}", end='--')

    def print_table(self):
        for key, value in enumerate(self.data_map):
            print(f"{key}:{value}")


x = HashTable()
x.__setitem__('bolts', 1400)
x.__setitem__('washers', 50)
x.__setitem__('lumber', 70)
x.keys()

""" Why do some methods start and end with '__'?? """

