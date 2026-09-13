import customtkinter as ctk
from tkinter import messagebox

class ItemCard(ctk.CTkFrame):
    def __init__(self, parent, app, subject, mrk):
        super().__init__(parent, corner_radius=8)

        self.app = app      # 🔥 reference to main app
        self.subject = subject    # store item name

        # Grid setup
        self.grid_columnconfigure((0,1,2), weight=1)

        ctk.CTkLabel(self, text=subject).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(self, text=mrk).grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkButton(self, text="Remove", command=self.remove_item).grid(row=0, column=2, padx=10, pady=10)

    
    def remove_item(self):
        # Remove from main app data
        self.app.items = [item for item in self.app.items if item["subject"] != self.subject]

        # Remove UI card
        self.destroy()

        # Call the display result
        self.app.display_result()

class GradeCalculator(ctk.CTk):
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
        main_frame = ctk.CTkFrame(self, corner_radius=0)
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        main_frame.grid_rowconfigure(0, weight=2)
        main_frame.grid_rowconfigure(1, weight=2)
        main_frame.grid_rowconfigure(2, weight=5)
        main_frame.grid_rowconfigure(3, weight=1)

        # UI Elements
        title_label = ctk.CTkLabel(main_frame,
                                   text="Grade Calculator",
                                   font=ctk.CTkFont(size=34, weight="bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=0, sticky="ew")

        self.subject_entry = ctk.CTkEntry(main_frame,
                                    placeholder_text="Enter subject",
                                    width=200,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.subject_entry.grid(row=1, column=0, padx=(10, 0), sticky="ew")

        self.marks_entry = ctk.CTkEntry(main_frame, 
                                    placeholder_text="Enter marks obtained",
                                    width=200,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.marks_entry.grid(row=1, column=1, padx=20, sticky="ew")

        submit_btn = ctk.CTkButton(main_frame,
                                   text="Submit",
                                   width=150,
                                   height=40,
                                   command=self.add_subject,
                                   font=ctk.CTkFont(size=14, weight="normal"))
        submit_btn.grid(row=1, column=2, padx=(0, 10), sticky="ew")

        # Marks card scrollable frame
        self.scroll = ctk.CTkScrollableFrame(main_frame, fg_color="#F2F2F2")
        self.scroll.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        self.scroll.grid_columnconfigure(0, weight=1)

        self.items = []

        # Result frame
        res_frame = ctk.CTkFrame(main_frame)
        res_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        res_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        res_frame.grid_rowconfigure((0, 1), weight=1)

        self.result_text_label = ctk.CTkLabel(res_frame,
                                    text="Result:",
                                    width=50,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.result_text_label.grid(row=0, column=0, padx=(10, 0), sticky="w")

        self.result_label = ctk.CTkLabel(res_frame,
                                    text="????",
                                    width=50,
                                    fg_color="#ffffff",
                                    corner_radius=5,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.result_label.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.total_text_label = ctk.CTkLabel(res_frame,
                                    text="Total Marks Obtained:",
                                    width=50,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.total_text_label.grid(row=1, column=0, padx=(10, 0), pady=5, sticky="w")

        self.total_label = ctk.CTkLabel(res_frame,
                                    text="????",
                                    width=50,
                                    fg_color="#ffffff",
                                    corner_radius=5,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.total_label.grid(row=1, column=1, padx=10, sticky="ew")

        self.grade_text_label = ctk.CTkLabel(res_frame,
                                    text="Grade:",
                                    width=50,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.grade_text_label.grid(row=0, column=2, padx=(10, 0), sticky="w")

        self.grade_label = ctk.CTkLabel(res_frame,
                                    text="????",
                                    width=50,
                                    fg_color="#ffffff",
                                    corner_radius=5,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.grade_label.grid(row=0, column=3, padx=10, pady=5, sticky="ew")

        self.sub_num_text_label = ctk.CTkLabel(res_frame,
                                    text="Number of subjects:",
                                    width=50,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.sub_num_text_label.grid(row=1, column=2, padx=(10, 0), sticky="w")

        self.sub_num_label = ctk.CTkLabel(res_frame,
                                    text="????",
                                    width=50,
                                    fg_color="#ffffff",
                                    corner_radius=5,
                                    height=40,
                                    font=ctk.CTkFont(size=14, weight="normal"))
        self.sub_num_label.grid(row=1, column=3, padx=10, pady=5, sticky="ew")
    
    def is_inList(self, sub):
        sub = sub.lower()

        for item in self.items:
            if item["subject"].lower() == sub:
                return True
        return False
    
    def display_result(self):
        """Finding and Displaying the result from the given subjects"""
        total_marks_obt = sum(item["mrk"] for item in self.items)
        total_subjects = len(self.items)
        total_marks = total_subjects*100

        if total_marks != 0:
            per = (total_marks_obt/total_marks)*100
        else:
            self.result_label.configure(text="---", text_color="#2b2b2b")
            self.grade_label.configure(text="---")
            self.total_label.configure(text="---")
            self.sub_num_label.configure(text="---")
            return

        # Grading the marks
        if 93 <= per <= 100:
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"A+ ({round(per,2)}%)")
        elif 85 <= per < 93:
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"A ({round(per,2)}%)")
        elif 80 <= per < 85:
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"A- ({round(per,2)}%)")
        elif 75 <= per < 80 :
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"B+ ({round(per,2)}%)")
        elif 70 <= per < 75 :
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"B ({round(per,2)}%)")
        elif 65 <= per < 70 :
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"B- ({round(per,2)}%)")
        elif 60 <= per < 65 :
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"C+ ({round(per,2)}%)")
        elif 55 <= per < 60 :
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"C ({round(per,2)}%)")
        elif 50 <= per < 55 :
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"C- ({round(per,2)}%)")
        elif 45 <= per < 50 :
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"D+ ({round(per,2)}%)")
        elif 40 <= per < 45 :
            self.result_label.configure(text="PASS", text_color="#57e170")
            self.grade_label.configure(text=f"D ({round(per,2)}%)")
        else:
            self.result_label.configure(text="FAIL", text_color="#e16757")
            self.grade_label.configure(text=f"F ({round(per,2)}%)")
        
        self.total_label.configure(text=f"{total_marks_obt}")
        self.sub_num_label.configure(text=f"{total_subjects}")

    
    def add_subject(self):
        std_mrk = float(self.marks_entry.get())
        m = self.marks_entry.get()
        std_sub = self.subject_entry.get()

        try:
            # Check duplicate
            if len(m) == 0 or len(std_sub) == 0:
                messagebox.showerror("Error", "Empty string!!")
            elif self.is_inList(std_sub):
                messagebox.showerror("Error", "Item already exists")
                return
            else:
                # Save item
                self.items.append({
                    "subject": std_sub,
                    "mrk": std_mrk,
                })

                # Create UI card
                card = ItemCard(self.scroll, self, std_sub, std_mrk)
                card.pack(fill="x", pady=5)

                # Remove the text after add the details
                self.subject_entry.delete(0, "end")
                self.marks_entry.delete(0, "end")

                # Calling display result function
                self.display_result()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app = GradeCalculator()
    app.mainloop()