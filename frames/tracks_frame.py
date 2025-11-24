import customtkinter as ctk 


class TrackFrame(ctk.CTkFrame):

    def __init__(self, parent, data_processor, year):
        super().__init__(parent)
        self.data_processor = data_processor
        self.data_processor.year = year
        self.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

  
