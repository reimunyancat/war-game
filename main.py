import time

money = 1000
soldier = 0
weapon = 1
weapon_name = '나무검'
money_take = 100
def tutorial():
    print("부대모집은 단순히 사람을 뽑는거고 무기강화는 무기를 강화시키는겁니다")
    print("전투력은 부대수 X 무기강화수치입니다")
    print("메인화면에서 잔액과 부대수와 무기강화현황을 볼 수 있습니다")
    print("나라를 점령할수록 돈벌기 수익이 증가합니다")


def make_money():
    print("1 : 깡노동  2 : 도박  3 : 허접한 도박")
    main_input = input()
    if main_input == '1': make_money1()

def make_money1():
    global money, money_take
    print("1초에",money_take,"원씩 벌어요")
    money_input = int(input("돈을 벌 시간을 입력하세요(초) : "))
    while True:
        if money_input <= 0: break
        money += money_take
        time.sleep(1)
        money_input -= 1
    print("현재 돈은", money,"원 입니다")

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
    elif main_input == '5':
        break
