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

def soldier_display_f(soldier):
    display_str = f"{soldier:,}"
    return display_str

def money_display_f(money):
    display_str = f"{money:,}"
    return display_str

