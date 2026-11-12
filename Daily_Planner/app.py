import customtkinter as ctk
from tkinter import messagebox

total_tasks = 0
tasks_completed = 0
tasks_remaining = 0
tasks_completion_percentage = 0

class ItemCard(ctk.CTkFrame):
    def __init__(self, parent, app, time, task):
        super().__init__(parent, corner_radius=8)

        self.app = app      # 🔥 reference to main app
        self.name = task    # store task name

        # Grid setup
        self.grid_columnconfigure((0,1,2,3), weight=1)

        ctk.CTkLabel(self, text=time).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(self, text=task).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkCheckBox(self, text="", command=self.app.check_complete_task).grid(row=0, column=2, padx=10, pady=10)

        ctk.CTkButton(self, text="Remove", command=self.remove_item).grid(row=0, column=3, padx=10, pady=10)

    
    def remove_item(self):
        # Remove from main app data
        self.app.items = [item for item in self.app.items if item["task"] != self.name]

        # Remove UI card
        self.destroy()
        self.app.update_summry()


class DailyPlanner(ctk.CTk):
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
        # Main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, sticky='nsew')

        main_frame.grid_columnconfigure((0, 1, 2), weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=2)
        main_frame.grid_rowconfigure(3, weight=1)

        title = ctk.CTkLabel(main_frame,
                        text='Daily Planner',
                        font=ctk.CTkFont(size=30, weight="bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="ew")

        self.task_time = ctk.CTkEntry(main_frame,
                                 placeholder_text="Enter time",
                                 height=40,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        self.task_time.grid(row=1, column=0, padx=10, sticky="ew")

        self.task_name = ctk.CTkEntry(main_frame,
                                 placeholder_text="Enter task",
                                 height=40,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        self.task_name.grid(row=1, column=1, padx=10, sticky="ew")

        add_task_btn = ctk.CTkButton(main_frame,
                                     text="Add Task",
                                     height=40,
                                     command=self.add_to_list,
                                     font=ctk.CTkFont(size=15, weight="normal"))
        add_task_btn.grid(row=1, column=2, padx=10, sticky="ew")

        # Scrollable frame
        self.scroll = ctk.CTkScrollableFrame(main_frame, fg_color="#F2F2F2")
        self.scroll.grid(row=2, column=0, columnspan=3, padx=10, sticky="ew")
        self.scroll.grid_columnconfigure(0, weight=1)

        self.items = []

        # Tasks summry frame
        tasks_summry_frame = ctk.CTkFrame(main_frame)
        tasks_summry_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")

        tasks_summry_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        tasks_summry_frame.grid_rowconfigure((0, 1), weight=1)

        total_tasks = ctk.CTkLabel(tasks_summry_frame,
                                   text="Total Tasks:",
                                   font=ctk.CTkFont(size=15, weight="normal"))
        total_tasks.grid(row=0, column=0, sticky="w", padx=(10, 0))

        self.total_tasks_num = ctk.CTkLabel(tasks_summry_frame,
                                   text="0",
                                   fg_color="white",
                                   corner_radius=5,
                                   height=40,
                                   width=100,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        self.total_tasks_num.grid(row=0, column=1, sticky="w")

        tasks_completed = ctk.CTkLabel(tasks_summry_frame,
                                   text="Tasks Completed:",
                                   font=ctk.CTkFont(size=15, weight="normal"))
        tasks_completed.grid(row=0, column=3, sticky="w")

        self.tasks_completed_num = ctk.CTkLabel(tasks_summry_frame,
                                   text="0",
                                   fg_color="white",
                                   corner_radius=5,
                                   height=40,
                                   width=100,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        self.tasks_completed_num.grid(row=0, column=4, sticky="w")

        tasks_remaining = ctk.CTkLabel(tasks_summry_frame,
                                   text="Tasks Remaining:",
                                   font=ctk.CTkFont(size=15, weight="normal"))
        tasks_remaining.grid(row=1, column=0, sticky="w", padx=(10, 0))

        self.tasks_remaining_num = ctk.CTkLabel(tasks_summry_frame,
                                   text="0",
                                   fg_color="white",
                                   corner_radius=5,
                                   height=40,
                                   width=100,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        self.tasks_remaining_num.grid(row=1, column=1, sticky="w", padx=(0, 10))

        completion_rate = ctk.CTkLabel(tasks_summry_frame,
                                   text="Completion Rate:",
                                   font=ctk.CTkFont(size=15, weight="normal"))
        completion_rate.grid(row=1, column=3, sticky="w")

        self.completion_rate_num = ctk.CTkLabel(tasks_summry_frame,
                                   text=f"{tasks_completion_percentage}%",
                                   fg_color="white",
                                   corner_radius=5,
                                   height=40,
                                   width=100,
                                   font=ctk.CTkFont(size=15, weight="normal"))
        self.completion_rate_num.grid(row=1, column=4, sticky="w", padx=(0, 10))

    def is_inList(self, n):
        n = n.lower()

        for item in self.items:
            if item["task"].lower() == n:
                return True
        return False
    
    def update_summry(self):
        global total_tasks
        global tasks_remaining
        global tasks_completed
        global tasks_completion_percentage
        total_tasks = len(self.items)
        tasks_remaining = total_tasks - tasks_completed
        tasks_completion_percentage = (tasks_completed/total_tasks)*100

        self.total_tasks_num.configure(text=f"{total_tasks}")
        self.tasks_completed_num.configure(text=f"{tasks_completed}")
        self.tasks_remaining_num.configure(text=f"{tasks_remaining}")
        self.completion_rate_num.configure(text=f"{round(tasks_completion_percentage,2)}%")
        


    def check_complete_task(self):
        global tasks_completed
        tasks_completed += 1
        self.update_summry()

    def add_to_list(self):
        try:
            time = self.task_time.get()
            task = self.task_name.get()

            if len(time) == 0 and len(task) == 0:
                messagebox.showerror("Error", "Empty sting!!")
                return
            elif self.is_inList(task):
                messagebox.showerror("Error", "Duplicate Task")
                return
            else:
                self.items.append({
                    "time": time,
                    "task": task,
                })

                # add the card to the scrollable frame
                card = ItemCard(self.scroll, self, time, task)
                card.pack(fill="x", pady=5)
            self.update_summry()
            self.task_time.delete(0, "end")
            self.task_name.delete(0, "end")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")



if __name__ == "__main__":
    app = DailyPlanner()
    app.mainloop()
