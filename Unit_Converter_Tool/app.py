# Unit Converter Tool:-
from customtkinter import *
from PIL import Image

app = CTk()
app.title("Unit Converter Tool")
app.geometry("500x350")
app.resizable(False, False)

# Set the window mode
set_appearance_mode("light")

# Frame for gride layout
frame = CTkFrame(app,)
frame.pack(fill="both", expand=True)

# IMPORTANT: configure grid
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Program Logic
Type_of_Conversion = None

def Change_text(choice):
    global Type_of_Conversion
    if choice == "Length":
        result.configure(text="____ft")
        Change_type.configure(text="meters_to_feet")
    elif choice == "Mass":
        result.configure(text="____lbs")
        Change_type.configure(text="kg_to_lbs")
    elif choice == "Temperature":
        result.configure(text="____°F")
        Change_type.configure(text="celsius_to_fahrenheit")
    Type_of_Conversion = choice

def Calculate_OnClick():
    global Type_of_Conversion
    user_input = float(number.get())
    meters_to_feet = 3.28084
    kg_to_lbs = 2.20462
    celsius_to_fahrenheit = 1.8

    if Type_of_Conversion == "Length":
        feet = user_input * meters_to_feet
        result.configure(text=f"{feet}ft")
    elif Type_of_Conversion == "Mass":
        pound = user_input * kg_to_lbs
        result.configure(text=f"{pound}lbs")
    elif Type_of_Conversion == "Temperature":
        pound = (user_input * celsius_to_fahrenheit) + 32
        result.configure(text=f"{pound}°F")


# GUI Elements
project_name = CTkLabel(frame, text="Unit Converter Tool", font=("Arial", 25), width=100, height=20)

unit_type = CTkOptionMenu(frame, values=["Length", "Mass", "Temperature"],
                          corner_radius=5,
                          width=170,
                          height=30,
                          fg_color="#bebebe",
                          button_color="#a09f9f",
                          button_hover_color="#747373",
                          text_color="black",
                          command=Change_text)
unit_type.set("Select Conversion Type")

Change_type = CTkLabel(frame, text="??",
                       corner_radius=5,
                       width=170,
                       height=30,
                       fg_color="#a09f9f")

number = CTkEntry(frame, placeholder_text="Enter Number",
                     width=200,
                     height=40)

result = CTkLabel(frame, text="Number..",
                     width=150,
                     height=40,
                     justify="left",
                     fg_color="#ffffff",
                     corner_radius=5,
                     )

Calculate_button = CTkButton(frame, text="Calculate",
                             width=380,
                             height=40,
                             corner_radius=5,
                             font=("Arial", 20),
                             command=Calculate_OnClick)

# Positioning the GUI element
project_name.grid(row=0, column=0, columnspan=2, pady=(40,0))
unit_type.grid(row=1, column=0, columnspan=2, pady=(20, 0), padx=20, sticky="w")
Change_type.grid(row=1, column=1, columnspan=2, pady=(20, 0), padx=20, sticky="e")
number.grid(row=2, column=0, pady=(40, 0), padx=(30, 0), sticky="e")
result.grid(row=2, column=1, pady=(40, 0), columnspan=2, padx=(30, 0), sticky="w")
Calculate_button.grid(row=3, column=0, pady=20, columnspan=2)

app.mainloop()