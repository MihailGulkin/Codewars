class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.array = []
        self.__page_count = items_per_page
        count = 0
        mass = []
        collection = list(collection)
        while len(collection):
            if count == items_per_page:
                self.array.append(mass)
                mass = []
                count = 0
            mass.append(collection[0])
            collection.pop(0)
            count += 1
        self.array.append(mass)

    def item_count(self):
        return sum(len(page) for page in self.array)

    def page_count(self):
        return sum(1 for _ in self.array)

    def page_item_count(self, page_index):
        try:
            return len(self.array[page_index])
        except:
            return -1

    def page_index(self, item_index):
        if (len(self.array[0]) == 0 or item_index < 0):
            return -1
        if (item_index / self.__page_count <= len(self.array)):
            try:
                temp_mass = []
                for i in self.array:
                    temp_mass += i
                temp_mass[item_index]
            except:
                return -1
            return item_index // self.__page_count
        return -1
