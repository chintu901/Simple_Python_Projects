import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


# -----------------------------
# App Controller
# -----------------------------
class TeddyDayQuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Teddy Day Couple Quiz 🧸")
        self.geometry("570x595")
        self.resizable(False, False)

        self.container = ctk.CTkFrame(self, corner_radius=0)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for Page in (WelcomePage, QuizPage, ResultPage):
            page = Page(self.container, self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(WelcomePage)

    def show_page(self, page_class):
        self.pages[page_class].tkraise()


# -----------------------------
# Welcome Page
# -----------------------------
class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            self,
            text="Teddy Day Couple Quiz 🧸",
            font=("Segoe UI", 36, "bold")
        ).grid(row=0, column=0, pady=(80, 20))

        ctk.CTkLabel(
            self,
            text="A cute little quiz to test your love vibe 💖",
            font=("Segoe UI", 18)
        ).grid(row=1, column=0, pady=(0, 40))

        ctk.CTkButton(
            self,
            text="Start Quiz 🧸",
            fg_color="#eb81f0",
            hover_color="#cf66d5",
            width=220,
            height=50,
            font=("Segoe UI", 18),
            command=self.start_quiz
        ).grid(row=2, column=0)

    def start_quiz(self):
        quiz_page = self.controller.pages[QuizPage]
        quiz_page.reset_quiz()
        self.controller.show_page(QuizPage)


# -----------------------------
# Quiz Page
# -----------------------------
class QuizPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure((0, 1), weight=1)

        self.question_label = ctk.CTkLabel(
            self,
            text="",
            font=("Segoe UI", 22),
            wraplength=480,
            justify="center"
        )
        self.question_label.grid(row=0, column=0, columnspan=2, pady=(40, 20))

        self.teddy_image = ctk.CTkLabel(
            self,
            text="🧸",
            font=("Segoe UI", 120)
        )
        self.teddy_image.grid(row=1, column=0, columnspan=2, pady=10)

        self.answer_buttons = []
        for i in range(3):
            btn = ctk.CTkButton(
                self,
                height=55,
                fg_color="#eb81f0",
                hover_color="#cf66d5",
                font=("Segoe UI", 16),
                command=lambda i=i: self.handle_answer(i)
            )
            btn.grid(row=2+i, column=0, columnspan=2, pady=10, padx=120, sticky="ew")
            self.answer_buttons.append(btn)

        self.progress = ctk.CTkProgressBar(self, width=400, progress_color="#9a489e")
        self.progress.grid(row=5, column=0, columnspan=2, pady=(30, 10))

        self.reset_quiz()

    def reset_quiz(self):
        self.current_question = 0
        self.score = 0
        self.load_question()

    def load_question(self):
        question_data = QUESTIONS[self.current_question]

        self.question_label.configure(text=question_data["question"])
        self.teddy_image.configure(text="🧸")

        for btn, option in zip(self.answer_buttons, question_data["options"]):
            btn.configure(text=option[0])

        progress_value = self.current_question / len(QUESTIONS)
        self.progress.set(progress_value)

    def handle_answer(self, option_index):
        _, points = QUESTIONS[self.current_question]["options"][option_index]
        self.score += points
        self.current_question += 1

        if self.current_question < len(QUESTIONS):
            self.load_question()
        else:
            result_page = self.controller.pages[ResultPage]
            result_page.set_result(self.score)
            self.controller.show_page(ResultPage)


# -----------------------------
# Result Page
# -----------------------------
class ResultPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)

        self.tier_label = ctk.CTkLabel(
            self,
            font=("Segoe UI", 32, "bold")
        )
        self.tier_label.grid(row=0, column=0, pady=(60, 20))

        ctk.CTkLabel(
            self,
            text="🧸",
            font=("Segoe UI", 120)
        ).grid(row=1, column=0)

        self.message_label = ctk.CTkLabel(
            self,
            font=("Segoe UI", 18),
            wraplength=450,
            justify="center"
        )
        self.message_label.grid(row=2, column=0, pady=30)

        ctk.CTkButton(
            self,
            text="Back to Home",
            width=200,
            height=45,
            fg_color="#eb81f0",
            hover_color="#cf66d5",
            command=lambda: controller.show_page(WelcomePage)
        ).grid(row=3, column=0)

    def set_result(self, score):
        for tier in TIERS:
            if tier["min"] <= score <= tier["max"]:
                self.tier_label.configure(text=tier["title"])
                self.message_label.configure(text=tier["message"])
                break

# -----------------------------
# Question Data
# -----------------------------
QUESTIONS = [
    {
        "question": "If your partner gifts you a teddy, what does it mean most to you?",
        "options": [
            ("It’s cute 🧸", 1),
            ("It reminds me of them 💕", 2),
            ("It feels like a hug ❤️", 3)
        ],
        "image": "R.png"
    },
    {
        "question": "What color teddy suits your partner the most?",
        "options": [
            ("🤍 White (soft & calm)", 1),
            ("Brown (warm & caring)", 2),
            ("Red (romantic & bold)", 3)
        ],
        "image": "R_r.png"
    },
    {
        "question": "Your partner is sad. What teddy move do you choose?",
        "options": [
            ("Gift a teddy silently", 1),
            ("Hug + teddy", 2),
            ("Teddy + note + hug", 3)
        ],
        "image": "up_down.png"
    },
    {
        "question": "Where would your partner keep a teddy gift?",
        "options": [
            ("On a shelf", 1),
            ("On the bed", 2),
            ("Always close to them", 3)
        ],
        "image": "brown_bow.png"
    },
    {
        "question": "If a teddy could talk, what would it say for your partner?",
        "options": [
            ("Smile!", 1),
            ("I’m always with you", 2),
            ("You are deeply loved", 3)
        ],
        "image": "R.png"
    },
    {
        "question": "What’s the best Teddy Day surprise?",
        "options": [
            ("Simple teddy", 1),
            ("Teddy + flowers", 2),
            ("Teddy + heartfelt moment", 3)
        ],
        "image": "R_r.png"
    },
    {
        "question": "How does your partner react to cute gifts?",
        "options": [
            ("Smiles quietly", 1),
            ("Gets excited", 2),
            ("Emotional & expressive", 3)
        ],
        "image": "R.png"
    },
    {
        "question": "Your teddy represents your relationship as…",
        "options": [
            ("Soft and comfy", 1),
            ("Warm and caring", 2),
            ("Forever and safe", 3)
        ],
        "image": "family.png"
    },
    {
        "question": "What would you name your couple teddy?",
        "options": [
            ("Mr. Fluffy", 1),
            ("Love Bear", 2),
            ("Our Heart", 3)
        ],
        "image": "red_bow.png"
    },
    {
        "question": "What makes Teddy Day special for you?",
        "options": [
            ("Cute gifts", 1),
            ("Shared moments", 2),
            ("Emotional connection", 3)
        ],
        "image": "up_down.png"
    },
]


# -----------------------------
# Tier Logic
# -----------------------------
TIERS = [
    {"min": 0, "max": 10, "title": "🧸 Cute Crush", "message": "Sweet and gentle love."},
    {"min": 11, "max": 18, "title": "💕 Teddy Buddies", "message": "Warm, caring, and comfy."},
    {"min": 19, "max": 25, "title": "💖 Heart Stealers", "message": "Strong emotional bond."},
    {"min": 26, "max": 30, "title": "💍 Teddy Soulmates", "message": "Deep and secure love."},
]


if __name__ == "__main__":
    app = TeddyDayQuizApp()
    app.mainloop()
