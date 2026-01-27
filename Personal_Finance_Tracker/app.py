import customtkinter as ctk
from tkinter import messagebox

class PersonalFinanceTracker(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window config
        self.title("Personal Finance Tracker")
        self.geometry("700x550")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ctk.CTkFrame(self, corner_radius=0)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=2)
        main_frame.grid_rowconfigure(1, weight=6)
        main_frame.grid_rowconfigure(2, weight=2)

        # Title of the project
        title_label = ctk.CTkLabel(main_frame,
                                   text="Personal Finance Tracker",
                                   font=ctk.CTkFont(size=34, weight="bold"))
        title_label.grid(row=0, column=0, sticky="new")

        # Input frame
        input_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        input_frame.grid(row=1, column=0, sticky="nsew")

        input_frame.grid_columnconfigure((0,1,2), weight=1)
        input_frame.grid_rowconfigure(0, weight=2)
        input_frame.grid_rowconfigure(1, weight=6)
        input_frame.grid_rowconfigure(2, weight=2)

        # UI elements for input frame
        income_label = ctk.CTkLabel(input_frame,
                                    text="Income:",
                                    height=40,
                                    font=ctk.CTkFont(size=15, weight="normal"))
        income_label.grid(row=0, column=0, padx=(20, 0), sticky="w")

        self.inc_entry = ctk.CTkEntry(input_frame,
                                 placeholder_text="Enter Amount '$'",
                                 width=200,
                                 height=40,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        self.inc_entry.grid(row=0, column=1, columnspan=2, sticky="w")

        # Input frame for Expenses info..
        x_info_frame = ctk.CTkFrame(input_frame, corner_radius=5, fg_color="#b5b5b5")
        x_info_frame.grid(row=1, column=0, columnspan=3, padx=10, sticky="nsew")

        x_info_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        x_info_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Expenses info UI elements
        title2 = ctk.CTkLabel(x_info_frame,
                              text="Expenses",
                              font=ctk.CTkFont(size=20, weight="bold"))
        title2.grid(row=0, column=0, columnspan=4, padx=5, sticky="nw")

        rent_label = ctk.CTkLabel(x_info_frame,
                                  text="Rent:",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        rent_label.grid(row=1, column=0, sticky="ew")

        self.rent_entry = ctk.CTkEntry(x_info_frame,
                                  placeholder_text="---",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        self.rent_entry.grid(row=1, column=1, sticky="ew", padx=(0, 10))

        food_label = ctk.CTkLabel(x_info_frame,
                                  text="Food:",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        food_label.grid(row=1, column=2, sticky="ew")

        self.food_entry = ctk.CTkEntry(x_info_frame,
                                  placeholder_text="---",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        self.food_entry.grid(row=1, column=3, sticky="ew", padx=(0, 10))

        transport_label = ctk.CTkLabel(x_info_frame,
                                  text="Transport:",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        transport_label.grid(row=2, column=0, sticky="ew")

        self.transport_entry = ctk.CTkEntry(x_info_frame,
                                  placeholder_text="---",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        self.transport_entry.grid(row=2, column=1, sticky="ew", padx=(0, 10))

        savings_label = ctk.CTkLabel(x_info_frame,
                                  text="Savings:",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        savings_label.grid(row=2, column=2, sticky="ew")

        self.savings_entry = ctk.CTkEntry(x_info_frame,
                                  placeholder_text="---",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        self.savings_entry.grid(row=2, column=3, sticky="ew", padx=(0, 10))

        # Buttons frame
        btn_frame = ctk.CTkFrame(input_frame)
        btn_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")

        btn_frame.grid_columnconfigure((0, 1), weight=1)
        btn_frame.grid_rowconfigure(0, weight=1)

        # Button frame UI elemnets
        smt_button = ctk.CTkButton(btn_frame,
                                   text="Calculate",
                                   fg_color="#71c967",
                                   hover_color="#469f3c",
                                   height=50,
                                   command=self.calculate_inc,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        smt_button.grid(row=0, column=0, padx=10, sticky="ew")

        rst_button = ctk.CTkButton(btn_frame,
                                   text="Reset",
                                   fg_color="#e96b6b",
                                   hover_color="#db4444",
                                   command=self.reset_result,
                                   height=50,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        rst_button.grid(row=0, column=1, padx=10, sticky="ew")

        # Display calculated result
        result_frame = ctk.CTkFrame(main_frame, corner_radius=3, fg_color="#b5b5b5")
        result_frame.grid(row=2, column=0, sticky="nsew")

        result_frame.grid_columnconfigure((0, 1, 2), weight=1)
        result_frame.grid_rowconfigure((0, 1), weight=1)

        # UI elements for result
        total_exp = ctk.CTkLabel(result_frame,
                                 text="Total Expenses:",
                                 height=40,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        total_exp.grid(row=0, column=0, sticky="ew")

        self.exp_ans = ctk.CTkLabel(result_frame,
                               text="----",
                               fg_color="#ffffff",
                               corner_radius=5,
                               height=40,
                               font=ctk.CTkFont(size=15, weight="normal"))
        self.exp_ans.grid(row=0, column=1, sticky="ew")

        balance_label = ctk.CTkLabel(result_frame,
                                 text="Balance:",
                                 height=40,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        balance_label.grid(row=1, column=0, sticky="ew")

        self.balance_ans = ctk.CTkLabel(result_frame,
                               text="----",
                               fg_color="#ffffff",
                               corner_radius=5,
                               height=40,
                               font=ctk.CTkFont(size=15, weight="normal"))
        self.balance_ans.grid(row=1, column=1, sticky="ew")

        self.balance_msg = ctk.CTkLabel(result_frame,
                               text="----  no judgment ----",
                               corner_radius=5,
                               height=40,
                               font=ctk.CTkFont(size=15, weight="normal"))
        self.balance_msg.grid(row=1, column=2, padx=10, sticky="ew")
    
    def reset_result(self):
        self.balance_ans.configure(text="----")
        self.exp_ans.configure(text="----")
        self.balance_msg.configure(text="----  no judgment ----")

        # Remove the text after add the details
        self.inc_entry.delete(0, "end")
        self.rent_entry.delete(0, "end")
        self.food_entry.delete(0, "end")
        self.transport_entry.delete(0, "end")
        self.savings_entry.delete(0, "end")

    
    def calculate_inc(self):
        try:
            income_amount = self.inc_entry.get()
            rent_exp = self.rent_entry.get()
            food_exp = self.food_entry.get()
            transport_exp = self.transport_entry.get()
            saving_exp = self.savings_entry.get()

            if len(income_amount) == 0 or len(rent_exp) == 0 or len(food_exp) == 0 or len(transport_exp) == 0 or len(saving_exp) == 0:
                messagebox.showerror("Error", "String is empty")
                return
            else:
                total_exp = int(rent_exp) + int(food_exp) + int(transport_exp) + int(saving_exp)
                self.exp_ans.configure(text=f"${total_exp}")

                balance_left = int(income_amount) - total_exp
                per_balance = (balance_left / int(income_amount)) * 100
                if per_balance > 15:
                    self.balance_msg.configure(text=f"🎉 Excellent! You're saving {round(per_balance, 1)}%")
                    self.balance_ans.configure(text=f"{balance_left}", text_color="#469f3c")
                elif 5 <= per_balance < 15:
                    self.balance_msg.configure(text=f"✅ Good job! Your {round(per_balance, 1)}% savings")
                    self.balance_ans.configure(text=f"{balance_left}", text_color="#469f3c")
                elif 0 <= per_balance < 5:
                    self.balance_msg.configure(text=f"⚠️  Close call! Only {round(per_balance, 1)}% left")
                    self.balance_ans.configure(text=f"{balance_left}", text_color="#469f3c")
                else:
                    self.balance_msg.configure(text=f"❌ Overspending!")
                    self.balance_ans.configure(text=f"{balance_left}", text_color="#db4444")

                # Remove the text after add the details
                self.inc_entry.delete(0, "end")
                self.rent_entry.delete(0, "end")
                self.food_entry.delete(0, "end")
                self.transport_entry.delete(0, "end")
                self.savings_entry.delete(0, "end")


        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = PersonalFinanceTracker()
    app.mainloop()