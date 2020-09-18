import random
print('------------------가위바위보 게임입니다------------------\n\n')
print('5판 3선승제의 가위바위보 게임이며 가위, 바위, 보 셋 중 하나를 내시면 됩니다.\n')

win = 0
lose = 0

def playgame():
    global win
    global lose
    robot = random.randint(1,3)                 #1이 이기는경우, 2가 지는경우, 3이 비기는경우
    player = input('무엇을 내실건가요? : ')
    if robot == 1:
        win = win + 1
        print('이겼습니다!\n 전적 : {} 승 {} 패'.format(win, lose))
               
    elif robot == 2:
        lose = lose + 1
        print('졌습니다 ㅠㅠ\n 전적 : {} 승 {} 패'.format(win, lose))
        
    else:
        print('비겼습니다.\n 전적 : {} 승 {} 패'.format(win, lose))
        playgame()

while (win<3 and lose<3):
    p = playgame()

if win == 3:
    print('이겼습니다!')

if lose == 3:
    print('졌습니다.')










