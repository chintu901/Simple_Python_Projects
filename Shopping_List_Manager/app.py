import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

class ItemCard(ctk.CTkFrame):
    def __init__(self, parent, app, name, qty, price):
        super().__init__(parent, corner_radius=8)

        self.app = app      # 🔥 reference to main app
        self.name = name    # store item name

        # Grid setup
        self.grid_columnconfigure((0,1,2,3), weight=1)

        ctk.CTkLabel(self, text=name).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(self, text=qty).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkLabel(self, text=f"₹{price}").grid(row=0, column=2, padx=10, pady=10)

        ctk.CTkButton(self, text="Remove", command=self.remove_item).grid(row=0, column=3, padx=10, pady=10)

    
    def remove_item(self):
        # Remove from main app data
        self.app.items = [item for item in self.app.items if item["name"] != self.name]

        # Remove UI card
        self.destroy()



class ShoppingListManager(ctk.CTk):
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
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame.grid_columnconfigure((0, 1), weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        # Load image
        self.logo = ctk.CTkImage(Image.open("Shopping.png"), size=(250, 550))

         # Left column image
        img_label = ctk.CTkLabel(self.main_frame, image=self.logo)
        img_label.grid(row=0, column=0, sticky="w")

        # Right column frame
        right_input_frame = ctk.CTkFrame(self.main_frame, corner_radius=0, fg_color="#dbd9d9")
        right_input_frame.grid(row=0, padx=0, column=1, sticky="nsew")
        right_input_frame.grid_columnconfigure(0, weight=1)
        right_input_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Title of the project
        title_label = ctk.CTkLabel(
            right_input_frame,
            text="Shopping List Manager",
            font=ctk.CTkFont(size=34, weight="bold")
        )
        title_label.grid(row=0, column=0, pady=20, sticky="new")

        # Input frame
        input_frame = ctk.CTkFrame(right_input_frame, corner_radius=0)
        input_frame.grid(row=1, column=0, padx=5, sticky="new")
        input_frame.grid_columnconfigure((0, 1, 2), weight=1)
        input_frame.grid_rowconfigure((0, 1), weight=1)

        # Input form
        self.item_name = ctk.CTkEntry(input_frame,
                                 placeholder_text="Item name..",
                                 width=130,
                                 height=40,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        self.item_name.grid(row=0, column=0, pady=(10, 0), sticky="w")

        self.item_quantity = ctk.CTkEntry(input_frame,
                                 placeholder_text="Item quantity..",
                                 width=130,
                                 height=40,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        self.item_quantity.grid(row=0, column=1, padx=5, pady=(10, 0), sticky="w")

        self.item_price = ctk.CTkEntry(input_frame,
                                 placeholder_text="Item price..",
                                 width=130,
                                 height=40,
                                 font=ctk.CTkFont(size=15, weight="normal"))
        self.item_price.grid(row=0, column=2, pady=(10, 0), sticky="w")

        submit_button = ctk.CTkButton(input_frame,
                                      text="Add to list",
                                      width=405,
                                      height=40,
                                      command=self.add_to_list,
                                      font=ctk.CTkFont(size=20, weight="bold"))
        submit_button.grid(row=1, column=0, columnspan=3, pady=10)

        # Scrollable frame
        self.scroll = ctk.CTkScrollableFrame(right_input_frame, fg_color="#F2F2F2")
        self.scroll.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.scroll.grid_columnconfigure(0, weight=1)

        self.items = []

    def is_inList(self, n):
        n = n.lower()

        for item in self.items:
            if item["name"].lower() == n:
                return True
        return False


    def add_to_list(self):
        try:
            name = self.item_name.get().strip()
            quantity = int(self.item_quantity.get())
            price = float(self.item_price.get())

            # Check duplicate
            if self.is_inList(name):
                messagebox.showerror("Error", "Item already exists")
                return
        
            # Validate numbers
            if quantity <= 0 or price <= 0:
                messagebox.showerror("Error", "Please enter positive numbers")
                return

            # Save item
            self.items.append({
                "name": name,
                "qty": quantity,
                "price": price
            })

            # Create UI card
            card = ItemCard(self.scroll, self, name, quantity, price)
            card.pack(fill="x", pady=5)

            self.item_name.delete(0, "end")
            self.item_quantity.delete(0, "end")
            self.item_price.delete(0, "end")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        


if __name__ == "__main__":
    app = ShoppingListManager()
    app.mainloop()