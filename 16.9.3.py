class Client:
    def __init__(self, name, secname, city, money):
        self.name = name
        self.secname = secname
        self.city = city
        self.money = money

    def info(self):
        return f"{self.name} {self.secname} {self.city} {self.money}"

    def party(self):
        return f"{self.name} {self.secname} {self.city}"


client_1 = Client('Иван', 'Петров', 'Москва', 'Баланс: 50 руб')
client_2 = Client('Андрей', 'Шалаев', 'Сызрань', 'Баланс: 50 руб')
client_3 = Client('Максим', 'Воробьев', 'Самара', 'Баланс: 50 руб')
client_4 = Client('Евгений', 'Якушев', 'Воронеж', 'Баланс: 50 руб')

client_list = [client_1, client_2, client_3, client_4]

print(client_1.info())
print(client_1.party())

for client in client_list:
    print(client.party())
