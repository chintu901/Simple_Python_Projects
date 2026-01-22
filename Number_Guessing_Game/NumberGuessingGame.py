from customtkinter import *
from PIL import *
import random

app = CTk()
app.title("Number Guessing Game")
app.geometry("500x350")
app.resizable(False, False)

# Set the model for the window
set_appearance_mode("light")

# Frame for grid layout
frame = CTkFrame(app)
frame.pack(fill='both', expand=True)

# IMPORTANT: configure grid
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Program Logic
secrate_number = random.randint(1, 10)
attempts_counter = 3

def check_input():
    global secrate_number, attempts_counter
    user_input = text_box.get()

    correct_ans = str(secrate_number)

    if user_input.strip() == "":
        ans_msg.configure(text_color="#2D2C2C", text="Please enter something")
        return
    if attempts_counter > 0:
        if user_input == correct_ans:
            ans_msg.configure(text_color="#379137", text="🎉 Congratulations! You guessed the correct number!")
            attempts_counter -= 1
            attempt_count.configure(text=f"{attempts_counter}")
        else:
            ans_msg.configure(text=f"Oops! Your guess is Wrong. Try again!!", text_color="#cd2f2f")
            attempts_counter -= 1
            attempt_count.configure(text=f"{attempts_counter}")
    else:
        ans_msg.configure(text_color="#cd2f2f", text="No attempts left. Better luck next time!")
    
    text_box.delete(0, "end")

def reset_attempt():
    global attempts_counter
    attempts_counter = 3
    attempt_count.configure(text=f"{attempts_counter}")
    ans_msg.configure(text_color="#2D2C2C", text="Please enter something")

# GUI Elements
reset_button = CTkButton(frame, text="Reset", width=90, height=30, corner_radius=5, font=("Arial", 14), fg_color="#cd2f2f", hover_color="#a92323", command=reset_attempt)

attempt_left = CTkLabel(frame, text="Attempt Left:", width=90, height=30, font=("Arial", 14))

attempt_count = CTkLabel(frame, text="3", width=20, height=30, fg_color="#424141", font=("Arial", 14), text_color="#ffffff", corner_radius=5)

project_name = CTkLabel(frame, text="Number Guessing Game", font=("Arial", 25))

ans_msg = CTkLabel(frame, text="Welcome to the Number Guessing Game!")

text_box = CTkEntry(frame, placeholder_text="Enter number between 1 - 10", width=180, height=30, corner_radius=5)
my_button_2 = CTkButton(frame, text="Submit", font=("Arial", 14), width=90, height=30, corner_radius=5, command=check_input)

# Positioning the GUI element
reset_button.grid(row=0, column=0, pady=(10,0), padx=(5,0), sticky="w")
attempt_left.grid(row=0, column=1, pady=(10,0), padx=(0,5), sticky="e")
attempt_count.grid(row=0, column=2, pady=(10,0), padx=(0,5), sticky="e")
project_name.grid(row=1, column=0, columnspan=2, pady=(80, 20))
ans_msg.grid(row=2, column=0, columnspan=2)
text_box.grid(row=3, column=0, pady=20, sticky="e")
my_button_2.grid(row=3, column=1, pady=20, padx = 5, sticky="w")

app.mainloop()