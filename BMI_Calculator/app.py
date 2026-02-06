import customtkinter as ctk
from tkinter import messagebox

class BMICalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window config
        self.title("Shopping List Manager")
        self.geometry("650x550")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Then widgets
        self.create_widgets()
    
    def create_widgets(self):

        # Main frame for the project
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=2)
        main_frame.grid_rowconfigure(3, weight=1)

        # title of the project
        title = ctk.CTkLabel(main_frame,
                             text="BMI Calculator",
                             font=ctk.CTkFont(size=30, weight="bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="ew")

        reset_btn = ctk.CTkButton(main_frame,
                                  text="Reset",
                                  fg_color="#e15151",
                                  hover_color="#d24343",
                                  height=40,
                                  font=ctk.CTkFont(size=15, weight="normal"))
        reset_btn.grid(row=0, column=2, padx=10, pady=(10, 0), sticky="ne")

        # Input screen
        self.height_entry = ctk.CTkEntry(main_frame,
                                    placeholder_text="Height in feet.....",
                                    height=40,
                                    font=ctk.CTkFont(size=15, weight="normal"))
        self.height_entry.grid(row=1, column=0, padx=(10,5), sticky="ew")

        self.weight_entry = ctk.CTkEntry(main_frame,
                                    placeholder_text="Weight in kg.....",
                                    height=40,
                                    font=ctk.CTkFont(size=15, weight="normal"))
        self.weight_entry.grid(row=1, column=1, padx=5, sticky="ew")

        sub_btn = ctk.CTkButton(main_frame,
                                text="Enter",
                                height=40,
                                command=self.calculate_bmi,
                                font=ctk.CTkFont(size=15, weight="normal"))
        sub_btn.grid(row=1, column = 2, padx=(5,10), sticky="ew")

        # Result frame
        result_frame = ctk.CTkFrame(main_frame)
        result_frame.grid(row=2, column=0, columnspan=3, padx=40, sticky="nsew")

        result_frame.grid_columnconfigure(0, weight=1)
        result_frame.grid_rowconfigure((0,1), weight=1)

        display_ans_frame = ctk.CTkFrame(result_frame, corner_radius=0)
        display_ans_frame.grid(row=0, column=0, sticky="nsew")

        display_ans_frame.grid_columnconfigure((0,1,2), weight=1)
        display_ans_frame.grid_rowconfigure(0, weight=2)
        display_ans_frame.grid_rowconfigure(1, weight=1)

        self.bmi_result_num = ctk.CTkLabel(display_ans_frame,
                                      text="00.0",
                                      font=ctk.CTkFont(size=60, weight="bold"))
        self.bmi_result_num.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="ns")

        bmi_text = ctk.CTkLabel(display_ans_frame,
                                text="BMI",
                                font=ctk.CTkFont(size=30, weight='normal'))
        bmi_text.grid(row=0, column=2, sticky="w")

        self.bmi_type_text = ctk.CTkLabel(display_ans_frame,
                                text="------",
                                font=ctk.CTkFont(size=20, weight="normal"))
        self.bmi_type_text.grid(row=1, column=2, sticky="w")

        display_info_frame = ctk.CTkFrame(result_frame, corner_radius=0)
        display_info_frame.grid(row=1, column=0, sticky="nsew")

        display_info_frame.grid_columnconfigure((0, 1, 2), weight=1)
        display_info_frame.grid_rowconfigure(0, weight=1)
        display_info_frame.grid_rowconfigure(1, weight=1)
        display_info_frame.grid_rowconfigure(2, weight=1)

        under_text = ctk.CTkLabel(display_info_frame,
                                  text="Underweight",
                                  text_color="#4d71cc",
                                  font=ctk.CTkFont(size=13, weight="normal"))
        under_text.grid(row=0, column=0, sticky="ew")

        normal_text = ctk.CTkLabel(display_info_frame,
                                  text="Normal",
                                  text_color="#4dcc73",
                                  font=ctk.CTkFont(size=13, weight="normal"))
        normal_text.grid(row=0, column=1, sticky="ew")

        over_text = ctk.CTkLabel(display_info_frame,
                                  text="Overweight",
                                  text_color="#cc574d",
                                  font=ctk.CTkFont(size=13, weight="normal"))
        over_text.grid(row=0, column=2, sticky="ew")

        under_line = ctk.CTkLabel(display_info_frame,
                                  text='',
                                  height=10,
                                  fg_color="#4d71cc")
        under_line.grid(row=1, column=0, sticky="ew", padx=(5,0))

        normal_line = ctk.CTkLabel(display_info_frame,
                                  text='',
                                  height=10,
                                  fg_color="#4dcc73")
        normal_line.grid(row=1, column=1, sticky="ew", padx=0)

        over_line = ctk.CTkLabel(display_info_frame,
                                  text='',
                                  height=10,
                                  fg_color="#cc574d")
        over_line.grid(row=1, column=2, sticky="ew", padx=(0,5))

        number_info_frame = ctk.CTkFrame(display_info_frame, fg_color="transparent")
        number_info_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")

        number_info_frame.grid_columnconfigure((0,1,2,3), weight=1)
        number_info_frame.grid_rowconfigure(0, weight=1)

        num1 = ctk.CTkLabel(number_info_frame,
                            text="16.0",
                            font=ctk.CTkFont(size=15, weight="normal"))
        num1.grid(row=0, column=0, sticky="nw")

        num2 = ctk.CTkLabel(number_info_frame,
                            text="18.5",
                            font=ctk.CTkFont(size=15, weight="normal"))
        num2.grid(row=0, column=1, sticky="new", padx=(0,25))

        num3 = ctk.CTkLabel(number_info_frame,
                            text="25.0",
                            font=ctk.CTkFont(size=15, weight="normal"))
        num3.grid(row=0, column=2, sticky="new", padx=(25,0))

        num4 = ctk.CTkLabel(number_info_frame,
                            text="40.0",
                            font=ctk.CTkFont(size=15, weight="normal"))
        num4.grid(row=0, column=3, sticky="ne")
    
    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            height = height * 0.3048
            weight = float(self.weight_entry.get())
            bmi = weight / (height ** 2)

            self.bmi_result_num.configure(text=f"{round(bmi,1)}")

            self.bmi_type(bmi)

            self.height_entry.delete(0, "end")
            self.weight_entry.delete(0, "end")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def bmi_type(self, bmi):
        if 0 <= bmi <= 18.5:
            self.bmi_type_text.configure(text="Underweight", text_color="#4d71cc")
        elif 18.5 < bmi <= 25:
            self.bmi_type_text.configure(text="Normal", text_color="#4dcc73")
        elif 25 < bmi < 100:
            self.bmi_type_text.configure(text="Overweight", text_color="#cc574d")


if __name__ == "__main__":
    app = BMICalculator()
    app.mainloop()

