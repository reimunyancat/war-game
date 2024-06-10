from cryptography.fernet import Fernet
import json
import os

def back(betting, money):
    if betting <= 0 or betting > money:
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

def ensure_save_folder():
    if not os.path.exists('save'):
        os.makedirs('save')

def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    try:
        with open('secret.key', 'rb') as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        return generate_key()

key_data = load_key()
cipher_suite = Fernet(key_data)

def save_game(country_name, main_name, money, soldier, weapon, weapon_gan, enemycountry):
    ensure_save_folder()
    printline()
    game_state = {
        'money': money,
        'soldier': soldier,
        'weapon': weapon,
        'weapon_gan': weapon_gan,
        'enemycountry': enemycountry,
        'country_name': country_name,
        'main_name': main_name
    }
    encrypted_data = cipher_suite.encrypt(json.dumps(game_state).encode('utf-8'))
    with open('save/game_state.enc', 'wb') as f:
        f.write(encrypted_data)
    print("저장 성공")

def load_game():
    global country_name, main_name, money, soldier, weapon, weapon_gan, enemycountry
    ensure_save_folder()
    printline()
    try:
        with open('save/game_state.enc', 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        game_state = json.loads(decrypted_data.decode('utf-8'))
        country_name = game_state['country_name']
        main_name = game_state['main_name']
        money = game_state['money']
        soldier = game_state['soldier']
        weapon = game_state['weapon']
        weapon_gan = game_state['weapon_gan']
        enemycountry = game_state['enemycountry']
        print("로드 성공")
    except FileNotFoundError:
        print("저장된 게임이 없습니다.")
    except Exception as e:
        print(f"게임을 불러오는 중 오류가 발생했습니다: {e}")