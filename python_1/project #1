import tkinter as tk
import random
import os

W, H = 600, 400  # Corrected 'h' to 'H'
BALL_SIZE, GOAL_W, GOAL_H, SPEED = 30, 60, 80, 10
HS_FILE = "highscore.txt"

class Game:
    def __init__(self, root):
        self.c = tk.Canvas(root, width=W, height=H, bg="black")  # Capital 'Canvas'
        self.c.pack()
        self.score, self.time = 0, 60
        self.high_score = self.load_high_score()
        self.ball = self.c.create_oval(W//2, H//2, W//2+BALL_SIZE, H//2+BALL_SIZE, fill="white")  # Corrected spelling + fill
        self.goals = [self.make_goal(), self.make_goal()]
        self.lbl = tk.Label(root, text=f"Score: 0 | Time: 60", font=("Arial", 14)); self.lbl.pack()
        root.bind("<KeyPress>", self.move)
        self.update_timer()
         
def load_high_score(self):
    if os.path.exists(HS_FILE):
        with open(HS_FILE, "r") as f:
            return int(f.read())
    return 0  

def save_high_score(self):
    with open(HS_FILE, "w") as f:
        f.write(str(self.high_score)) 

def make_goal(self):
    r = self.c.create_rectangle(0,0, GOAL_W, GOAL_H, fill="red")
    self.move_goal(r)
    return r