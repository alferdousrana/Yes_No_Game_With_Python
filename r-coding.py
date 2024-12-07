import tkinter as tk
import random

def on_yes_click():
    message_label.config(text="Thank you for Accepting")

def move_no_button(event):
    # Random new position within the window boundaries
    new_x = random.randint(0, 400)
    new_y = random.randint(0, 700)
    no_button.place(x=new_x, y=new_y)

# Create the main window
root = tk.Tk()
root.title("R-Coding")
root.geometry("400x700")

# Question label
question_label = tk.Label(root, text="I like you! Do you like me?", font=("Arial", 16))
question_label.pack(pady=20)

# Yes button
yes_button = tk.Button(root, text="Yes", font=("Arial", 14), command=on_yes_click)
yes_button.pack(pady=20)

# No button
no_button = tk.Button(root, text="No", font=("Arial", 14))
no_button.place(x=150, y=150)
no_button.bind("<Enter>", move_no_button)  # Move the "No" button on mouse hover

# Message label
message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack(pady=20)

# Run the application
root.mainloop()
