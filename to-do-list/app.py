import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class TodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern To-Do List")
        self.geometry("500x600")
        self.resizable(False, False)

        self.tasks = []

        # Layout config
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # -------------------------
        # Title
        # -------------------------
        title = ctk.CTkLabel(
            self,
            text="📝 My To-Do List",
            font=("Segoe UI", 28, "bold")
        )
        title.grid(row=0, column=0, pady=20)

        # -------------------------
        # Task Input Section
        # -------------------------
        input_frame = ctk.CTkFrame(self, corner_radius=15)
        input_frame.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        input_frame.grid_columnconfigure(0, weight=1)

        self.task_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter a new task...",
            height=40,
            font=("Segoe UI", 14)
        )
        self.task_entry.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")

        add_button = ctk.CTkButton(
            input_frame,
            text="Add",
            width=80,
            height=40,
            command=self.add_task
        )
        add_button.grid(row=0, column=1, padx=(5, 10), pady=10)

        # -------------------------
        # Scrollable Task List
        # -------------------------
        self.task_frame = ctk.CTkScrollableFrame(self, corner_radius=15)
        self.task_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

    # -------------------------
    # Add Task
    # -------------------------
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text == "":
            return

        task_item = TaskItem(self.task_frame, task_text, self)
        task_item.pack(fill="x", padx=5, pady=5)

        self.tasks.append(task_item)
        self.task_entry.delete(0, "end")

    # -------------------------
    # Remove Task
    # -------------------------
    def remove_task(self, task):
        task.destroy()
        self.tasks.remove(task)


class TaskItem(ctk.CTkFrame):
    def __init__(self, parent, text, controller):
        super().__init__(parent, corner_radius=12)
        self.controller = controller
        self.completed = False

        self.grid_columnconfigure(1, weight=1)

        # Checkbox Button
        self.check_button = ctk.CTkButton(
            self,
            text="☐",
            fg_color="transparent",
            hover_color="#3c3c3c",
            width=40,
            command=self.toggle_complete
        )
        self.check_button.grid(row=0, column=1, padx=10, pady=(15,10), sticky="e")

        # Task Label
        self.label = ctk.CTkLabel(
            self,
            text=text,
            font=("Segoe UI", 14),
            anchor="w"
        )
        self.label.grid(row=0, column=0, sticky="w")

        # Delete Button
        delete_button = ctk.CTkButton(
            self,
            text="✕",
            width=40,
            fg_color="transparent",
            hover_color="#662121",
            command=lambda: controller.remove_task(self)
        )
        delete_button.grid(row=0, column=2, padx=10, pady=(15,10))

    # -------------------------
    # Toggle Complete
    # -------------------------
    def toggle_complete(self):
        self.completed = not self.completed

        if self.completed:
            self.check_button.configure(text="☑")
            self.label.configure(
                text_color="gray",
                font=("Segoe UI", 14, "overstrike")
            )
        else:
            self.check_button.configure(text="☐")
            self.label.configure(
                text_color="white",
                font=("Segoe UI", 14)
            )


if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
