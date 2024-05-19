import time
import random
# import pygame
# from pygame.locals import *
from random import randint
# import datetime
# import sys
# import PIL.Image

# FPS = 30
# FramePerSec = pygame.time.Clock()


# SCREEN_WIDTH = 1000

# SCREEN_HEIGHT = 1000

money = 1000
soldier = 0
weapon = 0
weapon_gan = 1
weapon_gan_take = 10
weapon_name = {
    0: '모래', 1: '돌', 2: '나무검', 3: '돌검', 4: '낫', 5: '망치', 6: '도끼', 7: '칼', 8: '노트북', 9: '톱', 10: '수류탄',
    11: '조총', 12: '권총', 13: '자동권총', 14: '소총', 15: '돌격소총', 16: '기관총', 17: '저격총', 18: '탱크', 19: '전함', 20: '전투기',
    21: '폭격기', 22: '포탄', 23: '화염방사기', 24: '레이저 무기', 25: 'EMP 발사기', 26: '드론', 27: '사이버 공격 장비', 28: '위성 무기', 29: '양자 무기',
    30: '바이오 무기', 31: '전자기 펄스', 32: '중력 폭탄', 33: '플라즈마 총', 34: '핵 미사일', 35: '안티 매터 폭탄', 36: '다크 매터 폭탄', 37: '시간 왜곡 장치', 38: '차원 이동 장치', 39: '우주 전함',
    40: '인공 지능 로봇 군단', 41: '나노 머신 스웜', 42: '퀀텀 해킹 도구', 43: '가상 현실 조종 장치', 44: '심리전 전파기', 45: '에너지 방패', 46: '테라포밍 장치', 47: '블랙홀 생성기', 48: '우주 파괴 레이저', 49: '창조의 손',
    50: '초신성 폭발 장치', 51: '시간 역행 기계', 52: '우주 재구성기', 53: '현실 조작기', 54: '차원 붕괴기', 55: '우주 재설정 버튼', 56: '무한 에너지 생성기', 57: '영원의 샘', 58: '존재 삭제 총', 59: '무한의 거울',
    60: '혼돈의 망치', 61: '순수의 검', 62: '파멸의 도끼', 63: '재생의 방패', 64: '파괴의 창', 65: '창조의 활', 66: '삭제의 단검', 67: '변형의 지팡이', 68: '통제의 왕관', 69: '지배의 왕좌',
    70: '종말의 책', 71: '시작의 문', 72: '무한의 계단', 73: '존재의 키', 74: '비밀의 상자', 75: '지식의 도서관', 76: '영혼의 우물', 77: '생명의 나무', 78: '죽음의 그림자', 79: '삶의 빛',
    80: '현실의 벽', 81: '환상의 문', 82: '가능성의 창', 83: '불가능의 방', 84: '무의 미로', 85: '유의 정원', 86: '잊혀진 섬', 87: '기억의 바다', 88: '상상의 산맥', 89: '현실의 평원',
    90: '우주의 경계', 91: '시간의 강', 92: '공간의 바다', 93: '차원의 폭포', 94: '역사의 늪', 95: '미래의 탑', 96: '과거의 동굴', 97: '현재의 다리', 98: '영원의 문', 99: '순간의 창', 100: '무한의 문'
}
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

