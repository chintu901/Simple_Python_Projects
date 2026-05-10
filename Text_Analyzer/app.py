import customtkinter as ctk
from tkinter import messagebox

class TextAnalyzer(ctk.CTk):

    def __init__(self):
        super().__init__()

        # window config
        self.title("Text Analyzer")
        self.geometry("700x550")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_widgets()
    
    def create_widgets(self):
        # Create main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.columnconfigure((0, 1), weight=1)
        main_frame.rowconfigure((0, 1, 2), weight=1)

        # Title of the project
        title_label = ctk.CTkLabel(main_frame,
            text="Text Analyzer",
            font=ctk.CTkFont(size=34, weight="bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=0, sticky="ew")

        #Text field
        self.text_box = ctk.CTkEntry(main_frame,
                                placeholder_text="Enter String...",
                                width=300,
                                height=40,
                                font=ctk.CTkFont(size=14, weight="normal"))
        self.text_box.grid(row=1, column=0, padx=(20,0), sticky="ne")

        # Submit button
        submit_btn = ctk.CTkButton(main_frame,
                                   text="Submit",
                                   width=150,
                                   height=40,
                                   command=self.get_result,
                                   font=ctk.CTkFont(size=14, weight="normal"))
        submit_btn.grid(row=1, column=1, padx=(10, 20), sticky="nw")

        # Result frame
        res_frame = ctk.CTkFrame(main_frame, fg_color="#b9b8b8")
        res_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=40, pady=(0, 40))

        res_frame.columnconfigure((0, 1), weight=1)
        res_frame.rowconfigure((0, 1), weight=1)

        # Letter Label
        self.letters_count = ctk.CTkLabel(res_frame,
                                     text="Letters: 0",
                                     font=ctk.CTkFont(size=24, weight="bold"))
        self.letters_count.grid(row=0,column=0, sticky="ew")

        self.words_count = ctk.CTkLabel(res_frame,
                                     text="Words: 0",
                                     font=ctk.CTkFont(size=24, weight="bold"))
        self.words_count.grid(row=1,column=0, sticky="ew")

        self.vowels_count = ctk.CTkLabel(res_frame,
                                     text="Vowels: 0",
                                     font=ctk.CTkFont(size=24, weight="bold"))
        self.vowels_count.grid(row=0,column=1, sticky="ew")

        self.Consonants_count = ctk.CTkLabel(res_frame,
                                     text="Consonants: 0",
                                     font=ctk.CTkFont(size=24, weight="bold"))
        self.Consonants_count.grid(row=1,column=1, sticky="ew")
    
    def get_result(self):
        user_input = self.text_box.get()
        vowels_letters = ["a", "e", "i", "o", "u"]
        letters = 0
        words = 0
        vowels = 0
        Consonants = 0

        try:
            if len(user_input) == 0:
                messagebox.showerror("Error", "The string is empty")
                return
            else:
                for i in user_input.lower():
                    if i in vowels_letters:
                        vowels += 1
                    elif i not in vowels_letters and i != " " and i.isalpha():
                        Consonants += 1
                    if i == " ":
                        words += 1
                    if i != " ":
                        letters += 1

                self.letters_count.configure(text=f"Letters: {letters}")                
                self.words_count.configure(text=f"Words: {words + 1}")                
                self.vowels_count.configure(text=f"Vowels: {vowels}")                
                self.Consonants_count.configure(text=f"Consonants: {Consonants}")
                self.text_box.delete(0, "end")                

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = TextAnalyzer()
    app.mainloop()
