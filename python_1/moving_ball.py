import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Moving Ball")

# Set up the canvas (drawing area)
canvas_width = 600
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Create a ball (a circle)
ball_radius = 20
x_start = 0
y_pos = canvas_height // 2
ball = canvas.create_oval(x_start, y_pos - ball_radius, x_start + 2 * ball_radius, y_pos + ball_radius, fill="blue")

# Movement settings
dx = 5  # pixels per frame

def move_ball():
    canvas.move(ball, dx, 0)  # move right
    pos = canvas.coords(ball)

    # If the ball hits the right edge, reset to left
    if pos[2] >= canvas_width:
        canvas.coords(ball, 0, y_pos - ball_radius, 2 * ball_radius, y_pos + ball_radius)
    
    # Schedule the next move
    root.after(30, move_ball)  # 30ms delay = ~33 frames per second

# Start moving the ball
move_ball()

# Run the GUI event loop
root.mainloop()
