class Sneakers:
    def __init__(self, brand, size, color, material, price, quantity, number_of_sales):
        self.brand = brand
        self.size = size
        self.color = color
        self.material = material
        self.price = price
        self.quantity = quantity
        self.number_of_sales = number_of_sales

    def __str__(self):
        return f"{self.brand} ({self.size} см, {self.color}, {self.material}): ціна {self.price} грн, кількість: {self.quantity}, продано: {self.number_of_sales}"


class SportShoesStore:
    def __init__(self):
        self.inventory = []

    def create_inventory(self, sneakers):
        self.inventory.append(sneakers)

    def sort_by_price(self):
        self.inventory.sort(key=lambda sneakers: sneakers.price)

    def sort_by_quantity(self):
        self.inventory.sort(key=lambda sneakers: sneakers.quantity)

    def sort_by_sales(self):
        self.inventory.sort(key=lambda sneakers: sneakers.number_of_sales, reverse=True)

    # виведення інформації про взуття
    def show_inventory(self, title, inventory):
        print(title)
        for sneaker in inventory:
            print(sneaker)

    def show_all_sneakers(self):
        self.show_inventory("Асортимент взуття в магазині:", self.inventory)

    def show_sorted_by_price(self):
        self.sort_by_price()
        self.show_inventory("\nВзуття за ціною:", self.inventory)

    def show_sorted_by_quantity(self):
        self.sort_by_quantity()
        self.show_inventory("\nКількість взуття в магазині:", self.inventory)

    def show_top_sellers(self):
        self.sort_by_sales()
        self.show_inventory("\nТоп продажів:", self.inventory)


sneakers1 = Sneakers("Nike", "37-42", "чорний", "шкіра", 3000, "500", 500)
sneakers2 = Sneakers("Adidas", "39-45", "білий", "синтетика", 4500, "400", 800)
sneakers3 = Sneakers("Crocs", "36-47", "кольоровий", "резина", 2000, "300", 1200)

shop = SportShoesStore()
shop.create_inventory(sneakers1)
shop.create_inventory(sneakers2)
shop.create_inventory(sneakers3)

shop.show_all_sneakers()
shop.show_sorted_by_price()
shop.show_sorted_by_quantity()
shop.show_top_sellers()
