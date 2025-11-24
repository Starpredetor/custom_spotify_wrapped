import customtkinter as ctk 


class FinalFrame(ctk.CTkFrame):

    def __init__(self, parent, data_processor, year):
        super().__init__(parent)
        self.data_processor = data_processor
        self.data_processor.year = year
        self.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

    def populate_artists(self):
        artists = self.data_processor.top_artists()

        artist_label = ctk.CTkLabel(self, text="Top Artists:", font=('Helvetica', 14))
        artist_label.pack(pady=10)

        for index, artist in enumerate(artists.index, start=1):
            artist_text = f"{index}. {artist} - {artists[artist]} plays"
            artist_entry = ctk.CTkLabel(self, text=artist_text, font=('Helvetica', 12))
            artist_entry.pack(anchor='w', padx=20)

    def populate_songs(self):
        songs = self.data_processor.top_songs()

        song_label = ctk.CTkLabel(self, text="Top Songs:", font=('Helvetica', 14))
        song_label.pack(pady=10)

        for index, song in enumerate(songs.index, start=1):
            song_text = f"{index}. {song} - {songs[song]} plays"
            song_entry = ctk.CTkLabel(self, text=song_text, font=('Helvetica', 12))
            song_entry.pack(anchor='w', padx=20)
