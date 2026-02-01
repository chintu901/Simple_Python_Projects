import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

bank_balance = 2000

items = []

num_transaction = 0

class TransactionCard(ctk.CTkFrame):
    def __init__(self, parent, trans_type, amount, balance):
        super().__init__(parent, corner_radius=10)

        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Type
        ctk.CTkLabel(self, text=trans_type, font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=5)

        # Amount
        ctk.CTkLabel(self, text=f"₹{amount}", text_color="green").grid(row=0, column=1, padx=10)

        # Balance
        ctk.CTkLabel(self, text=f"Bal: ₹{balance}", text_color="gray").grid(row=0, column=2, padx=10)

class ATM_Simulator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window config
        self.title("Personal Finance Tracker")
        self.geometry("700x550")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)


        # Dictionary to store pages
        self.pages = {}

        # Create pages
        for Page in (VerificationPage, DashboardPage, WithdrawCash, MiniStatement, DepositMoney):
            page = Page(self.container, self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show first page
        self.show_page(VerificationPage)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.tkraise()

class VerificationPage(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        # Configure main grid (3 rows)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            self,
            fg_color="transparent",
            text="Welcome to SBI ATM",
            font=("Arial", 30, "bold")
        )
        title_label.grid(row=0, column=0, sticky="ew")

        # PIN Frame
        pin_frame = ctk.CTkFrame(self, fg_color="transparent")
        pin_frame.grid(row=1, column=0, sticky="nsew")

        pin_frame.grid_columnconfigure(0, weight=1)
        pin_frame.grid_columnconfigure(1, weight=4)
        pin_frame.grid_columnconfigure(0, weight=1)
        pin_frame.grid_rowconfigure(0, weight=1)

        # PIN Label
        pin_label = ctk.CTkLabel(
            pin_frame,
            text="Enter PIN:",
            font=("Arial", 16, "bold")
        )
        pin_label.grid(row=0, column=0, padx=10)

        # PIN Entry
        self.pin_entry = ctk.CTkEntry(
            pin_frame,
            width=250,
            height=40,
            show="*",
            font=("Arial", 16)
        )
        self.pin_entry.grid(row=0, column=1, padx=10, sticky="ew")

        # Enter Button
        enter_btn = ctk.CTkButton(
            pin_frame,
            text="Enter",
            width=120,
            height=40,
            command=self.Check_PIN,
            font=("Arial", 16, "bold")
        )
        enter_btn.grid(row=0, column=2, padx=20)

        # Footer for the app
        footer = ctk.CTkLabel(self,
                              text="This ATM Simulation is build by @Chota_Chetan",
                              fg_color="transparent",
                              font=("Arial", 12, "normal"))
        footer.grid(row=2, column=0, sticky="ew")
    
    def Check_PIN(self):
        pin = self.pin_entry.get()

        if pin == "1234":
            # Switch page
            self.app.show_page(DashboardPage)
        else:
            messagebox.showerror("Wrong PIN", "Try Again!!")
            return


class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        # Configure main grid (4 rows, 2 coulmn)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        # Load image
        self.logo = ctk.CTkImage(Image.open("Bank.png"), size=(250, 550))

         # Left column image
        img_label = ctk.CTkLabel(self,
                                text=" ",
                                image=self.logo)
        img_label.grid(row=0, column=0, rowspan=4, sticky="w")

        btn_style = {
            "width": 250,
            "height": 50,
            "corner_radius": 5,
            "font": ("Poppins", 15, "bold"),
            "text_color": "white"
        }

        # ================= Buttons =================
        btn_balance = ctk.CTkButton(self, text="Check Balance", command=self.on_balance, **btn_style)
        btn_balance.grid(row=0, column=1, padx=60, sticky="ew")

        btn_withdraw = ctk.CTkButton(self, text="Withdraw Cash",command=self.on_withdraw , **btn_style)
        btn_withdraw.grid(row=1, column=1, padx=60, sticky="ew")
        
        btn_statement = ctk.CTkButton(self, text="Deposit Money",command=self.on_deposit ,**btn_style)
        btn_statement.grid(row=2, column=1, padx=60, sticky="ew")
        
        btn_deposit = ctk.CTkButton(self, text="Mini-Statement",command=self.on_statement  ,**btn_style)
        btn_deposit.grid(row=3, column=1, padx=60, sticky="ew")

    
    def on_balance(self):
        global bank_balance
        balance = bank_balance

        popup = ctk.CTkToplevel(self)
        popup.geometry("400x200")   # ✅ YOU control size
        popup.title("Bank Balance")

        popup.grab_set()  # block main window

        label = ctk.CTkLabel(popup, text=f"Your Balance is ${balance}", font=("Arial", 20))
        label.pack(expand=True, pady=40)

        ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
        return
    
    def on_withdraw(self):
        # Switch page
        self.app.show_page(WithdrawCash)
    
    def on_statement(self):
        # Switch page
        self.app.show_page(MiniStatement)
    
    def on_deposit(self):
        # Switch page
        self.app.show_page(DepositMoney)


class WithdrawCash(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        # Configure main grid (3 rows)
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        title_label = ctk.CTkLabel(
            self,
            fg_color="transparent",
            text="Please enter the amount you wish to withdraw.",
            font=("Arial", 20, "normal")
        )
        title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        back_btn = ctk.CTkButton(self,
                                     text="Back",
                                     height=40,
                                     command=self.take_back,
                                     font=("Arial", 15, "normal"))
        back_btn.grid(row=0, column=1, padx=(5, 20), pady=(5,0), sticky="ne")

        self.withdraw_amount_entry = ctk.CTkEntry(self,
                                       placeholder_text="Enter Amount..",
                                       width=200,
                                       height=40,
                                       font=("Arial", 20, "normal"))
        self.withdraw_amount_entry.grid(row=1, column=0, padx=(20, 5), sticky="ew")

        withdraw_btn = ctk.CTkButton(self,
                                     text="Withdraw",
                                     height=40,
                                     command=self.withdraw_amount,
                                     font=("Arial", 20, "normal"))
        withdraw_btn.grid(row=1, column=1, padx=(5, 20), sticky="ew")

        # Footer for the app
        footer = ctk.CTkLabel(self,
                              text="This ATM Simulation is build by @Chota_Chetan",
                              fg_color="transparent",
                              font=("Arial", 12, "normal"))
        footer.grid(row=2, column=0, columnspan=2, sticky="ew")



    def withdraw_amount(self):
        global num_transaction
        global items
        global bank_balance
        amount_withdraw = self.withdraw_amount_entry.get()

        if len(amount_withdraw) == 0:
            messagebox.showerror("Error", "Empty String")
            return
        else:
            if bank_balance <= 0 or int(amount_withdraw) > bank_balance:
                messagebox.showerror("Error", "Insufficient Balance!")
                return
            else:
                bank_balance -= int(amount_withdraw)
                num_transaction += 1

                # Update the transactions
                items.append({
                    "amount": int(amount_withdraw),
                    "type": "Withdraw",
                    "balance": bank_balance,
                })

                popup = ctk.CTkToplevel(self)
                popup.geometry("400x200")   # popup msg screen size
                popup.title("Money Successfully Withdrawn")

                popup.grab_set()  # block main window

                label = ctk.CTkLabel(popup, text=f"Balance left: ${bank_balance}", font=("Arial", 20))
                label.pack(expand=True, pady=40)

                ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
                self.withdraw_amount_entry.delete(0, "end")
                return
            
    def take_back(self):
        # Switch page
        self.app.show_page(DashboardPage)
        self.withdraw_amount_entry.delete(0, "end")


class MiniStatement(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=4)

        
        # Title of the page
        title_label = ctk.CTkLabel(
            self,
            fg_color="transparent",
            text="Mini Statement of your Bank Account",
            font=("Arial", 20, "normal")
        )
        title_label.grid(row=0, column=0, columnspan=2, sticky="ew",  pady=50)

        back_btn = ctk.CTkButton(self,
                                text="Back",
                                height=40,
                                command=self.take_back,
                                font=("Arial", 15, "normal"))
        back_btn.grid(row=0, column=1, padx=(5, 20), pady=(5,0), sticky="ne")

        refresh_btn = ctk.CTkButton(self,
                                text="refresh",
                                height=40,
                                command=self.load_transaction,
                                font=("Arial", 15, "normal"))
        refresh_btn.grid(row=0, column=1, padx=(5, 170), pady=(5,0), sticky="ne")

        # Frame for bank details
        bnk_frame = ctk.CTkFrame(self, fg_color="transparent")
        bnk_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        bnk_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        bnk_frame.grid_rowconfigure(0, weight=1)

        balance_lable1 = ctk.CTkLabel(bnk_frame,
                                      text="Balance:",
                                      height=40,
                                      font=("Arial", 20, "normal"))
        balance_lable1.grid(row=0, column=0, sticky="e", padx=(0, 5))

        self.balance_amount = ctk.CTkLabel(bnk_frame,
                                           text=f"${bank_balance}",
                                           fg_color="#ffffff",
                                           corner_radius=5,
                                           height=40,
                                           font=("Arial", 20, "normal"))
        self.balance_amount.grid(row=0, column=1, sticky="w")

        transactions_label = ctk.CTkLabel(bnk_frame,
                                      text="Transactions:",
                                      height=40,
                                      font=("Arial", 20, "normal"))
        transactions_label.grid(row=0, column=2, sticky="e", padx=(0, 5))

        self.transaction_num = ctk.CTkLabel(bnk_frame,
                                           text=f"----",
                                           fg_color="#ffffff",
                                           corner_radius=5,
                                           height=40,
                                           font=("Arial", 20, "normal"))
        self.transaction_num.grid(row=0, column=3, sticky="w")

        # Header Frame
        header = ctk.CTkFrame(self, corner_radius=5)
        header.grid(row=2, column=0, columnspan=2, sticky="sew", padx=40)

        header.grid_columnconfigure((0,1,2), weight=1)

        ctk.CTkLabel(header, text="Type", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10)
        ctk.CTkLabel(header, text="Amount", font=("Arial", 14, "bold")).grid(row=0, column=1, padx=10)
        ctk.CTkLabel(header, text="Balance", font=("Arial", 14, "bold")).grid(row=0, column=2, padx=10)

        # Scrollable frame
        self.scroll = ctk.CTkScrollableFrame(self)
        self.scroll.grid(row=3, column=0, columnspan=2, padx=40, pady=10, sticky="new")
        self.scroll.grid_columnconfigure(0, weight=1)
    
    def load_transaction(self):
        # Clear old card
        for widget in self.scroll.winfo_children():
            widget.destroy()
        
        # Add new cards
        for item in items:
            card = TransactionCard(
                self.scroll,
                item["type"],
                item["amount"],
                item["balance"]
            )
            card.pack(fill="x", pady=5)
        
        self.balance_amount.configure(text=f"${bank_balance}")
        self.transaction_num.configure(text=f"{num_transaction}")

        
    
    def take_back(self):
        # Switch page
        self.app.show_page(DashboardPage)



class DepositMoney(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Title of the page
        title_label = ctk.CTkLabel(
            self,
            fg_color="transparent",
            text="Please enter the amount you wish to deposit.",
            font=("Arial", 20, "normal")
        )
        title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        back_btn = ctk.CTkButton(self,
                                text="Back",
                                height=40,
                                command=self.take_back,
                                font=("Arial", 15, "normal"))
        back_btn.grid(row=0, column=1, padx=(5, 20), pady=(5,0), sticky="ne")

        # Input UI Elemnets
        self.d_amount = ctk.CTkEntry(self,
                                     placeholder_text="Enter Amount..",
                                     height=40,
                                     font=("Arial", 20, "normal"))
        self.d_amount.grid(row=1, column=0, padx=10, sticky="ew")

        deposit_btn = ctk.CTkButton(self,
                                    text="Deposit",
                                    height=40,
                                    command=self.deposit_em,
                                    font=("Arial", 20, "normal"))
        deposit_btn.grid(row=1, column=1, padx=10, sticky="ew")

        # Footer
        footer = ctk.CTkLabel(self,
                              text="This ATM Simulation is build by @Chota_Chetan",
                              fg_color="transparent",
                              font=("Arial", 12, "normal"))
        footer.grid(row=2, column=0, columnspan=2, sticky="ew")

    def deposit_em(self):
        global num_transaction
        global items
        global bank_balance
        amount = self.d_amount.get()

        if len(amount) == 0:
            messagebox.showerror("Error", "Empty String!")
            return
        else:
            if amount.isalpha():
                messagebox.showerror("Error", "Enter number not alpha character!")
                return
            elif int(amount) < 0:
                messagebox.showerror("NegNum Error", "Please enter positive number")
            else:
                bank_balance += int(amount)
                num_transaction += 1

                items.append({
                    "amount": int(amount),
                    "type": "Deposit",
                    "balance": bank_balance,
                })

                popup = ctk.CTkToplevel(self)
                popup.geometry("400x200")
                popup.title("Money Successfully Deposited")

                popup.grab_set()    # Black the main screen

                label = ctk.CTkLabel(popup, text=f"Balance left: ${bank_balance}", font=("Arial", 20))
                label.pack(expand=True, pady=40)

                ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
                self.d_amount.delete(0, "end")
                return
            
    def take_back(self):
        self.app.show_page(DashboardPage)
        self.d_amount.delete(0, "end")



if __name__ == "__main__":
    app = ATM_Simulator()
    app.mainloop()