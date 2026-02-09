import customtkinter as ctk
from tkinter import messagebox

class TemperatureConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ---------------- App Setup ----------------
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("Temperature Converter")
        self.geometry("500x600")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ---------------- Main Card ----------------
        self.card = ctk.CTkFrame(self, corner_radius=20)
        self.card.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.card.grid_columnconfigure(0, weight=1)
        self.card.grid_columnconfigure(1, weight=1)

        self.type_of_convertion = ""
        self.converted_type = ""

        self._create_header()
        self._create_inputs()
        self._create_result()

    # ---------------- Header ----------------
    def _create_header(self):
        title = ctk.CTkLabel(
            self.card,
            text="Temperature Converter",
            font=("Segoe UI", 26, "bold")
        )
        title.grid(row=0, column=0, columnspan=2, pady=(25, 5))

        subtitle = ctk.CTkLabel(
            self.card,
            text="Convert between Celsius, Fahrenheit & Kelvin",
            font=("Segoe UI", 13),
            text_color="gray"
        )
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 25))

    # ---------------- Inputs ----------------
    def _create_inputs(self):
        # Input Value
        ctk.CTkLabel(self.card, text="Enter Temperature").grid(
            row=2, column=0, columnspan=2, sticky="w", padx=30
        )

        self.input_temp = ctk.CTkEntry(
            self.card,
            height=45,
            corner_radius=12
        )
        self.input_temp.grid(
            row=3, column=0, columnspan=2,
            padx=30, pady=(5, 20), sticky="ew"
        )

        # From Unit
        ctk.CTkLabel(self.card, text="From").grid(
            row=4, column=0, sticky="w", padx=(30, 10)
        )

        self.from_unit = ctk.CTkComboBox(
            self.card,
            values=["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"],
            height=40,
            command=self.covert_from,
            corner_radius=10
        )
        self.from_unit.set("from...")
        self.from_unit.grid(
            row=5, column=0, padx=(30, 10), pady=(5, 20), sticky="ew"
        )

        # To Unit
        ctk.CTkLabel(self.card, text="To").grid(
            row=4, column=1, sticky="w", padx=(10, 30)
        )

        self.to_unit = ctk.CTkComboBox(
            self.card,
            values=["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"],
            height=40,
            command=self.convert_to,
            corner_radius=10
        )
        self.to_unit.set("to....")
        self.to_unit.grid(
            row=5, column=1, padx=(10, 30), pady=(5, 20), sticky="ew"
        )

        # Convert Button
        self.convert_btn = ctk.CTkButton(
            self.card,
            text="CONVERT",
            height=50,
            command=self.calculate_result,
            font=("Segoe UI", 16, "bold"),
            corner_radius=14
        )
        self.convert_btn.grid(
            row=6, column=0, columnspan=2,
            padx=30, pady=(10, 25), sticky="ew"
        )

    # ---------------- Result ----------------
    def _create_result(self):
        result_frame = ctk.CTkFrame(self.card, corner_radius=14)
        result_frame.grid(
            row=7, column=0, columnspan=2,
            padx=30, pady=(0, 25), sticky="ew"
        )

        result_label = ctk.CTkLabel(
            result_frame,
            text="Result",
            font=("Segoe UI", 14),
            text_color="gray"
        )
        result_label.pack(pady=(15, 5))

        self.result_value = ctk.CTkLabel(
            result_frame,
            text="--",
            font=("Segoe UI", 28, "bold")
        )
        self.result_value.pack(pady=(0, 15))
    
    def covert_from(self, choice):
        self.type_of_convertion = choice
    def convert_to(self, choice):
        self.converted_type = choice
    def calculate_result(self):
        try:
            value = self.input_temp.get()
            if len(value) == 0:
                messagebox.showerror("Error", "Empty string error")
                return
            elif not value.isnumeric():
                messagebox.showerror("Error", "Only Numbers are allowed")
                return
            else:
                if self.type_of_convertion == "Celsius (°C)" and self.converted_type == "Fahrenheit (°F)":
                    result = float(value) * (9/5) + 32
                    self.result_value.configure(text=f"{round(result, 1)} °F")
                elif self.type_of_convertion == "Fahrenheit (°F)" and self.converted_type == "Celsius (°C)":
                    result = (float(value) - 32) * 5/9
                    self.result_value.configure(text=f"{round(result, 1)} °C")
                elif self.type_of_convertion == "Fahrenheit (°F)" and self.converted_type == "Kelvin (K)":
                    result = (float(value) - 32) / 1.8 + 273.15
                    self.result_value.configure(text=f"{round(result, 1)} K")
                elif self.type_of_convertion == "Celsius (°C)" and self.converted_type == "Kelvin (K)":
                    result = float(value) + 273.15
                    self.result_value.configure(text=f"{round(result, 1)} K")
                elif self.type_of_convertion == "Kelvin (K)" and self.converted_type == "Celsius (°C)":
                    result = float(value) - 273.15
                    self.result_value.configure(text=f"{round(result, 1)} °C")
                elif self.type_of_convertion == "Celsius (°C)" and self.converted_type == "":
                    result = (float(value) - 273.15) * 9/5 + 32.
                    self.result_value.configure(text=f"{round(result, 1)} °F")
                elif self.type_of_convertion == self.converted_type:
                    result = float(value)
                    self.result_value.configure(text=f"{round(result, 1)}")
                
                self.input_temp.delete(0, "end")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


# ---------------- Run App ----------------
if __name__ == "__main__":
    app = TemperatureConverterApp()
    app.mainloop()
