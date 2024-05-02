import datetime, time, pygame, sys, random
# import PIL.Image
from random import randint
# from pygame.locals import *

# FPS = 30
# FramePerSec = pygame.time.Clock()


SCREEN_WIDTH = 1000

SCREEN_HEIGHT = 1000

money = 1000
soldier = 0
weapon = 0
weapon_gan = 1
weapon_name = {0 : '모래', 1 : '돌', 2 : '나무검', 3 : '돌검'}
money_take = 100
weapon_ganha_take = 100
weapon_random_front = '100%'
weapon_random = randint(1, 100)
weapon_random_back = 100
enemycountry = 0
enemycountry_name = {0 : '일본', 1 : '중국', 2 : '몽골', 3 : '태국'}
enemycountry_defence = {0 : 10, 1 : 30, 2 : 50, 3 : 100}
enemycountry_attack = {0 : 2, 1 : 5, 2 : 10, 3 : 20}

def printline():
    print("\n==============================\n")

def tutorial():
    printline()
    print("부대모집은 단순히 사람을 뽑는거고 무기강화는 무기를 강화시키는겁니다")
    print("전투력은 부대수 = HP, 무기 = 공격력입니다")
    print("메인화면에서 잔액과 부대수와 무기강화현황을 볼 수 있습니다")
    print("나라를 점령할수록 돈벌기 수익이 증가합니다\n")


def make_money():
    printline()
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
    printline()
    serve_input = input("1 : 홀짝 게임  2 : 블랙잭\n")
    if serve_input == '1':
        make_money2()
    elif serve_input == '2':
        make_money3()

def make_money2():
    global money
    printline()
    print("홀짝 게임을 시작합니다!\n성공하신다면 베팅금액을 4배로 획득하실수 있습니다.\n실패하시면 베팅금액을 잃습니다.")
    
    while(True):
        serve_input = input("하시려면 1, 나가시려면 2를 입력하세요\n")
        if serve_input == '2':
            break

        if money <= 0:
            print("돈도 없으면서 뭔 도박이야")
            break

        betting = int(input("베팅 금액을 입력하세요: "))
        user_choice = input("홀수인지 짝수인지 선택하세요 (홀수/짝수): ")
        
        if user_choice not in ['홀수', '짝수']:
            print("제대로 입력도 못하노")
            return

        computer_number = randint(1, 100)
        print(f"컴퓨터가 선택한 숫자는 {computer_number}입니다.")
        
        if (computer_number % 2 == 0 and user_choice == '짝수') or (computer_number % 2 != 0 and user_choice == '홀수'):
            money += betting*4-money
            print("축하합니다! 이겼습니다.")
        else:
            money -= betting
            print("아쉽지만 실패했습니다. 다음 기회에 도전해보세요.")

def make_money3():
    global money
    printline()
    def initialize_deck():
        suits = ['스페이드', '다이아몬드', '하트', '클로버']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(hand):
        value = 0
        num_aces = 0
        for card in hand:
            if card['rank'] in ['J', 'Q', 'K']:
                value += 10
            elif card['rank'] == 'A':
                num_aces += 1
            else:
                value += int(card['rank'])
        value += num_aces
        for i in range(num_aces):
            if value + 11 <= 21:
                value += 11
        return value
    print("블랙잭 게임을 시작합니다!\n성공하시면 배팅금액의 10배로 획득하실수 있습니다\n실패하시면 배팅금액을 잃습니다.")
    while True:
        serve_input = input("하시려면 1, 나가시려면 2를 입력하세요\n")
        if serve_input == '2':
            break

        if money <= 0:
            print("돈도 없으면서 뭔 도박이야")
            break

        betting = int(input("베팅 금액을 입력하세요: "))

        deck = initialize_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print("딜러의 카드:")
        print(f" ** {dealer_hand[1]['rank']} of {dealer_hand[1]['suit']} **")
        print("플레이어의 카드:")
        for card in player_hand:
            print(f" {card['rank']} of {card['suit']}")
        player_hand_value = calculate_hand_value(player_hand)
        dealer_hand_value = calculate_hand_value(dealer_hand)

        while player_hand_value < 21:
            action = input("카드를 더 받으시겠습니까? (y/n): ").lower()
            if action == 'y':
                player_hand.append(deck.pop())
                print(f"플레이어가 받은 카드: {player_hand[-1]['rank']} of {player_hand[-1]['suit']}")
                player_hand_value = calculate_hand_value(player_hand)
                print(f"플레이어의 현재 카드 합계: {player_hand_value}")
            elif action == 'n':
                break

        if player_hand_value > 21:
            print("카드 합계가 21을 넘었습니다. 플레이어 패배!")
            return

        while dealer_hand_value < 17:
            dealer_hand.append(deck.pop())
            dealer_hand_value = calculate_hand_value(dealer_hand)

        print("딜러의 최종 카드:")
        for card in dealer_hand:
            print(f" {card['rank']} of {card['suit']}")
        print(f"딜러의 최종 카드 합계: {dealer_hand_value}")

        if dealer_hand_value > 21 or player_hand_value > dealer_hand_value:
            print("플레이어 승리!")
            money += betting*10-money
        elif dealer_hand_value > player_hand_value:
            print("딜러 승리!")
            money -= betting
        else:
            print("무승부!")