enemy_countries = {
    0: EnemyCountry('몽골', 10, 5, 2, 1000),
    1: EnemyCountry('중국', 30, 10, 5, 3000),
    2: EnemyCountry('태국', 50, 20, 10, 5000),
    3: EnemyCountry('캄보디아', 100, 25, 30, 7000),
    4: EnemyCountry('필리핀', 200, 40, 50, 10000),
    5: EnemyCountry('일본', 500, 100, 100, 15000),
    6: EnemyCountry('호주', 1000, 150, 200, 30000),
    7: EnemyCountry('싱가포르', 3000, 250, 500, 50000),
    8: EnemyCountry('몰디브', 5000, 500, 1000, 75000),
    9: EnemyCountry('인도', 10000, 700, 2000, 100000),
    10: EnemyCountry('네팔', 20000, 1000, 5000, 200000),
    11: EnemyCountry('두바이', 40000, 3000, 8000, 500000),
    12: EnemyCountry('사우디아라비아', 75000, 5000, 10000, 750000),
    13: EnemyCountry('케냐', 100000, 8000, 15000, 1200000),
    14: EnemyCountry('마다가스카르', 150000, 10000, 20000, 1500000),
    15: EnemyCountry('남아프리카', 300000, 20000, 60000, 20000000),
    16: EnemyCountry('가나', 750000, 30000, 80000, 50000000),
    17: EnemyCountry('사하라사막', 1000000, 50000, 130000, 80000000),
    18: EnemyCountry('이집트', 1500000, 75000, 175000, 110000000),
    19: EnemyCountry('터키', 4000000, 100000, 240000, 150000000),
    20: EnemyCountry('러시아', 8000000, 150000, 270000, 200000000),
    21: EnemyCountry('그리스', 13000000, 200000, 330000, 230000000),
    22: EnemyCountry('이탈리아', 18000000, 300000, 370000, 260000000),
    23: EnemyCountry('모나코', 25000000, 500000, 400000, 300000000),
    24: EnemyCountry('스페인', 35000000, 700000, 500000, 400000000),
    25: EnemyCountry('프랑스', 50000000, 1000000, 750000, 800000000),
    26: EnemyCountry('독일', 75000000, 1500000, 1000000, 1500000000),
    27: EnemyCountry('덴마크', 100000000, 2000000, 1500000, 2000000000),
    28: EnemyCountry('노르웨이', 140000000, 3000000, 2000000, 2500000000),
    29: EnemyCountry('영국', 190000000, 4500000, 2500000, 3000000000),
    30: EnemyCountry('그린란드', 250000000, 6000000, 3000000, 3500000000),
    31: EnemyCountry('캐나다', 330000000, 10000000, 4000000, 4500000000),
    32: EnemyCountry('뉴욕', 440000000, 17000000, 5000000, 5000000000),
    33: EnemyCountry('버뮤다', 600000000, 25000000, 6000000, 5500000000),
    34: EnemyCountry('자메이카', 800000000, 35000000, 7000000, 6000000000),
    35: EnemyCountry('콜롬비아', 1000000000, 45000000, 8000000, 6500000000),
    36: EnemyCountry('브라질', 1300000000, 60000000, 9000000, 7000000000),
    37: EnemyCountry('아르헨티나', 1600000000, 80000000, 10000000, 7500000000),
    38: EnemyCountry('마추픽추', 2000000000, 100000000, 11000000, 8000000000),
    39: EnemyCountry('이스터 섬', 2500000000, 120000000, 12000000, 8500000000),
    40: EnemyCountry('멕시코', 3000000000, 150000000, 13000000, 9000000000),
    41: EnemyCountry('NASA', 3600000000, 180000000, 14000000, 9500000000),
    42: EnemyCountry('라스베가스', 4300000000, 220000000, 15000000, 10000000000),
    43: EnemyCountry('할리우드', 5000000000, 270000000, 16000000, 10500000000),
    44: EnemyCountry('알래스카', 5700000000, 330000000, 17000000, 11000000000),
    45: EnemyCountry('미국', 6400000000, 400000000, 18000000, 11500000000),
    46: EnemyCountry('하와이', 7100000000, 500000000, 19000000, 12000000000),
    47: EnemyCountry('북한', 7800000000, 600000000, 20000000, 12500000000),
    48: EnemyCountry('한국', 8500000000, 700000000, 21000000, 13000000000),
    49: EnemyCountry('달', 9200000000, 800000000, 22000000, 13500000000),
    50: EnemyCountry('화성', 9900000000, 900000000, 23000000, 14000000000),
    51: EnemyCountry('수성', 10600000000, 1000000000, 24000000, 14500000000),
    52: EnemyCountry('금성', 11300000000, 1200000000, 25000000, 15000000000),
    53: EnemyCountry('목성', 12000000000, 1500000000, 26000000, 15500000000),
    54: EnemyCountry('토성', 12700000000, 1800000000, 27000000, 16000000000),
    55: EnemyCountry('천왕성', 13400000000, 2200000000, 28000000, 16500000000),
    56: EnemyCountry('해왕성', 14100000000, 2700000000, 29000000, 17000000000),
    57: EnemyCountry('태양', 14800000000, 3300000000, 30000000, 17500000000),
    58: EnemyCountry('명왕성', 15500000000, 4000000000, 31000000, 18000000000),
    59: EnemyCountry('견우성', 16200000000, 5000000000, 32000000, 18500000000),
    60: EnemyCountry('천랑성', 16900000000, 6000000000, 33000000, 19000000000),
    61: EnemyCountry('직녀성', 17600000000, 7000000000, 34000000, 19500000000),
    62: EnemyCountry('알데바란', 18300000000, 8000000000, 35000000, 20000000000),
    63: EnemyCountry('베텔게우스', 19000000000, 9000000000, 36000000, 20500000000),
    64: EnemyCountry('디네프', 19700000000, 10000000000, 37000000, 21000000000),
    65: EnemyCountry('리겔', 20400000000, 12000000000, 38000000, 21500000000),
    66: EnemyCountry('시리우스', 21100000000, 15000000000, 39000000, 22000000000),
    67: EnemyCountry('안드로메다', 21800000000, 18000000000, 40000000, 22500000000),
    68: EnemyCountry('중성자별', 22500000000, 22000000000, 41000000, 23000000000),
    69: EnemyCountry('블랙홀', 50000000000, 50000000000, 10000000, 50000000000),
    70: EnemyCountry('빅뱅', 10000000000000, 5000000000000, None, None),
}
soldier_display = ""
money_display = ""

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
    soldier_display_str = str(soldier)
    if soldier >= 1000000000:
        soldier_display_str = soldier_display_str[:-9] + ',' + soldier_display_str[-9:-6] + ',' + soldier_display_str[-6:-3] + ',' + soldier_display_str[-3:]
    elif soldier >= 1000000:
        soldier_display_str = soldier_display_str[:-6] + ',' + soldier_display_str[-6:-3] + ',' + soldier_display_str[-3:]
    elif soldier >= 1000:
        soldier_display_str = soldier_display_str[:-3] + ',' + soldier_display_str[-3:]
    return soldier_display_str

