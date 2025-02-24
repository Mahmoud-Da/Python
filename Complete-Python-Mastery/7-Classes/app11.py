class Product:

    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f"{self.price}"


product = Product(-50)
print(product)
# -50


class Product1:

    def __init__(self, price):
        # self.__price = price
        self.set_price(price)

    def __str__(self):
        return f"{self.__price}"

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self.__price = value


product = Product1(-50)
print(product)

# raise ValueError("Price can't be negative")
# ValueError: Price can't be negative


class Product2:

    def __init__(self, price):
        self.set_price(price)

    def __str__(self):
        return f"{self.__price}"

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self.__price = value

    price = property(get_price, set_price)


product = Product2(10)
print(product.price)
# 10


product = Product2(10)
product.price = -1
print(product.price)
# raise ValueError("Price can't be negative")
# ValueError: Price can't be negative

# product.get_price
# product.set_price


class Product3:

    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f"{self.__price}"

    # def __get_price(self):
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self.__price = value


product = Product3(-10)
print(product.price)
# raise ValueError("Price can't be negative")
# ValueError: Price can't be negative
