import customtkinter as ctk
from PIL import *
from tkinter import messagebox
import math

class PrimeNumberFinder(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Prime Number Finder")
        self.geometry("700x550")
        
        # Set theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        
        # Create main container
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = ctk.CTkLabel(
            self,
            text="Prime Number Finder",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Input form
        input_frame = ctk.CTkFrame(self, fg_color="#acacac")
        input_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        input_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        input_frame.grid_rowconfigure((0,1), weight=1)

        # Form Input
        from_label = ctk.CTkLabel(input_frame, text="From:", font=ctk.CTkFont(size=14))
        from_label.grid(row=0, column=0, padx=(0, 10), pady=(20 ,5), sticky="e")

        self.from_entry = ctk.CTkEntry(input_frame,
                                       placeholder_text="Enter Starting Number",
                                       width=200,
                                       height=40,
                                       font=ctk.CTkFont(size=14))
        self.from_entry.grid(row=0, column=1, padx=(0,10), pady=(20, 5), sticky="w")

        # To Input
        from_label2 = ctk.CTkLabel(input_frame, text="To:", font=ctk.CTkFont(size=14))
        from_label2.grid(row=0, column=2, padx=(0, 10), pady=(20, 5), sticky="e")

        self.to_entry = ctk.CTkEntry(input_frame,
                                       placeholder_text="Enter Ending Number",
                                       width=200,
                                       height=40,
                                       font=ctk.CTkFont(size=14))
        self.to_entry.grid(row=0, column=3, padx=(0,10), pady=(20, 5), sticky="w")

        # Find Button
        find_button = ctk.CTkButton(input_frame,
                                    text="Find Prime Numbers",
                                    width=200,
                                    height=40,
                                    command=self.find_prime,
                                    font=ctk.CTkFont(size=14, weight="bold"),
                                    fg_color="#2563eb",
                                    hover_color="#1d4ed8")
        find_button.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=30, pady=(20, 20))

         # Results Label
        results_label = ctk.CTkLabel(
            self,
            text="Prime Numbers:",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        results_label.grid(row=2, column=0, padx=20, pady=(10, 5), sticky="nw")

        # Output frame
        output_frame = ctk.CTkFrame(self, fg_color="#acacac")
        output_frame.grid(row=3, column=0, padx=20, pady=10, sticky="new")
        output_frame.grid_columnconfigure((0), weight=1)
        output_frame.grid_rowconfigure((0,1), weight=1)

        self.prime_numbers = ctk.CTkLabel(output_frame,
                                     text="Waiting for your input...",
                                     width=500,
                                     height=40,
                                     corner_radius=5,
                                     fg_color="#acacac")
        self.prime_numbers.grid(row=3, column=0, padx=20, pady=10, sticky="nwe")
    
    def is_prime(self, n):
        """Check if a number is prime"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Check odd divisors up to sqrt(n)
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    def find_prime(self):
        """Find and display prime numbers in the given range"""
        try:
            # Get input values
            from_num = int(self.from_entry.get())
            to_num = int(self.to_entry.get())

            # Validate input
            if from_num > to_num:
                messagebox.showerror("Error", "Starting number must be less than or equal to ending number")
                return
            
            if from_num < 0 or to_num < 0:
                messagebox.showerror("Error", "Please enter positive numbers")
                return
            # Find prime numbers
            primes = [num for num in range(from_num, to_num + 1) if self.is_prime(num)]

            # Display prime numbers
            self.prime_numbers.configure(text=f"{primes}",
                                         fg_color="#ffffff")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = PrimeNumberFinder()
    app.mainloop()