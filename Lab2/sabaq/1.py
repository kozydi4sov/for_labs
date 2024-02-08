class Dengy():
    def __init__(self, name = 'диане',  balance = 0, deposit  = 0 , dolg = 0, traty = 0):
        self.balance = balance 
        self.deposit = deposit
        self.dolg = dolg
        self.traty = traty
        self.name = name
    def add_balance(self, amount):
        self.balance += amount
        print('ваш баланс:', self.balance)
    def my_dolg(self, money):
        self.dolg += money
        print('вы должны', self.name, self.dolg, 'тенге')
x = int(input('введите сумму:'))
y = Dengy()
y.add_balance(x)
y.my_dolg(x)

