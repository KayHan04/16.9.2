class Client:
    def __init__(self,name,secname,city,money):
        self.name = name
        self.secname = secname
        self.city = city
        self.money = money
    def info(self):
        return f"{self.name} {self.secname} {self.city} {self.money}"
client_1 = Client('Иван','Петров','Москва','Баланс: 50 руб')

print(client_1.info())