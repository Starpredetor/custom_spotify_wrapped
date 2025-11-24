import customtkinter as ctk
from artists_frame import ArtistsFrame

class InitialFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        welcome_label = ctk.CTkLabel(self, text="Welcome to Your Own Wrapped!", font=('Helvetica', 20))
        welcome_label.pack(pady=10, padx=10)

        instructions_label = ctk.CTkLabel(self, text="Please select a year to view your listening data:", font=('Helvetica', 14))
        instructions_label.pack(pady=10)

        intvar = ctk.CTkIntVar()
        year_cbox = ctk.CTkComboBox(self, text="2020", values=[2021, 2022, 2023, 2024], variable=intvar)
        
    
        
        
    
