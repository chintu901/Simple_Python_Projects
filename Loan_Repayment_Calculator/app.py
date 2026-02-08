import customtkinter as ctk

class LoanRepaymentCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Loan Repayment Calculator")
        self.geometry("1000x650")
        self.minsize(1000, 650)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Make window expandable
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.pages_container = ctk.CTkFrame(self, corner_radius=0)
        self.pages_container.grid(row=0, column=1, sticky="nsew")
        self.pages_container.grid_rowconfigure(0, weight=1)
        self.pages_container.grid_columnconfigure(0, weight=1)

        # Store pages
        self.pages = {}

        # Create all pages
        for Page in (DashboardPage, WithdrawPage):
            page = Page(self.pages_container, self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")

        # Show first page
        self.show_page(DashboardPage)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.tkraise()

# ==================== Sidebar ====================
class Sidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=230, corner_radius=0)

        self.grid_rowconfigure(5, weight=1)

        title = ctk.CTkLabel(
            self,
            text="Loan Tools",
            font=("Segoe UI", 22, "bold")
        )
        title.grid(row=0, column=0, padx=20, pady=(30, 20), sticky="w")

        self.btn_dashboard = ctk.CTkButton(
            self,
            text="📊 Dashboard",
            height=45,
            corner_radius=12
        )
        self.btn_dashboard.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.btn_schedule = ctk.CTkButton(
            self,
            text="📅 Repayment Schedule",
            height=45,
            corner_radius=12
        )
        self.btn_schedule.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_early = ctk.CTkButton(
            self,
            text="🎯 Early Payoff Simulator",
            height=45,
            corner_radius=12
        )
        self.btn_early.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

# ==================== Dashboard Page ====================
class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.controller = controller

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        self._create_header()
        self._create_input_card()
        self._create_result_card()

        self.type_of_loan = ""

    # -------- Header --------
    def _create_header(self):
        header_frame = ctk.CTkFrame(self, corner_radius=0)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=30, pady=(30, 20))

        title = ctk.CTkLabel(
            header_frame,
            text="Loan Repayment Calculator",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(anchor="w")

        subtitle = ctk.CTkLabel(
            header_frame,
            text="Plan your EMI smartly — Home, Car & Personal Loans",
            font=("Segoe UI", 14),
            text_color="gray"
        )
        subtitle.pack(anchor="w", pady=(5, 0))

    # -------- Input Card --------
    def _create_input_card(self):
        card = ctk.CTkFrame(self, corner_radius=18)
        card.grid(row=1, column=0, sticky="nsew", padx=(30, 15), pady=20)

        card.grid_columnconfigure(1, weight=1)

        title = ctk.CTkLabel(
            card,
            text="Loan Details",
            font=("Segoe UI", 20, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 15), sticky="w")

        ctk.CTkLabel(card, text="Loan Type").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.loan_type = ctk.CTkComboBox(
            card,
            values=["Home Loan", "Car Loan", "Personal Loan"]
        )
        self.loan_type.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        self.loan_type.set("Select Loan Type")

        ctk.CTkLabel(card, text="Principal Amount (₹)").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.principal = ctk.CTkEntry(card)
        self.principal.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        ctk.CTkLabel(card, text="Interest Rate (% p.a.)").grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.interest = ctk.CTkEntry(card)
        self.interest.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        ctk.CTkLabel(card, text="Tenure (Years)").grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.tenure = ctk.CTkEntry(card)
        self.tenure.grid(row=4, column=1, padx=20, pady=10, sticky="ew")

        self.calculate_btn = ctk.CTkButton(
            card,
            text="CALCULATE EMI",
            height=55,
            command=self.calculate_emi,
            font=("Segoe UI", 17, "bold"),
            corner_radius=14
        )
        self.calculate_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=(25, 20), sticky="ew")

    # -------- Results Card --------
    def _create_result_card(self):
        card = ctk.CTkFrame(self, corner_radius=18)
        card.grid(row=1, column=1, sticky="nsew", padx=(15, 30), pady=20)

        title = ctk.CTkLabel(
            card,
            text="Quick Results",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(anchor="w", padx=20, pady=(20, 15))

        self.monthly_emi = ctk.CTkLabel(
            card,
            text="₹ 0",
            font=("Segoe UI", 34, "bold")
        )
        self.monthly_emi.pack(anchor="w", padx=20, pady=(0, 15))

        self.total_payable = ctk.CTkLabel(
            card,
            text="Total Payable: ₹ 0",
            font=("Segoe UI", 14)
        )
        self.total_payable.pack(anchor="w", padx=20, pady=5)

        self.total_interest = ctk.CTkLabel(
            card,
            text="Total Interest: ₹ 0",
            font=("Segoe UI", 14)
        )
        self.total_interest.pack(anchor="w", padx=20, pady=5)

        self.tenure_info = ctk.CTkLabel(
            card,
            text="Tenure: 0 months",
            font=("Segoe UI", 14)
        )
        self.tenure_info.pack(anchor="w", padx=20, pady=(5, 20))

    def update_loan_type(self, choice):
        self.type_of_loan = choice
        return
    
    def calculate_emi(self):
        loan_type = self.type_of_loan
        amount = int(self.principal.get())
        interset_rate = float(self.interest.get()) / 100
        years = float(self.tenure.get())

        tenure_month = years * 12
        monthly_rate = float((interset_rate / 12))
        emi = (amount * monthly_rate * (1 + monthly_rate)**tenure_month) / ((1 + monthly_rate)**tenure_month - 1)
        total_payable = emi * tenure_month
        total_interest = total_payable - amount

        self.monthly_emi.configure(text=f"₹ {int(emi)}")
        self.total_payable.configure(text=f"Total Payable: ₹ {int(total_payable)}")
        self.total_interest.configure(text=f"Total Interest: ₹ {int(total_interest)}")
        self.tenure_info.configure(text=f"Tenure: {int(tenure_month)} months")

        

class WithdrawPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self, text="Withdraw Money", font=("Arial", 30)).grid(row=0, column=0)

        ctk.CTkButton(self, text="Back", command=lambda: app.show_page(DashboardPage)).grid(row=1, column=0)


if __name__ == "__main__":
    app = LoanRepaymentCalculator()
    app.mainloop()
