import customtkinter as ctk
from PIL import Image
import os

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.title("Click Counter")
app.geometry("500x500")
app.resizable(False, False)

# Create a Quick frame
Frame = ctk.CTkFrame(app)
Frame.pack(fill="both", expand=True)

# Load image
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
ICON_DIR = os.path.join(BASE_DIR, "res", "icons")

reset_img = ctk.CTkImage(
    Image.open(os.path.join(ICON_DIR, "reset_icon.png")),
    size=(30, 30)
    )

click_img = ctk.CTkImage(
    Image.open(os.path.join(ICON_DIR, "click_icon.png")),
    size=(30, 30)
    )

# IMPORTANT: configure grid
Frame.grid_columnconfigure(0, weight=1)
Frame.grid_columnconfigure(1, weight=1)
Frame.grid_rowconfigure(0, weight=1)
Frame.grid_rowconfigure(1, weight=1)

count = 0

def click_button():
    global count
    count += 1
    label.configure(text=f"You've clicked the button {count} times", font=("Arial", 22))

def reset_count():
    global count
    count = 0
    label.configure(text=f"You've clicked the button {count} times", font=("Arial", 22))

label = ctk.CTkLabel(Frame, text = f"You've clicked the button {count} times",
                     font=("Arial", 22))

my_button = ctk.CTkButton(Frame, text="Click Me!!",
                          font=("Arial", 20),
                          image=click_img,
                          command=click_button)

reset_button = ctk.CTkButton(Frame, text="Reset",
                             font=("Arial", 20),
                             fg_color="#cd2f2f",
                             hover_color="#a92222",
                             image=reset_img,
                             command=reset_count)



label.grid(row=0, column=0, columnspan=2, pady=(80,20), sticky="nsew")
my_button.grid(row=1, column=0, padx=10, sticky="e")
reset_button.grid(row=1, column=1, padx=10, sticky="w")

app.mainloop()