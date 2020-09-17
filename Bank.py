class Account:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def deposit(self, amount):
        self.money += amount
        print("-----{0}님의 계좌-----".format(self.name))
        print("{0}원을 입금했습니다.".format(amount))
        print("잔액 : {0}".format(self.money))
