import datetime, time, pygame, sys
# from pygame.locals import *

# FPS = 30
# FramePerSec = pygame.time.Clock()


SCREEN_WIDTH = 1000

SCREEN_HEIGHT = 1000


money = 1000
soldier = 0
weapon = 0
weapon_gan = 1
weapon_name = '모래'
money_take = 100
weapon_ganha_take = 100
def tutorial():
    print("부대모집은 단순히 사람을 뽑는거고 무기강화는 무기를 강화시키는겁니다")
    print("전투력은 부대수 = HP, 무기 = 공격력입니다")
    print("메인화면에서 잔액과 부대수와 무기강화현황을 볼 수 있습니다")
    print("나라를 점령할수록 돈벌기 수익이 증가합니다\n")


def make_money():
    print("1 : 깡노동  2 : 도박")
    main_input = input()
    if main_input == '1': make_money1()
    elif main_input == '2':make_money2ex()

def make_money1():
    global money, money_take
    print("1초에",money_take,"원씩 벌어요")
    money_input = int(input("돈을 벌 시간을 입력하세요(초) : "))
    while True:
        if money_input <= 0:break
        money += money_take
        time.sleep(1)
        money_input -= 1
    print("현재 돈은", money,"원 입니다")

def make_money2ex():
    serve_input = input("1 : 홀짝 게임  2 : 룰렛\n")


def make_soldier():
    global money, soldier
    print("군인 한명당 1000원입니다\n군인을 몇 명 모집하시겠습니까 ")
    soldier_i = int(input())
    if money < soldier_i*1000:
        print("허접~거지")
    else:
        soldier += soldier_i
        money -= soldier_i*1000
        print("현재 군인수는", soldier,"명입니다")

def weapon_wa():
    print("현재 무기는", weapon_name,"입니다\n현재 공격력은", weapon_gan, "입니다")
    serve_input = int(input("1 : 강화\n2 : 돌아가기\n"))
    if serve_input == 1:
        weapon_ganha()

def weapon_ganha():
    global weapon_ganha_take, weapon_gan, weapon, weapon_name
    print(f"현재 강화 수치는 {weapon}입니다\n강화 비용은 {weapon_ganha_take}입니다")
    serve_input = input("강화하시려면 '/강화'를 입력하세요\n강화를 멈추려면'/튀튀'를 입력하세요")
    while True:
        if serve_input == '/튀튀':break
    


print("전쟁 게임에 오신 것을 환영합니다")
print("제작자는 평화주의자입니다")
print("오해 없으시길 바랍니다")

country_name = input("나라 이름을 입력하세요 : ")
main_name = input("유저 이름을 입력하세요 : ")

print("\n'/도움말'을 입력하세요")

while True:
    print("돈 :", money, " 군인 수 :", soldier, " 무기 :", weapon_name)
    print("1: 돈벌기\n2: 부대모집\n3: 무기강화\n4: 전쟁시작\n5: 게임을 끄기")
    main_input = input()
    if main_input == "/도움말":
        tutorial()
    elif main_input == '1':
        make_money()
    elif main_input == '2':
        make_soldier()
    elif main_input == '3':
        weapon_wa()
    elif main_input == '5':
        break


def main():
    pygame.init()
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("세계 전쟁")

    run = True

    while run:
        pass
    return