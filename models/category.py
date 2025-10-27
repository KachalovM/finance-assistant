class Category:
    '''Класс для представления категорий.'''

    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return f"Category({self.category})"