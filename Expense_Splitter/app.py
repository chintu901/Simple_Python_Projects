import customtkinter as ctk
from tkinter import messagebox

class ItemCard(ctk.CTkFrame):
    def __init__(self, parent, app, name, amount):
        super().__init__(parent, corner_radius=8)

        self.app = app      # 🔥 reference to main app
        self.name = name    # store item name

        # Grid setup
        self.grid_columnconfigure((0,1,2), weight=1)

        ctk.CTkLabel(self, text=name).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(self, text=amount).grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkButton(self, text="Remove", command=self.remove_item).grid(row=0, column=2, padx=10, pady=10)

    
    def remove_item(self):
        # Remove from main app data
        self.app.items = [item for item in self.app.items if item["name"] != self.name]

        # Remove UI card
        self.destroy()

        self.app.display_result()

class ExpenseSplitter(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window config
        self.title("Grade Calculator")
        self.geometry("700x550")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=2)
        main_frame.grid_rowconfigure(2, weight=5)
        main_frame.grid_rowconfigure(3, weight=2)

        # Title of the project
        title_label = ctk.CTkLabel(main_frame,
                                   text="Expense Splitter",
                                   font=ctk.CTkFont(size=34, weight="bold")
        )
        title_label.grid(row=0, column=0, pady=0, sticky="ew")

        # Input frame
        input_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        input_frame.grid(row=1, column=0,sticky="nsew")

        input_frame.grid_columnconfigure(0, weight=4)
        input_frame.grid_columnconfigure(1, weight=4)
        input_frame.grid_columnconfigure(2, weight=2)
        input_frame.grid_rowconfigure((0, 1), weight=1)

        # Input frame UI elements
        self.num_people = ctk.CTkEntry(input_frame,
                                  placeholder_text="Number of People?",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        self.num_people.grid(row=0, column=0, columnspan=2, padx=10, sticky="ew")

        reset_btn = ctk.CTkButton(input_frame,
                                  text="Clear All",
                                  fg_color="#d84545",
                                  hover_color="#c42f2f",
                                  command=self.clear_all,
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        reset_btn.grid(row=0, column=2, padx=20, sticky="ew")

        self.exp_amount = ctk.CTkEntry(input_frame,
                                  placeholder_text="Amount of Expense",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        self.exp_amount.grid(row=1, column=0, padx=(10, 10), sticky="ew")

        self.exp_name = ctk.CTkEntry(input_frame,
                                  placeholder_text="Name of Expense",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        self.exp_name.grid(row=1, column=1, padx=(10, 10), sticky="ew")

        calculate_btn = ctk.CTkButton(input_frame,
                                  text="Add",
                                  fg_color="#7edc79",
                                  hover_color="#59c160",
                                  command=self.add_toList,
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        calculate_btn.grid(row=1, column=2, padx=20, sticky="ew")

        # Scrollable frame
        self.scroll = ctk.CTkScrollableFrame(main_frame)
        self.scroll.grid(row=2, column=0, columnspan=3, padx=10, sticky="ew")
        self.scroll.grid_columnconfigure(0, weight=1)

        self.items = []

        # Calculated Result Frame
        res_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        res_frame.grid(row=3, column=0, sticky="nsew")

        res_frame.grid_columnconfigure((0, 1), weight=1)
        res_frame.grid_rowconfigure((0, 1), weight=1)

        # Calculated Result Frame UI Elements
        total_label = ctk.CTkLabel(res_frame,
                                   text="TOTAL:",
                                   height=40,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        total_label.grid(row=0, column=0, padx=10, sticky="nsew")

        self.to_label = ctk.CTkLabel(res_frame,
                                   text="------",
                                   corner_radius=5,
                                   width=200,
                                   height=40,
                                   fg_color="#ffffff",
                                   font=ctk.CTkFont(size=15, weight="normal"))
        self.to_label.grid(row=0, column=1, padx=10, sticky="w")

        split_label = ctk.CTkLabel(res_frame,
                                   text="Split:",
                                   height=40,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        split_label.grid(row=1, column=0, padx=10, sticky="nsew")

        self.sp_label = ctk.CTkLabel(res_frame,
                                   text="------",
                                   corner_radius=5,
                                   width=200,
                                   height=40,
                                   fg_color="#ffffff",
                                   font=ctk.CTkFont(size=15, weight="normal"))
        self.sp_label.grid(row=1, column=1, padx=10,pady=10, sticky="w")
    
    def is_inList(self, sub):
        sub = sub.lower()

        for item in self.items:
            if item["name"].lower() == sub:
                return True
        return False
    
    def display_result(self):
        """Finding and Displaying the result from the given expenses"""
        total_exp = sum(item["amount"] for item in self.items)
        peoples = int(self.num_people.get())
        split_avg = total_exp/peoples

        self.to_label.configure(text=f"{total_exp}")
        self.sp_label.configure(text=f"{split_avg}")
    
    def clear_all(self):
        self.items.clear()
        self.display_result()

    
    def add_toList(self):
        peoples = self.num_people.get()
        amount = int(self.exp_amount.get())
        amount_len = self.exp_amount.get()
        name = self.exp_name.get()

        try:
            if len(peoples) == 0 or len(amount_len) == 0 or len(name) == 0:
                messagebox.showerror('Error', 'Empty string!!')
                return
            elif self.is_inList(name):
                messagebox.showerror("Error", "Item already exists")
                return
            else:
                # Save item
                self.items.append({
                    "name": name,
                    "amount": amount,
                })

                # Create UI card
                card = ItemCard(self.scroll, self, name, amount)
                card.pack(fill="x", pady=5)

                # Remove the text after add the details
                self.exp_name.delete(0, "end")
                self.exp_amount.delete(0, "end")

                # Calling display result function
                self.display_result()

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
if __name__ == "__main__":
    app = ExpenseSplitter()
    app.mainloop()



