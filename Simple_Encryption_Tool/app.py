import customtkinter as ctk
from tkinter import messagebox

type_of_mode = None

class SimpleEncryptionTool(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simple Encryption Tool")
        self.geometry("600x400")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_widgets()
    
    def create_widgets(self):

        # main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=4)

        # Title of the project
        title_txt = ctk.CTkLabel(main_frame,
                                 text="Simple Encryption Tool",
                                 font=ctk.CTkFont(size=30, weight="bold"))
        title_txt.grid(row=0, column=0, sticky="ew")

        # Input frame
        input_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        input_frame.grid(row=1, column=0, sticky="nsew")

        input_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        input_frame.grid_rowconfigure((0, 1), weight=1)

        mode_txt = ctk.CTkLabel(input_frame,
                                text="Mode:",
                                height=40,
                                font=ctk.CTkFont(size=15, weight="normal"))
        mode_txt.grid(row=0, column=0, sticky="ew", pady=(10, 20))

        option_menu = ctk.CTkOptionMenu(input_frame,
                                        values=["Encryption", "Decryption"],
                                        height=40,
                                        command=self.check_mode,
                                        font=ctk.CTkFont(size=15, weight="normal"))
        option_menu.set("Select Mode")
        option_menu.grid(row=0, column=1, columnspan=2, sticky="w", padx=(10, 0), pady=(10, 20))

        self.text_input = ctk.CTkEntry(input_frame,
                                  placeholder_text="Enter String..",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        self.text_input.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10)

        self.shift_input = ctk.CTkEntry(input_frame,
                                   placeholder_text="Enter shift number.",
                                   height=40,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        self.shift_input.grid(row=1, column=2, sticky="ew", padx=(0, 10))

        self.act_btn = ctk.CTkButton(input_frame,
                                text="Enter",
                                height=40,
                                command=self.on_click,
                                font=ctk.CTkFont(size=15, weight="normal"))
        self.act_btn.grid(row=1, column=3, sticky="ew", padx=(0, 10))


        # Output frame
        output_frame = ctk.CTkFrame(main_frame, corner_radius=5)
        output_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=40)

        output_frame.grid_columnconfigure(0, weight=1)
        output_frame.grid_rowconfigure((0, 1), weight=1)

        self.output_label = ctk.CTkLabel(output_frame,
                                         text="Decryption:",
                                         height=40,
                                         font=ctk.CTkFont(size=15, weight="normal"))
        self.output_label.grid(row=0, column=0, sticky="w", padx=10)

        self.result = ctk.CTkLabel(output_frame,
                                   text="----------",
                                   fg_color="#ffffff",
                                   corner_radius=5,
                                   height=40,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        self.result.grid(row=1, column=0, sticky="ew", padx=10, pady=(10, 20))
    
    def check_mode(self, choice):
        global type_of_mode

        if choice == "Encryption":
            self.output_label.configure(text="Decrypted Code:")
            self.act_btn.configure(text="Encrypt it!")
        elif choice == "Decryption":
            self.output_label.configure(text="Encrypted Code:")
            self.act_btn.configure(text="Decrypt it!")

        type_of_mode = choice
    
    def on_click(self):
        try:
            user_input = self.text_input.get()
            shift_num = int(self.shift_input.get())

            if type_of_mode == "Encryption":
                enc_result = ""
                for char in user_input:
                    if char.isupper():
                        enc_result += chr((ord(char) + shift_num - 65) % 26 + 65)
                    elif char.islower():
                        enc_result += chr((ord(char) + shift_num - 97) % 26 + 97)
                    else:
                        enc_result += char
                self.result.configure(text=f"{enc_result}")
            elif type_of_mode == "Decryption":
                shift_num = 26 - shift_num
                dec_result = ""
                for char in user_input:
                    if char.isupper():
                        dec_result += chr((ord(char) + shift_num - 65) % 26 + 65)
                    elif char.islower():
                        dec_result += chr((ord(char) + shift_num - 97) % 26 + 97)
                    else:
                        dec_result += char
                self.result.configure(text=f"{dec_result}")
        
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

            


if __name__ == "__main__":
    app = SimpleEncryptionTool()
    app.mainloop()