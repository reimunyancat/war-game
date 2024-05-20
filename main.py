import time
import random
# import pygame
# from pygame.locals import *
from random import randint
# import datetime
# import sys
# import PIL.Image
import json

# FPS = 30
# FramePerSec = pygame.time.Clock()


# SCREEN_WIDTH = 1000

# SCREEN_HEIGHT = 1000

money = 1000
soldier = 0
weapon = 0
weapon_gan = 1
weapon_gan_take = 10
money_take = 100
money_magnification_1 = 4
money_magnification_2 = 10 
weapon_ganha_take = 100
weapon_random_front = '100%'
weapon_random = randint(1, 100)
weapon_random_back = 100
enemycountry = 0

class EnemyCountry:
    def __init__(self, name, defence, attack, soldier_reward, money_reward):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.soldier_reward = soldier_reward
        self.money_reward = money_reward

soldier_display = ""
money_display = ""

def load_data_from_json(filename):
    """JSON 파일에서 데이터를 로드합니다."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

weapon_name = load_data_from_json('Scripts/weapons.json')
enemy_coutries = load_data_from_json('Scripts/enemy_countries.json')

def back(betting):
    if betting <= 0:
        print("\aYou are an idiot")
        return False
    return True

def printline():
    print("\n\n==============================\n")

def tutorial():
    printline()
    print("부대모집은 군인을 사는거고 무기강화는 무기를 강화시키는겁니다")
    print("전투력은 군인수 = HP, 무기 = 공격력입니다")
    print("메인화면에서 잔액과 부대수와 무기강화현황을 볼 수 있습니다")
    print("나라를 점령하면 군인과 돈을 얻고 점령할수록 돈벌기 수익이 증가합니다")
    print("나라를 5개 점령하면 도박수익이 증가합니다\n")

def soldier_display_f():
    display_str = f"{soldier:,}"
    return display_str

def money_display_f():
    display_str = f"{money:,}"
    return display_str

def make_money():
    printline()
    print("1 : 깡노동  2 : 도박")
    main_input = input()
    if main_input == '1': make_money1()
    elif main_input == '2':make_money2ex()

def make_money1():
    global money
    print("1초에",money_take,"원씩 벌어요")
    money_input = int(input("돈을 벌 시간을 입력하세요(초) : "))
    while True:
        if money_input <= 0:break
        money += money_take
        time.sleep(1)
        money_input -= 1
        money_display_f()
    print("현재 돈은", money_display,"원 입니다")

def make_money2ex():
    printline()
    serve_input = input("1 : 홀짝 게임  2 : 블랙잭\n")
    if serve_input == '1':
        make_money2()
    elif serve_input == '2':
        make_money3()

def make_money2():
    global money, money_display
    printline()
    print(f"홀짝 게임을 시작합니다!\n성공하신다면 베팅금액을 {money_magnification_1}배로 획득하실수 있습니다.\n실패하시면 베팅금액을 잃습니다.")
    
    while(True):
        money_display = money_display_f()
        print(f"현재 돈 : {money_display}")
        serve_input = input("하시려면 1, 나가시려면 2를 입력하세요\n")
        if serve_input == '2':
            break

        if money <= 0:
            print("돈도 없으면서 뭔 도박이야")
            break

        betting = int(input("베팅 금액을 입력하세요: "))
        if not back(betting):
            continue

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
    global money, money_display
    
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
    while True:
        forgive = 0
        money_display = money_display_f()
        print(f"현재 돈 : {money_display}")
        serve_input = input("하시려면 1, 나가시려면 2를 입력하세요\n")
        if serve_input == '2':
            break

        if money <= 0:
            print("You are an idiot")
            break

        betting = int(input("베팅 금액을 입력하세요: "))
        if not back(betting):
            continue

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
                print("허접~")
                forgive = 1
                break

        if forgive == 1:
            money -= int(betting/2)
            break
        else:
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
    money_display = money_display_f()
    print(f"현재 돈 : {money_display}\n")
    print("1 : 군인(1,000원)  2 : 탱크(1,000,000원) 3 : 전투기(1,000,000,000원) 4 : 핵미사일(1,000,000,000,000,000원)")
    military = int(input())
    if military == 1:
        print("군인 한명당 1,000원입니다\n군인을 몇 명 모집하시겠습니까")
        soldier_i = int(input())
        if not back(soldier_i):
            print("You are an idiot")

        elif money < soldier_i*1000:
            print("허접~ 거지주제에 군인이라니")
        else:
            soldier += soldier_i
            money -= soldier_i*1000000
            soldier_display = soldier_display_f()
            print("현재 군인수는", soldier_display,"명입니다")

    elif military == 2:
        print("탱크 한대당 1,000,000원입니다\n군인은 1,200명이 모집됩니다\n탱크를 몇 개 사시겠습니까")
        soldier_i = int(input())
        if not back(soldier_i):
            print("You are an idiot")

        elif money < soldier_i*1000000:
            print("허접~ 거지주제에 탱크라니")
        else:
            soldier += soldier_i*1200
            money -= soldier_i*1000000
            soldier_display = soldier_display_f()
            print("현재 군인수는", soldier_display,"명입니다")

    elif military == 3:
        print("전투기 한대당 1,000,000,000원입니다\n군인은 1,500,000명이 모집됩니다\n전투기를 몇 개 사시겠습니까")
        soldier_i = int(input())
        if not back(soldier_i):
            print("You are an idiot")

        elif money < soldier_i*1000000000:
            print("허접~ 거지주제에 전투기라니")
        else:
            soldier += soldier_i*1500000
            money -= soldier_i*1000000000
            soldier_display = soldier_display_f()
            print("현재 군인수는", soldier_display,"명입니다")
    
    elif military == 4:
        print("핵미사일 한개당 1,000,000,000,000,000원입니다\n군인은 15,000,000,000,000명이 모집됩니다\n핵미사일을 몇 개 사시겠습니까")
        soldier_i = int(input())
        if not back(soldier_i):
            print("You are an idiot")

        elif money < soldier_i*1000000000000000:
            print("허접~ 거지주제에 전투기라니")
        else:
            soldier += soldier_i*15000000000000
            money -= soldier_i*1000000000000000
            soldier_display = soldier_display_f()
            print("현재 군인수는", soldier_display,"명입니다")

def weapon_ganha():
    global money, weapon_ganha_take, weapon_gan, weapon, weapon_name, weapon_random_back, weapon_random_front, weapon_gan_take
    
    printline()
    while True:
        money_display = money_display_f()
        print(f"현재 강화 수치는 {weapon_name[weapon]} ({weapon})입니다\n강화 비용은 {int(weapon_ganha_take)}입니다\n강화 확률은 {weapon_random_front}입니다.")
        print(f"현재 돈 : {money_display}")
        serve_input = input("강화하시려면 '/강화'를 입력하세요\n강화를 멈추려면 '/튀튀'를 입력하세요\n")

        if serve_input == '/강화':
            if money - weapon_ganha_take < 0:
                print("You are an idiot")
                return

            weapon_random = randint(1, 100)
            money -= int(weapon_ganha_take)
            if weapon_random <= weapon_random_back:
                weapon += 1
                if weapon == 1:
                    weapon_gan = 5
                if weapon < 10:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 1.3
                    weapon_ganha_take *= 1.2
                elif weapon < 20:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 1.7
                    weapon_ganha_take *= 1.8
                elif weapon < 30:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 2.3
                    weapon_ganha_take *= 2.5
                elif weapon < 40:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 2.9
                    weapon_ganha_take *= 3.2
                elif weapon < 50:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 3.5
                    weapon_ganha_take *= 4
                elif weapon < 60:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 4.2
                    weapon_ganha_take *= 5
                elif weapon < 70:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 5
                    weapon_ganha_take *= 6
                elif weapon < 80:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 6
                    weapon_ganha_take *= 7.5
                elif weapon < 90:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 7.5
                    weapon_ganha_take *= 9
                elif weapon < 100:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 9
                    weapon_ganha_take *= 10.5
                elif weapon == 100:
                    weapon_gan_take *= 10000000000
                    weapon_ganha_take *= 100000000
                    weapon_gan += int(weapon_gan_take)
                tmp = int(weapon_random_back) - int(weapon_random_back) * 0.94
                weapon_random_back -= int(tmp)
                weapon_random_front = str(weapon_random_back) + "%"
                print("\n강화 성공!")
                printline()
            else:
                money -= int(weapon_ganha_take)
                print("\n강화 실패 ㅋㅋㅋㅋ")
                printline()
            
        elif serve_input == '/튀튀':
            print("에휴")
            break
        else:
            print("뭐라카노")


def war():
    global soldier, enemycountry, money, money_take, money_magnification_1, money_magnification_2, enemy_countries
    
    while True:
        printline()
        print(f"이번 나라는 {enemy_countries[enemycountry].name}입니다.")
        print("전쟁을 시작하시려면 1, 나가시려면 2를 입력하세요\n")
        serve_input = int(input(""))
        if serve_input == 1:
            while True:
                printline()
                if enemy_countries[enemycountry].defence < 0:
                    enemy_countries[enemycountry].defence = 0
                print(f"{country_name} 군인 수 : {soldier}명  공격력 : {weapon_gan} " + "=" * 15 + f" {enemy_countries[enemycountry].name} 군인 수 : {enemy_countries[enemycountry].defence}  공격력 : {enemy_countries[enemycountry].attack}")

                if enemy_countries[enemycountry].defence < 0:
                    enemy_countries[enemycountry].defence = 0

                if enemy_countries[enemycountry].defence == 0:
                    printline()
                    print(f"{enemy_countries[enemycountry].name}를 이겼습니다!")
                    soldier += enemy_countries[enemycountry].soldier_reward
                    money += enemy_countries[enemycountry].money_reward
                    print(f"군인 {enemy_countries[enemycountry].soldier_reward}명과  돈 {enemy_countries[enemycountry].money_reward}원을 얻었습니다")
                    money_take += 10
                    if (enemycountry+1) % 5 == 0:
                        money_magnification_1 += 1
                        money_magnification_2 += 1
                    enemycountry += 1
                    break
                if soldier < 0:
                    soldier = 0 

                if soldier == 0:
                    printline()
                    print(f"{enemy_countries[enemycountry].name}의 공격에 의해 패배하였습니다.")
                    break
                soldier -= enemy_countries[enemycountry].attack
                enemy_countries[enemycountry].defence -= weapon_gan
                time.sleep(1)
        else: 
            print("에휴")
            break

    
printline()

print("전쟁 게임에 오신 것을 환영합니다")
print("제작자는 평화주의자입니다")
print("오해 없으시길 바랍니다")

country_name = input("나라 이름을 입력하세요 : ")
main_name = input("유저 이름을 입력하세요 : ")

print("\n'/도움말'을 입력하세요")

def menu():
    money_display = money_display_f()
    soldier_display = soldier_display_f()
    printline()
    print(f"국가 이름 : {country_name}  유저 이름 : {main_name}\n")
    print(f"돈 : {money_display}원\n군인 수 : {soldier_display}\n무기 : {weapon_name[weapon]} (공격력 : {weapon_gan})\n")
    print("1: 돈벌기  2: 부대모집  3: 무기강화  4: 전쟁시작  5: 게임종료")
    main_input = input()
    if main_input == "/도움말": tutorial()
    elif main_input == '1': make_money()
    elif main_input == '2': make_soldier()
    elif main_input == '3': weapon_ganha()
    elif main_input == '4': war()
    elif main_input == '5': exit()

def ending(enemy_country_index):
    if enemy_country_index == 70:
        print("축하드립니다")
        exit()

def main():
    while True:
        menu()
        ending(enemycountry)

if __name__ == '__main__':
    main()

# def main():
#     pygame.init()
#     display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("세계 전쟁")

#     run = True

#     while run:
#         pass
#     return
