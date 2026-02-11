import customtkinter as ctk
from datetime import datetime

# Appearance settings
ctk.set_appearance_mode("dark")   # "light" or "dark"
ctk.set_default_color_theme("blue")


class DigitalClock(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Digital Clock")
        self.geometry("400x200")
        self.resizable(False, False)

        # Center layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Main Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=20)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.main_frame.grid_rowconfigure((0, 1), weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Time Label
        self.time_label = ctk.CTkLabel(
            self.main_frame,
            text="00:00:00",
            font=("Segoe UI", 48, "bold")
        )
        self.time_label.grid(row=0, column=0, pady=(30, 10))

        # Date Label
        self.date_label = ctk.CTkLabel(
            self.main_frame,
            text="Date",
            font=("Segoe UI", 18)
        )
        self.date_label.grid(row=1, column=0, pady=(0, 20))

        # Start updating clock
        self.update_time()

    def update_time(self):
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%A, %d %B %Y")

        self.time_label.configure(text=current_time)
        self.date_label.configure(text=current_date)

        # Update every 1000 ms (1 second)
        self.after(1000, self.update_time)


if __name__ == "__main__":
    app = DigitalClock()
    app.mainloop()
