from dataclasses import dataclass
import Question_1_SQL as SQL

@dataclass
class Product:
    code: str
    name: str
    price: float

    def __str__(self):
        return f"{self.code} {self.name} {self.price:.2f}"


@dataclass
class Category:
    catID: int
    name: str


class CategoryList:
    def __init__(self):
        self._catList = []

    def _add(self, new_cat: Category):
        self._catList.append(new_cat)

    def create(self):
        cats = SQL.get_categories()
        for cat in cats:
            new_cat = Category(cat[0], cat[1])
            self._add(new_cat)
