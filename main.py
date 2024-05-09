import datetime, time, sys, random
# import PIL.Image
from random import randint
# import pygame
# from pygame.locals import *

# FPS = 30
# FramePerSec = pygame.time.Clock()


# SCREEN_WIDTH = 1000

# SCREEN_HEIGHT = 1000

money = 1000
soldier = 0
weapon = 0
weapon_gan = 1
weapon_gan_take = 10
weapon_name = {0 : '모래', 1 : '돌', 2 : '나무검', 3 : '돌검', 4 : '낫', 5 : '망치', 6 : '도끼', 7 : '칼', 8 : '노트북', 9 : '톱', 10 : '수류탄', 11 : '조총'
               ,11 : '권총'}
money_take = 100
money_magnification_1 = 4
money_magnification_2 = 10 
weapon_ganha_take = 100
weapon_random_front = '100%'
weapon_random = randint(1, 100)
weapon_random_back = 100
enemycountry = 0
enemycountry_name = {0 : '몽골', 1 : '중국', 2 : '태국', 3 : '캄보디아', 4 : '필리핀', 5 : '일본', 6 : '호주', 7 : '싱가포르', 8 : '몰디브', 9 : '인도', 10 : '네팔',
                     11 : '두바이', 12 : '사우디아라비아', 13 : '케냐', 14 : '마다가스카르', 15 : '남아프리카', 16 : '가나', 17 : '사하라사막', 18 : '이집트', 19 : '터키',
                     20 : '러시아', 21 : '그리스', 22 : '이탈리아', 23 : '모나코', 24 : '스페인', 25 : '프랑스', 26 : '독일', 27 : '덴마크', 28 : '노르웨이', 29 : '영국',
                     30 : '그린란드', 31 : '캐나다', 32 : '뉴욕', 33 : '버뮤다', 34 : '자메이카', 35 : '콜롬비아', 36 : '브라질', 37 : '아르헨티나', 38 : '마추픽추', 39 : '이스터 섬',
                     40 : '멕시코', 41 : 'NASA', 42 : '라스베가스', 43 : '할리우드', 44 : '알래스카',45 : '미국', 46 : '하와이', 47 : '북한', 48 : '한국', 49 : '달', 50 : '화성',
                     51 : '수성', 52 : '금성', 53 : '목성', 54 : '토성', 55 : '천왕성', 56 : '해왕성', 57 : '태양', 58 : '명왕성', 59 : '견우성', 60 : '천랑성', 61 : '직녀성',
                     62 : '알데바란', 63 : '베텔게우스', 64 : '디네프', 65 : '리겔', 66 : '시리우스', 67 : '안드로메다', 68 : '중성자별', 69 : '블랙홀', 70 : '빅뱅'}
enemycountry_defence = {0 : 10, 1 : 30, 2 : 50, 3 : 100, 4 : 200, 5 : 500, 6 : 1000, 7 : 3000, 8 : 5000, 9 : 10000, 10 : 20000, 11 : 40000, 12 : 75000, 13 : 100000}
enemycountry_attack = {0 : 5, 1 : 10, 2 : 20, 3 : 25, 4 : 40, 5 : 100, 6 : 150, 7 : 250, 8 : 500, 9 : 700, 10 : 1000}
enemycountry_soldier_reward = {0 : 2, 1 : 5, 2 : 10, 3 : 30, 4 : 50, 5 : 100, 6 : 200, 7 : 500, 8 : 1000, 9 : 2000}
enemycountry_money_reward = {0 : 1000, 1 : 2000, 2 : 3000, 3 : 4000, 4 : 5000, 5 : 10000, 6 : 20000, 7 : 50000, 8 : 100000, 9 : 200000, 10 : 500000}

def printline():
    print("\n\n==============================\n")