def money_display_f():
    display_str = str(money)
    if money >= 1000000000:
        display_str = display_str[:-9] + ',' + display_str[-9:-6] + ',' + display_str[-6:-3] + ',' + display_str[-3:]
    elif money >= 1000000:
        display_str = display_str[:-6] + ',' + display_str[-6:-3] + ',' + display_str[-3:]
    elif money >= 1000:
        display_str = display_str[:-3] + ',' + display_str[-3:]
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
                if weapon_gan == 1:
                    weapon_gan += int(weapon_gan_take)
                if weapon < 10:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 1.2
                    weapon_ganha_take *= 1.1
                elif weapon < 20:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 1.5
                    weapon_ganha_take *= 1.5
                elif weapon < 30:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 2
                    weapon_ganha_take *= 2.2
                elif weapon < 40:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 2.7
                    weapon_ganha_take *= 3
                elif weapon < 50:
                    weapon_gan += int(weapon_gan_take)
                    weapon_gan_take *= 3.5
                    weapon_ganha_take *= 3.9
                weapon_random_back -= int(weapon_random_back) * 0.25
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
                print(f"{country_name} 군인 수 : {soldier}명  공격력 : {weapon_gan}" + "=" * 15 + f"{enemy_countries[enemycountry].name} 군인 수 : {enemy_countries[enemycountry].defence}  공격력 : {enemy_countries[enemycountry].attack}")

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