def make_soldier():
    global money, soldier
    printline()
    print("군인 한명당 1000원입니다\n군인을 몇 명 모집하시겠습니까 ")
    soldier_i = int(input())
    if money < soldier_i*1000:
        print("허접~거지")
    else:
        soldier += soldier_i
        money -= soldier_i*1000
        print("현재 군인수는", soldier,"명입니다")


def weapon_ganha():
    global money, weapon_ganha_take, weapon_gan, weapon, weapon_name, weapon_random, weapon_random_back, weapon_random_front
    printline()
    print(f"현재 강화 수치는 {weapon_name[weapon]} {weapon}입니다\n강화 비용은 {weapon_ganha_take}입니다\n강화 확률은 {weapon_random_front}입니다.")
    serve_input = input("강화하시려면 '/강화'를 입력하세요\n강화를 멈추려면'/튀튀'를 입력하세요\n")
    if serve_input == '/강화':
        while True:
            if money - weapon_ganha_take < 0:
                print("돈부터 벌으세요")
                break
            if weapon_random <= weapon_random_back:
                weapon += 1
                if weapon_gan == 1:
                    weapon_gan += 9
                weapon_gan += 10
                money -= weapon_ganha_take
                weapon_ganha_take *= 1.05
                weapon_random_back -= weapon_random_back * 0.21
                weapon_random_front = str(weapon_random_back)+"%"
                print("강화 성공!")
                print(f"현재 강화 수치는 {weapon_name[weapon]} {weapon}입니다\n강화 비용은 {int(weapon_ganha_take)}입니다\n강화 확률은 {weapon_random_front}입니다.")
                serve_input = input("강화하시려면 '/강화'를 입력하세요\n강화를 멈추려면'/튀튀'를 입력하세요\n")
                if serve_input == '/강화':
                    continue
                elif serve_input == '/튀튀':
                    break
                else:
                    print("에러")
            else:
                money -= weapon_ganha_take
                print("강화 실패 ㅋㅋㅋㅋ")
                break
    elif serve_input == '/튀튀':print("에휴")
    else:
        print("뭐라카노")

def war():
    printline()
    while True:
        global enemycountry_defence, soldier
        print(f"이번 나라는 {enemycountry_name[enemycountry]}입니다.")
        print("전쟁을 시작하시려면 1, 나가시려면 2를 입력하세요\n")
        serve_input = int(input(""))
        if serve_input == 1:
            while True:
                printline()
                print(f"{country_name} 군인 수 : {soldier}명  공격력 : {weapon_gan} ==================== {enemycountry_name[enemycountry]} 군인 수 : {enemycountry_defence[enemycountry]}  공격력 : {enemycountry_attack[enemycountry]}")
                if enemycountry_defence[enemycountry] <= 0:
                    printline()
                    print(f"{enemycountry_name[enemycountry]}를 이겼습니다!")
                    break
                if soldier <= 0:
                    printline()
                    print(f"{enemycountry_name[enemycountry]}에게 졌습니다...")
                    if soldier < 0: soldier = 0 
                    break
                enemycountry_defence[enemycountry] -= weapon_gan
                soldier -= enemycountry_attack[enemycountry]
                time.sleep(1)
                printline()

        elif serve_input == 2:
            break
    
printline()

print("전쟁 게임에 오신 것을 환영합니다")
print("제작자는 평화주의자입니다")
print("오해 없으시길 바랍니다")

country_name = input("나라 이름을 입력하세요 : ")
main_name = input("유저 이름을 입력하세요 : ")

print("\n'/도움말'을 입력하세요")

while True:
    printline()
    print(f"국가 이름 : {country_name}  유저 이름 : {main_name}")
    print(f"돈 : {money}  군인 수 : {soldier}  무기 : {weapon_name[weapon]} (공격력 : {weapon_gan})")
    print("1: 돈벌기\n2: 부대모집\n3: 무기강화\n4: 전쟁시작\n5: 게임을 끄기\n")
    main_input = input()
    if main_input == "/도움말":
        tutorial()
    elif main_input == '1':
        make_money()
    elif main_input == '2':
        make_soldier()
    elif main_input == '3':
        weapon_ganha()
    elif main_input == '4':
        war()
    elif main_input == '5':
        break


# def main():
#     pygame.init()
#     display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("세계 전쟁")

#     run = True

#     while run:
#         pass
#     return