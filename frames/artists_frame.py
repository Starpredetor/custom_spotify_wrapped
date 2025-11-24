import customtkinter as ctk
from PIL import Image 


class ArtistsFrame(ctk.CTkFrame):
    def __init__(self, parent, data_processor,year):
        super().__init__(parent)
        self.data_processor = data_processor
        data_processor.year = year
        self.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)
    

    def populate_artists(self):
        artists = self.data_processor.top_artists(self.year)

        artist_label = ctk.CTkLabel(self, text="Top Artists:", font=('Helvetica', 14))
        artist_label.pack(pady=10)

        for index, artist in enumerate(artists.index, start=1):
            artist_text = f"{index}. {artist}"
            artist_entry = ctk.CTkLabel(self, text=artist_text, font=('Helvetica', 12))
            artist_entry.pack(anchor='w', padx=20)