def tutorial():
    printline()
    print("부대모집은 단순히 사람을 뽑는거고 무기강화는 무기를 강화시키는겁니다")
    print("전투력은 부대수 = HP, 무기 = 공격력입니다")
    print("메인화면에서 잔액과 부대수와 무기강화현황을 볼 수 있습니다")
    print("나라를 점령하면 군인과 돈을 얻고 점령할수록 돈벌기 수익이 증가합니다")
    print("나라를 5개 점령하면 도박수익이 증가합니다\n")

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
    print(f"홀짝 게임을 시작합니다!\n성공하신다면 베팅금액을 {money_magnification_1}배로 획득하실수 있습니다.\n실패하시면 베팅금액을 잃습니다.")
    
    while(True):
        print(f"현재 돈 : {money}")
        serve_input = input("하시려면 1, 나가시려면 2를 입력하세요\n")
        if serve_input == '2':
            break

        if money <= 0:
            print("돈도 없으면서 뭔 도박이야")
            break

        betting = int(input("베팅 금액을 입력하세요: "))
        user_choice = input("홀수인지 짝수인지 선택하세요 (홀수/짝수): ")
        
        if user_choice not in ['홀수', '짝수']:
            print("제대로 입력해")
            return

        computer_number = randint(1, 100)
        print(f"컴퓨터가 선택한 숫자는 {computer_number}입니다.")
        
        if (computer_number % 2 == 0 and user_choice == '짝수') or (computer_number % 2 != 0 and user_choice == '홀수'):
            money += betting*money_magnification_1-money
            print("축하합니다! 이겼습니다.")
        else:
            money -= betting
            print("아쉽지만 실패했습니다. 다음 기회에 도전해보세요.")

def make_money3():
    global money
    
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
        for i in range(num_aces):
            if value + 11 <= 21 and num_aces - i == 1: 
                value += 11
            else:
                value += 1
        return value
    
    def card_priority(card):
        if card['rank'] == 'A':
            return 1
        elif card['rank'] in ['K', 'Q', 'J']:
            return 2
        elif card['rank'] in ['10', '9', '8', '7', '6', '5', '4', '3', '2']:
            return int(card['rank'])
        else:
            return 0

    print(f"블랙잭 게임을 시작합니다!\n성공하시면 배팅금액의 {money_magnification_2}배로 획득하실수 있습니다\n실패하시면 배팅금액을 잃습니다\n포기하시면 베팅금액의 절반을 얻습니다.")
    a = 0
    while True:
        if a == 1:
            money -= betting/2
            break
        print(f"현재 돈 : {money}")
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

        print("플레이어의 카드:")
        for card in player_hand:
            print(f" {card['rank']} of {card['suit']}")
            
        player_hand_value = calculate_hand_value(player_hand)
        print(f"플레이어의 현재 카드 합계: {player_hand_value}")

        while player_hand_value < 22:
            action = input("카드를 더 받으시겠습니까?(포기 : f) (y/n/f): ").lower()
            if action == 'y':
                player_hand.append(deck.pop())
                print(f"플레이어가 받은 카드: {player_hand[-1]['rank']} of {player_hand[-1]['suit']}")
                player_hand_value = calculate_hand_value(player_hand)
                print(f"플레이어의 현재 카드 합계: {player_hand_value}")
            elif action == 'n':
                break
            elif action == 'f':
                a = 1
                break

        if player_hand_value > 21:
            print("카드 합계가 21을 넘었습니다. 플레이어 패배!")
            money -= betting
            return

        while True:
            dealer_hand_value = calculate_hand_value(dealer_hand)
            if dealer_hand_value >= 17:
                break
            dealer_hand.append(deck.pop())

        print("딜러의 최종 카드:")
        for card in dealer_hand:
            print(f" {card['rank']} of {card['suit']}")
        print(f"딜러의 최종 카드 합계: {dealer_hand_value}")

        if dealer_hand_value > 21 or player_hand_value > dealer_hand_value:
            print("플레이어 승리!")
            money += betting * money_magnification_2 - money
        elif dealer_hand_value > player_hand_value:
            print("딜러 승리!")
            money -= betting
        else:
            player_priority = max([card_priority(card) for card in player_hand])
            dealer_priority = max([card_priority(card) for card in dealer_hand])

            if player_priority > dealer_priority:
                print("플레이어 승리!")
                money += betting * money_magnification_2 - money
            elif player_priority < dealer_priority:
                print("딜러 승리!")
                money -= betting
            else:
                print("무승부")
        


