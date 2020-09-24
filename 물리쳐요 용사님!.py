import random
class gamePlay:
    def __init__(self, name):
        self.name = name
        self.PlayerAtk = random.randint(0, 100)
        self.gold = 0
        self.MonAtk = random.randint(0, 100)
        self.result = 10 * random.randint(1, 10)

    def store(self):
        print('현재 보유하고있는 골드는 %dG 입니다.' % self.gold)
        arm = input('구매하실 무기를 골라주세요. 1.안쎈검 10G 2.그냥검 20G 3.쎈검 30G 4.짱쎈검 100G\n')
        print('무기는 그 금액만큼 공격력을 올려줍니다')
        if arm == 1:
            if self.gold >= 10:
                print('안쎈검을 구매하셨습니다! 공격력이 10 상승합니다')
                self.PlayerAtk = self.PlayerAtk + 10
                self.gold = self.gold - 10
            else:
                print('골드가 부족합니다.')
        elif arm == 2:
            if self.gold >= 20:
                print('그냥검을 구매하셨습니다! 공격력이 20 상승합니다')
                self.PlayerAtk = self.PlayerAtk + 20
                self.gold = self.gold - 20
            else:
                print('골드가 부족합니다.')
        elif arm == 3:
            if self.gold >= 30:
                print('쎈검을 구매하셨습니다! 공격력이 30 상승합니다')
                self.PlayerAtk = self.PlayerAtk + 30
                self.gold = self.gold - 30
            else:
                print('골드가 부족합니다.')
        elif arm == 4:
            if self.gold >= 100:
                print('짱쎈검을 구매하셨습니다! 공격력이 100 상승합니다')
                self.PlayerAtk = self.PlayerAtk + 100
                self.gold = self.gold - 100
            else:
                print('골드가 부족합니다.')

    def battle(self):
        if self.MonAtk < self.PlayerAtk:
            self.gold += self.result
            print('전투에서 승리했습니다! ')
            print('%dG를 획득하였습니다. 남은 골드는 %dG 입니다.' % (self.result, self.gold))
        elif self.MonAtk < self.PlayerAtk:
            self.gold -= self.result
            print('전투에서 패배했습니다. ')
            print('%dG를 잃었습니다. 남은 골드는 %dG 입니다.' % (self.result, self.gold))
        else:
            print('전투에서 비겼습니다.')
            print('남은 골드는 %dG 입니다.' % self.gold)

player = input('유저명을 입력하세요 : ')
a = gamePlay(player)
print('유저명이 %s로 설정되었습니다.' % player)

