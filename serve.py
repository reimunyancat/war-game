import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

class WarGameApp:
    def __init__(self, master):
        self.master = master
        master.title("전쟁 게임")

        self.money = 1000
        self.soldier = 0
        self.weapon = 0
        self.weapon_gan = 1
        self.weapon_gan_take = 10
        self.weapon_name = {0: '모래', 1: '돌', 2: '나무검', 3: '돌검', 4: '낫', 5: '망치', 6: '도끼', 7: '칼', 8: '노트북', 9: '톱', 10: '수류탄'}

        self.status_frame = tk.Frame(master)
        self.status_frame.pack()

        self.money_label = tk.Label(self.status_frame, text=f"돈: {self.money}원")
        self.money_label.pack()

        self.soldier_label = tk.Label(self.status_frame, text=f"군인 수: {self.soldier}명")
        self.soldier_label.pack()

        self.weapon_label = tk.Label(self.status_frame, text=f"무기: {self.weapon_name[self.weapon]} (공격력: {self.weapon_gan})")
        self.weapon_label.pack()

        self.action_frame = tk.Frame(master)
        self.action_frame.pack()

        self.recruit_button = tk.Button(self.action_frame, text="군인 모집", command=self.recruit_soldier)
        self.recruit_button.pack(side=tk.LEFT)

        self.upgrade_weapon_button = tk.Button(self.action_frame, text="무기 강화", command=self.upgrade_weapon)
        self.upgrade_weapon_button.pack(side=tk.LEFT)

        self.make_money_button = tk.Button(self.action_frame, text="돈 벌기", command=self.make_money)
        self.make_money_button.pack(side=tk.LEFT)

        self.start_war_button = tk.Button(self.action_frame, text="전쟁 시작", command=self.start_war)
        self.start_war_button.pack(side=tk.LEFT)

    def recruit_soldier(self):
        soldier_cost = 1000
        if self.money >= soldier_cost:
            self.soldier += 1
            self.money -= soldier_cost
            self.update_status()
        else:
            messagebox.showinfo("알림", "돈이 부족합니다!")

    def upgrade_weapon(self):
        upgrade_cost = 100
        if self.money >= upgrade_cost:
            self.weapon += 1
            self.money -= upgrade_cost
            self.update_status()
        else:
            messagebox.showinfo("알림", "돈이 부족합니다!")

    def make_money(self):
        money_earned = simpledialog.askinteger("돈 벌기", "몇 시간 돈을 벌겠습니까?", minvalue=1, maxvalue=24)
        if money_earned:
            self.money += money_earned * 100  # 예를 들어 시간당 100원 번다고 가정
            self.update_status()

    def start_war(self):
        enemy_strength = random.randint(1, 10)
        if self.soldier > enemy_strength:
            messagebox.showinfo("전쟁 결과", "승리했습니다!")
            self.money += 500  # 전쟁 승리 보상
            self.soldier -= enemy_strength  # 전쟁 중 손실된 군인 수
        else:
            messagebox.showinfo("전쟁 결과", "패배했습니다!")
            self.soldier = 0  # 모든 군인이 전쟁에서 패배
        self.update_status()

    def update_status(self):
        self.money_label.config(text=f"돈: {self.money}원")
        self.soldier_label.config(text=f"군인 수: {self.soldier}명")
        self.weapon_label.config(text=f"무기: {self.weapon_name[self.weapon]} (공격력: {self.weapon_gan})")

if __name__ == "__main__":
    root = tk.Tk()
    app = WarGameApp(root)
    root.mainloop()