import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import time

class WarGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("전쟁 게임")

        self.money = 1000
        self.money_take = 100
        self.money_magnification_1 = 4
        self.money_magnification_2 = 10

        self.create_widgets()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, text=f"현재 돈: {self.money}원")
        self.info_label.pack(pady=20)

        self.money_button = tk.Button(self.root, text="돈 벌기", command=self.make_money)
        self.money_button.pack()

    def update_info_label(self):
        self.info_label.config(text=f"현재 돈: {self.money}원")

    def make_money(self):
        options = {"1": "깡노동", "2": "도박"}
        choice = simpledialog.askstring("돈 벌기", "1: 깡노동  2: 도박\n선택:")
        if choice == "1":
            self.make_money_by_work()
        elif choice == "2":
            self.make_money_by_gambling()

    def make_money_by_work(self):
        work_time = simpledialog.askinteger("깡노동", "돈을 벌 시간을 입력하세요(초):")
        if work_time and work_time > 0:
            for _ in range(work_time):
                self.money += self.money_take
                self.update_info_label()
                time.sleep(1)

    def make_money_by_gambling(self):
        game_options = {"1": "홀짝 게임", "2": "블랙잭"}
        game_choice = simpledialog.askstring("도박", "1: 홀짝 게임  2: 블랙잭\n선택:")
        if game_choice == "1":
            self.play_odd_even_game()
        elif game_choice == "2":
            self.play_blackjack()

    def play_odd_even_game(self):
        bet = simpledialog.askinteger("홀짝 게임", "베팅 금액을 입력하세요:")
        if bet and bet <= self.money:
            result = random.randint(1, 100)
            user_choice = simpledialog.askstring("홀짝 게임", "홀수인지 짝수인지 선택하세요 (홀수/짝수):")
            if (result % 2 == 0 and user_choice == "짝수") or (result % 2 != 0 and user_choice == "홀수"):
                self.money += bet * self.money_magnification_1
                messagebox.showinfo("홀짝 게임", f"이겼습니다! 컴퓨터의 숫자: {result}")
            else:
                self.money -= bet
                messagebox.showinfo("홀짝 게임", f"졌습니다. 컴퓨터의 숫자: {result}")
            self.update_info_label()

    def play_blackjack(self):
        betting = simpledialog.askinteger("블랙잭", "베팅 금액을 입력하세요:")
        if betting > self.money:
            messagebox.showwarning("경고", "돈이 부족합니다.")
            return

        deck = self.initialize_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        player_hand_value = self.calculate_hand_value(player_hand)
        dealer_hand_value = self.calculate_hand_value(dealer_hand)

        while True:
            action = simpledialog.askstring("블랙잭", f"플레이어의 카드: {player_hand}\n플레이어의 현재 카드 합계: {player_hand_value}\n카드를 더 받으시겠습니까?(yes/no):")
            if action.lower() == 'yes':
                player_hand.append(deck.pop())
                player_hand_value = self.calculate_hand_value(player_hand)
                if player_hand_value > 21:
                    messagebox.showinfo("블랙잭", "버스트! 당신이 졌습니다.")
                    self.money -= betting
                    break
            else:
                break

        while dealer_hand_value < 17:
            dealer_hand.append(deck.pop())
            dealer_hand_value = self.calculate_hand_value(dealer_hand)

        if dealer_hand_value > 21 or player_hand_value > dealer_hand_value:
            messagebox.showinfo("블랙잭", "당신이 이겼습니다!")
            self.money += betting
        elif player_hand_value < dealer_hand_value:
            messagebox.showinfo("블랙잭", "당신이 졌습니다.")
            self.money -= betting
        else:
            messagebox.showinfo("블랙잭", "무승부입니다.")

        self.update_info_label()

    def initialize_deck(self):
        suits = ['스페이드', '다이아몬드', '하트', '클로버']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        value = 0
        num_aces = 0
        for card in hand:
            rank = card['rank']
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                num_aces += 1
                value += 11
            else:
                value += int(rank)
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

if __name__ == "__main__":
    root = tk.Tk()
    app = WarGameApp(root)
    root.mainloop()