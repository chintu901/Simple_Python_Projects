import customtkinter as ctk
import random
from tkinter import messagebox

class RockPaperScissors(ctk.CTk):
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

        self.string = ["ROCK", "PAPER", "SCISSORS"]
        self.answer = ""
        self.computer_score = 0
        self.human_score = 0

        self.create_widgets()
    
    def create_widgets(self):
        #main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.grid_columnconfigure((0,1,2), weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=2)
        main_frame.grid_rowconfigure(3, weight=1)
        main_frame.grid_rowconfigure(4, weight=1)

        #Title of the project
        title = ctk.CTkLabel(main_frame,
                             text="Rock Paper Scissors",
                             font=ctk.CTkFont(size=30, weight="bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="ew")

        computer_ans_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        computer_ans_frame.grid(row=1, column=0, columnspan=3, sticky="nsew")

        computer_ans_frame.grid_columnconfigure(0, weight=1)
        computer_ans_frame.grid_rowconfigure(0, weight=1)

        self.computer_ans = ctk.CTkLabel(computer_ans_frame,
                                    text="---------",
                                    fg_color="white",
                                    height=40,
                                    width=300,
                                    corner_radius=5,
                                    font=ctk.CTkFont(size=15, weight="normal"))
        self.computer_ans.grid(row=0, column=0)

        self.score_board = ctk.CTkLabel(main_frame,
                                   text=f"{self.computer_score} : {self.human_score}",
                                   font=ctk.CTkFont(size=40, weight="bold"))
        self.score_board.grid(row=2, column=0, columnspan=3, sticky="ew")

        computer_lable = ctk.CTkLabel(main_frame,
                                      text="COMP.",
                                      font=ctk.CTkFont(size=40, weight="bold"))
        computer_lable.grid(row=2, column=0, sticky="ew")

        you_lable = ctk.CTkLabel(main_frame,
                                      text="YOU.",
                                      font=ctk.CTkFont(size=40, weight="bold"))
        you_lable.grid(row=2, column=2, sticky="ew")

        self.user_ans = ctk.CTkLabel(main_frame,
                                text="---------",
                                height=40,
                                width=300,
                                fg_color="white",
                                corner_radius=5,
                                font=ctk.CTkFont(size=15, weight="normal"))
        self.user_ans.grid(row=3, column=0, columnspan=3)

        # Buttons
        rock_btn = ctk.CTkButton(main_frame,
                                 text="-- ROCK --",
                                 height=40,
                                 command=self.do_rock,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        rock_btn.grid(row=4, column=0, padx=10, sticky="ew", pady=(0, 30))

        paper_btn = ctk.CTkButton(main_frame,
                                 text="-- PAPER --",
                                 height=40,
                                 command=self.do_paper,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        paper_btn.grid(row=4, column=1, padx=10, sticky="ew", pady=(0, 30))

        scissor_btn = ctk.CTkButton(main_frame,
                                 text="-- SCISSORS --",
                                 height=40,
                                 command= self.do_scissor,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        scissor_btn.grid(row=4, column=2, padx=10, sticky="ew", pady=(0, 30))

    def on_click(self):
        computer_ans = random.choice(self.string)
        self.computer_ans.configure(text=f"{computer_ans}")

        if computer_ans == "ROCK" and self.answer == "PAPER":
            self.human_score += 1
            self.score_board.configure(text=f"{self.computer_score} : {self.human_score}")
        elif computer_ans == "PAPER" and self.answer == "ROCK":
            self.computer_score += 1
            self.score_board.configure(text=f"{self.computer_score} : {self.human_score}")
        elif computer_ans == "ROCK" and self.answer == "SCISSORS":
            self.computer_score += 1
            self.score_board.configure(text=f"{self.computer_score} : {self.human_score}")
        elif computer_ans == "SCISSORS" and self.answer == "ROCK":
            self.human_score += 1
            self.score_board.configure(text=f"{self.computer_score} : {self.human_score}")
        elif computer_ans == "SCISSORS" and self.answer == "PAPER":
            self.computer_score += 1
            self.score_board.configure(text=f"{self.computer_score} : {self.human_score}")
        elif computer_ans == "PAPER" and self.answer == "SCISSORS":
            self.human_score += 1
            self.score_board.configure(text=f"{self.computer_score} : {self.human_score}")
        else:
            pass


    def check_ans(self):
        if self.answer == "ROCK":
            self.user_ans.configure(text="ROCK")
        elif self.answer == "PAPER":
            self.user_ans.configure(text="PAPER")
        elif self.answer == "SCISSORS":
            self.user_ans.configure(text="SCISSORS")
        self.on_click()
    
    def do_rock(self):
        self.answer = "ROCK"
        self.check_ans()
    
    def do_paper(self):
        self.answer = "PAPER"
        self.check_ans()

    def do_scissor(self):
        self.answer = "SCISSORS"
        self.check_ans()
    

if __name__ == "__main__":
    app = RockPaperScissors()
    app.mainloop()