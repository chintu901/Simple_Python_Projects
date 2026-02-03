import customtkinter as ctk
from tkinter import messagebox

class Timer(ctk.CTk):
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

        # Timer variables
        self.time_left = 10  # seconds
        self.timer_running = False
        self.timer_id = None

        self.create_widgets()

    def create_widgets(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=4)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_rowconfigure(3, weight=1)

        # Title of the project
        title = ctk.CTkLabel(main_frame,
                             text="Timer",
                             font=ctk.CTkFont(size=30, weight="bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="ew")

        self.timer_label = ctk.CTkLabel(main_frame, 
                                   text=f"Time left: {self.time_left}",
                                   corner_radius=5,
                                   fg_color="#ffffff",
                                   font=ctk.CTkFont(size=50, weight="bold"))
        self.timer_label.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=20)

        self.timer_msg = ctk.CTkLabel(main_frame, 
                                 text="----------",
                                 fg_color="#ffffff",
                                 corner_radius=5,
                                 height=40,
                                 font=ctk.CTkFont(size=14, weight="normal"))
        self.timer_msg.grid(row=2, column=0, columnspan=3, sticky="ew", padx=20, pady=(0, 10))

        # Buttons elements

        stop_btn = ctk.CTkButton(main_frame,
                                 text="STOP",
                                 height=40,
                                 command=self.stop_timer,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        stop_btn.grid(row=3, column=0, sticky="ew", padx=10)

        reset_btn = ctk.CTkButton(main_frame,
                                 text="RESET",
                                 height=40,
                                 command=self.reset_timer,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        reset_btn.grid(row=3, column=1, sticky="ew", padx=10)

        start_btn = ctk.CTkButton(main_frame,
                                 text="START",
                                 height=40,
                                 command=self.start_timer,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        start_btn.grid(row=3, column=2, sticky="ew", padx=10)
    
    def update_timer(self):
        """Update the timer every second."""
        if self.time_left > 0 and self.timer_running:
            self.time_left -= 1
            self.timer_label.configure(text=f"Time left: {self.time_left}")
            self.timer_id = self.after(1000, self.update_timer) # Call the some function again after 1 second
        else:
            self.timer_running = False
            if self.time_left <= 0:
                self.timer_label.configure(text=f"Time left: {self.time_left}")
                self.timer_msg.configure(text="Time Out", text_color="#f76565")
    
    def start_timer(self):
        self.timer_running = True
        self.timer_msg.configure(text="----------")
        self.update_timer()
    
    def reset_timer(self):
        self.time_left = 10
        self.timer_msg.configure(text="Timer resetted!", text_color="black")
        self.timer_label.configure(text=f"Time left: {self.time_left}")
        self.timer_running = False

    def stop_timer(self):
        self.timer_running = False
        self.timer_msg.configure(text="Timer Stopped!!")

       

if __name__ == "__main__":
    app = Timer()
    app.mainloop()