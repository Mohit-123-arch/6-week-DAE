#this code is for my game called balls and goals
import tkinter as tk
import random
import os

W, H = 600, 400
BALL_SIZE, GOAL_W, GOAL_H, SPEED = 30, 60, 80, 10
HS_FILE = "highscore.txt"

class Game:
    
    #creates variables for game-related objects
    def __init__(self, root):
        self.c = tk.Canvas(root, width=W, height=H, bg="black")
        self.c.pack()
        self.score, self.time = 0, 60
        self.high_score = self.load_high_score()
        self.ball = self.c.create_oval(W//2, H//2, W//2+BALL_SIZE, H//2+BALL_SIZE, fill="white")
        self.goals = [self.make_goal(), self.make_goal()]
        self.lbl = tk.Label(root, text=f"Score: 0 | Time: 60", font=("Arial", 14))
        self.lbl.pack()
        root.bind("<KeyPress>", self.move)
        self.update_timer()

#loads the highscore
    def load_high_score(self):
        if os.path.exists(HS_FILE):
            with open(HS_FILE, "r") as f:
                content = f.read().strip()
                if content.isdigit():
                    return int(content)
        return 0

#saves highscore
    def save_high_score(self):
        with open(HS_FILE, "w") as f:
            f.write(str(self.high_score))

#creates the goal
    def make_goal(self):
        g = self.c.create_rectangle(0, 0, GOAL_W, GOAL_H, fill="red")
        self.move_goal(g)
        return g

#helps teleport the goal to random location
    def move_goal(self, goal):
        x, y = random.randint(0, W - GOAL_W), random.randint(0, H - GOAL_H)
        self.c.coords(goal, x, y, x + GOAL_W, y + GOAL_H)

#helps move the ball with arrow keys
    def move(self, event):
        dx = {"Left": -SPEED, "Right": SPEED}.get(event.keysym, 0)
        dy = {"Up": -SPEED, "Down": SPEED}.get(event.keysym, 0)
        self.c.move(self.ball, dx, dy)
        self.check_collision()

#gets coordinates of ball and goals and checks for overlap
    def check_collision(self):
        ball_coords = self.c.coords(self.ball)
        for goal in self.goals:
            goal_coords = self.c.coords(goal)
            if not (ball_coords[2] < goal_coords[0] or ball_coords[0] > goal_coords[2] or
                    ball_coords[3] < goal_coords[1] or ball_coords[1] > goal_coords[3]):
                self.score += 1
                self.lbl.config(text=f"Score: {self.score} | Time: {self.time}")
                self.move_goal(goal)
                break

#updates the timer and game over screen
    def update_timer(self):
        if self.time > 0:
            self.time -= 1
            self.lbl.config(text=f"Score: {self.score} | Time: {self.time}")
            self.c.after(1000, self.update_timer)
        else:
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            self.c.create_text(W//2, H//2, 
                               text=f"Game Over\nScore: {self.score}\nHigh Score: {self.high_score}",
                               font=("Helvetica", 20), fill="white")

# Run the game
root = tk.Tk()
root.title("Soccer Game")
Game(root)
tk.mainloop()