def make_soldier():
    global money, soldier
    printline()
    print("군인 한명당 1000원입니다\n군인을 몇 명 모집하시겠습니까 ")
    soldier_i = int(input())
    if money < soldier_i*1000:
        print("허접~ 거지주제에 군인이라니")
    else:
        soldier += soldier_i
        money -= soldier_i*1000
        print("현재 군인수는", soldier,"명입니다")


def weapon_ganha():
    global money, weapon_ganha_take, weapon_gan, weapon, weapon_name, weapon_random_back, weapon_random_front, weapon_gan_take
    
    printline()
    while True:
        print(f"현재 강화 수치는 {weapon_name[weapon]} ({weapon})입니다\n강화 비용은 {int(weapon_ganha_take)}입니다\n강화 확률은 {weapon_random_front}입니다.")
        print(f"현재 돈 : {int(money)}")
        serve_input = input("강화하시려면 '/강화'를 입력하세요\n강화를 멈추려면 '/튀튀'를 입력하세요\n")

        if serve_input == '/강화':
            if money - weapon_ganha_take < 0:
                print("돈부터 벌으세요")
                return

            weapon_random = randint(1, 100)
            money -= int(weapon_ganha_take)
            if weapon_random <= weapon_random_back:
                weapon += 1
                if weapon_gan == 1:
                    weapon_gan += int(weapon_gan_take)
                if weapon < 10:
                    weapon_gan_take *= 1.2
                    weapon_ganha_take *= 1.1
                elif weapon < 20:
                    weapon_gan_take *= 1.5
                    weapon_ganha_take *= 1.5
                elif weapon < 30:
                    weapon_gan_take *= 1.7
                    weapon_ganha_take *= 1.8
                weapon_random_back -= weapon_random_back * 0.2
                weapon_random_front = str(weapon_random_back) + "%"
                print("\n강화 성공!")
                printline()
            else:
                money -= weapon_ganha_take
                print("\n강화 실패 ㅋㅋㅋㅋ")
                printline()
            
        elif serve_input == '/튀튀':
            print("에휴")
            break
        else:
            print("뭐라카노")


def war():
    global enemycountry_defence, soldier, enemycountry, money, money_take, money_magnification_1, money_magnification_2
    printline()
    tmp = enemycountry_defence[enemycountry]
    while True:
        print(f"이번 나라는 {enemycountry_name[enemycountry]}입니다.")
        print("전쟁을 시작하시려면 1, 나가시려면 2를 입력하세요\n")
        serve_input = int(input(""))
        if serve_input == 1:
            while True:
                printline()
                if enemycountry_defence[enemycountry] < 0:
                    enemycountry_defence[enemycountry] = 0
                print(f"{country_name} 군인 수 : {soldier}명  공격력 : {weapon_gan} ==================== {enemycountry_name[enemycountry]} 군인 수 : {enemycountry_defence[enemycountry]}  공격력 : {enemycountry_attack[enemycountry]}")
                if enemycountry_defence[enemycountry] <= 0:
                    printline()
                    print(f"{enemycountry_name[enemycountry]}를 이겼습니다!")
                    soldier += enemycountry_soldier_reward[enemycountry]
                    money += enemycountry_money_reward[enemycountry]
                    print(f"군인 {enemycountry_soldier_reward[enemycountry]}명과  돈 {enemycountry_money_reward[enemycountry]}원을 얻었습니다")
                    money_take += 10
                    if (enemycountry+1) % 5 == 0:
                        money_magnification_1 += 1
                        money_magnification_2 += 1
                    enemycountry += 1
                    break
                if soldier <= 0:
                    printline()
                    if soldier < 0: soldier = 0 
                    print(f"{enemycountry_name[enemycountry]}에게 졌습니다...")
                    enemycountry_defence[enemycountry] = tmp
                    break
                enemycountry_defence[enemycountry] -= weapon_gan
                soldier -= enemycountry_attack[enemycountry]
                time.sleep(1)
                printline()

        elif serve_input == 2:
            print("에휴")
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
    print(f"돈 : {int(money)}  군인 수 : {soldier}  무기 : {weapon_name[weapon]} (공격력 : {int(weapon_gan)})")
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