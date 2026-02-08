import customtkinter as ctk


class CalculatorApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        
        self.left_number = ""
        self.operation = ""
        self.right_number = ""

        # -------------------- App Setup --------------------
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Calculator")
        self.geometry("360x520")
        self.resizable(False, False)

        # -------------------- Display --------------------
        self.display = ctk.CTkEntry(
            self,
            height=80,
            font=("Segoe UI", 32),
            justify="right",
            corner_radius=12
        )
        self.display.pack(padx=20, pady=(20, 10), fill="x")

        # -------------------- Button Frame --------------------
        self.btn_frame = ctk.CTkFrame(self, corner_radius=12)
        self.btn_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # -------------------- Button Layout --------------------
        self.buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["0", ".", "="]
        ]

        self._create_buttons()

    # -------------------- Create Buttons --------------------
    def _create_buttons(self):
        btn_font = ("Segoe UI", 20)
        btn_height = 60
        btn_width = 70

        for row_index, row in enumerate(self.buttons):
            self.btn_frame.rowconfigure(row_index, weight=1)

            col_index = 0
            for text in row:
                self.btn_frame.columnconfigure(col_index, weight=1)

                # Wide "0" button
                if text == "0":
                    self.btn = ctk.CTkButton(
                        self.btn_frame,
                        text=text,
                        font=btn_font,
                        height=btn_height,
                        corner_radius=12,
                         command=lambda t=text: self.handle_button(t)
                    )
                    self.btn.grid(
                        row=row_index,
                        column=col_index,
                        columnspan=2,
                        padx=6,
                        pady=6,
                        sticky="nsew"
                    )
                    col_index += 2
                else:
                    self.btn = ctk.CTkButton(
                        self.btn_frame,
                        text=text,
                        font=btn_font,
                        width=btn_width,
                        height=btn_height,
                        corner_radius=12,
                         command=lambda t=text: self.handle_button(t)
                    )
                    self.btn.grid(
                        row=row_index,
                        column=col_index,
                        padx=6,
                        pady=6,
                        sticky="nsew"
                    )
                    col_index += 1
    
    def update_display(self):
        value = self.left_number + self.operation + self.right_number
        self.display.delete(0, "end")
        self.display.insert(0, value)

    
    def handle_button(self, value):

        # ---------------- Clear ----------------
        if value == "C":
            self.left_number = ""
            self.operation = ""
            self.right_number = ""
            self.update_display()
            return

        # ---------------- Numbers & Decimal ----------------
        if value.isdigit() or value == ".":
            if self.operation == "":
                self.left_number += value
            else:
                self.right_number += value
            self.update_display()
            return

        # ---------------- Operators ----------------
        if value in ["+", "−", "×", "÷"]:
            if self.left_number != "":
                self.operation = value
            self.update_display()
            return

        # ---------------- Equals ----------------
        if value == "=":
            if self.left_number and self.operation and self.right_number:
                result = self.calculate()

                self.left_number = str(result)
                self.operation = ""
                self.right_number = ""

                self.update_display()
            return

        # ---------------- Plus / Minus ----------------
        if value == "±":
            if self.operation == "":
                if self.left_number.startswith("-"):
                    self.left_number = self.left_number[1:]
                else:
                    self.left_number = "-" + self.left_number
            else:
                if self.right_number.startswith("-"):
                    self.right_number = self.right_number[1:]
                else:
                    self.right_number = "-" + self.right_number

            self.update_display()
            return

        # ---------------- Percentage ----------------
        if value == "%":
            try:
                if self.operation == "":
                    self.left_number = str(float(self.left_number) / 100)
                else:
                    self.right_number = str(float(self.right_number) / 100)
                self.update_display()
            except:
                pass

    def calculate(self):
        try:
            left = float(self.left_number)
            right = float(self.right_number)

            if self.operation == "+":
                return left + right
            elif self.operation == "−":
                return left - right
            elif self.operation == "×":
                return left * right
            elif self.operation == "÷":
                return left / right
        except:
            return "Error"



# -------------------- Run App --------------------
if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
