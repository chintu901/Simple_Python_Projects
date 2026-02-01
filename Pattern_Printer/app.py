import customtkinter as ctk
from tkinter import messagebox

type_of_pattern = None

class  PatternPrinter(ctk.CTk):
    def __init__(self):
        super().__init__()

        # GUI Window
        self.title("Pattern Printer")
        self.geometry("700x550")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=4)

        # Title of the project
        title = ctk.CTkLabel(main_frame,
                             text="Pattern Printer",
                             font=ctk.CTkFont(size=30, weight="bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="ew")

        # Input Field
        option_menu = ctk.CTkOptionMenu(main_frame,
                                        values=["Triangle", "Square", "Diamond"],
                                        height=40,
                                        command=self.get_pattern_type,
                                        font=ctk.CTkFont(size=15, weight="normal"))
        option_menu.set("Select Pattern")
        option_menu.grid(row=1, column=0, sticky="ew", padx=20)

        self.num_entry = ctk.CTkEntry(main_frame,
                                 placeholder_text="Enter height",
                                 height=40,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        self.num_entry.grid(row=1, column=1, sticky="ew")

        enter_btn = ctk.CTkButton(main_frame,
                                  text="Enter",
                                  height=40,
                                  command=self.generate,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        enter_btn.grid(row=1, column=2, sticky="ew", padx=20)


        # TextBox for the pattern printing
        self.pattern_box = ctk.CTkTextbox(main_frame,
                                     font=ctk.CTkFont(size=15, weight="normal"))
        self.pattern_box.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=20, pady=20)

    def get_pattern_type(self, choice):
        global type_of_pattern
        type_of_pattern = choice
    
    def generate_pattern(self, height, pattern_type):
        pattern = []
        height = int(height)
        if pattern_type == "Triangle":
            for i in range(1, height+1):
                line = "*"*i
                pattern.append(line)
            return "\n".join(pattern)
        elif pattern_type == "Square":
            for i in range(1, height+1):
                line = "*"*height
                pattern.append(line)
            return "\n".join(pattern)
        elif pattern == "Diamond":
            mid = height // 2
            if height % 2 == 0:
                messagebox.showerror("Error", "Enter only odd number for 'Diamond' pattern")
                return
            else:
                # for upper half of diamond
                for i in range(mid + 1):
                    space = " "*(mid - 1)
                    star = "*"*(2 * i + 1)
                    pattern.append(space+star)
                # for lower half of diamon
                for i in (mid - 1, -1, -1):
                    space = " "*(mid - 1)
                    star = "*"*(2 * i + 1)
                    pattern.append(space+star)
                return "\n".join(pattern)
    
    def generate(self):
        try:
            num = self.num_entry.get()
            if len(num) == 0 and int(num) <= 0:
                messagebox.showerror("Error", "Only positive numbers allowed")
            else:
                pattern = self.generate_pattern(num, type_of_pattern)
                self.pattern_box.delete("1.0", "end")
                self.pattern_box.insert("1.0", pattern)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = PatternPrinter()
    app.mainloop()