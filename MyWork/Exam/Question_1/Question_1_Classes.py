from dataclasses import dataclass
import Question_1_SQL as SQL


@dataclass
class Product:
    code: str
    name: str
    price: float

    def __str__(self):
        return f"{self.code:<12}{self.name:<40}{self.price:.2f}"


class ProductList:
    def __init__(self):
        self.products = []

    def _add_product(self, new_prod: Product):
        """
        Adds a new product to the list.
        """
        self.products.append(new_prod)

    def create(self, cat_id: int):
        """
        Adds all products of chosen category ID in the database to the list.

        :param cat_id:
        :return:
        """
        prods = SQL.view_prod(cat_id)
        for prod in prods:
            new_prod = Product(prod[0], prod[1], prod[2])
            self._add_product(new_prod)


@dataclass
class Category:
    catID: int
    name: str


class CategoryList:
    def __init__(self):
        self.catList = []

    def _add(self, new_cat: Category):
        """
        Adds a new category to the list.
        """
        self.catList.append(new_cat)

    def create(self):
        """
        Adds all categories from the database to the list.
        """
        cats = SQL.get_categories()
        for cat in cats:
            new_cat = Category(cat[0], cat[1])
            self._add(new_cat)
