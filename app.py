import customtkinter as ctk

# UI Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NeumorphicCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Python Calculator")
        self.geometry("460x575")
        self.configure(fg_color="#1a1a2e")

        # String variable to store the calculation
        self.result_var = ctk.StringVar(value="0")

        # --- DISPLAY ---
        self.screen = ctk.CTkLabel(
            self, 
            textvariable=self.result_var,
            font=("Roboto", 48),
            anchor="e",
            fg_color="#252525",
            height=100,
            corner_radius=15
        )
        self.screen.pack(padx=20, pady=(30, 20), fill="x")

        # --- BUTTON CONTAINER ---
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        buttons = [
            ('Cl', 0, 0, '#ff4d4d'), ('Del', 0, 1, '#ff4d4d'), ('%', 0, 2, '#4ade80'), ('/', 0, 3, '#4ade80'),
            ('7', 1, 0, None),      ('8', 1, 1, None),      ('9', 1, 2, None),      ('*', 1, 3, '#4ade80'),
            ('4', 2, 0, None),      ('5', 2, 1, None),      ('6', 2, 2, None),      ('-', 2, 3, '#4ade80'),
            ('1', 3, 0, None),      ('2', 3, 1, None),      ('3', 3, 2, None),      ('+', 3, 3, '#4ade80'),
            ('e^', 4, 0, '#4ade80'),('0', 4, 1, None),      ('.', 4, 2, None),      ('=', 4, 3, '#ff9f1c')
        ]

        for (text, r, c, color) in buttons:
            self.create_button(text, r, c, color)

    def create_button(self, text, row, col, text_color):
        # Default button style
        btn_color = "#2d2d2d" 
        t_color = text_color if text_color else "white"
        hover = "#3d3d3d"

        # Special case for Equals button background
        if text == "=":
            btn_color = "#ff9f1c"
            t_color = "white"
            hover = "#e68a00"

        button = ctk.CTkButton(
            self.button_frame,
            text=text,
            width=65,
            height=65,
            corner_radius=32, # Circular look
            fg_color=btn_color,
            text_color=t_color,
            hover_color=hover,
            font=("Roboto", 20, "bold"),
            command=lambda x=text: self.on_click(x)
        )
        button.grid(row=row, column=col, padx=8, pady=8)

    def on_click(self, char):
        current = self.result_var.get()

        if char == "Cl":
            self.result_var.set("0")
        elif char == "Del":
            if len(current) > 1:
                self.result_var.set(current[:-1])
            else:
                self.result_var.set("0")
        elif char == "=":
            try:
                # Basic math evaluation
                # Note: replace 'e^' and '%' with proper python logic if needed
                res = str(eval(current.replace('x', '*').replace('%', '/100')))
                self.result_var.set(res)
            except:
                self.result_var.set("Error")
        elif char == "e^":
            # Just a placeholder for the UI look
            self.result_var.set(current + "**")
        else:
            if current == "0":
                self.result_var.set(char)
            else:
                self.result_var.set(current + char)

if __name__ == "__main__":
    app = NeumorphicCalculator()
    app.mainloop()