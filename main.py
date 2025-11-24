import tkinter as ctk
from tkinter import ttk
import customtkinter as ctk
from dataparser import DataProcessor
from PIL import Image

ctk.set_appearance_mode("System")

ctk.set_default_color_theme('green')

#GUI
class App(ctk.CTk):
    def __init__(self, data_processor):
        super().__init__()
        self.title("Your Own Wrapped")
        self.geometry("800x600")
        self.configure(bg='#000000')  
        self.iconbitmap('assets/black_icon.ico')

        self.data_processor = data_processor

        self.total_minutes_frame = ctk.CTkFrame(self)
        self.total_minutes_frame.pack(pady=10)
        total_minutes = self.data_processor.total_time()
        total_minutes_label = ctk.CTkLabel(self.total_minutes_frame, text=f"Total Listening Time: {format(total_minutes, ',d')} minutes", font=('Helvetica', 14))
        total_minutes_label.pack()

        self.artists_frame = ctk.CTkFrame(self)
        self.songs_frame = ctk.CTkFrame(self)

        self.artists_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)
        self.songs_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        self.populate_artists()
        self.populate_songs()

    def populate_artists(self):
        artists = self.data_processor.top_artists()

        artist_label = ctk.CTkLabel(self.artists_frame, text="Top Artists:", font=('Helvetica', 14))
        artist_label.pack(pady=10)

        for index, artist in enumerate(artists.index, start=1):
            artist_text = f"{index}. {artist} - {artists[artist]} plays"
            artist_entry = ctk.CTkLabel(self.artists_frame, text=artist_text, font=('Helvetica', 12))
            artist_entry.pack(anchor='w', padx=20)

    def populate_songs(self):
        songs = self.data_processor.top_songs()

        song_label = ctk.CTkLabel(self.songs_frame, text="Top Songs:", font=('Helvetica', 14))
        song_label.pack(pady=10)

        for index, song in enumerate(songs.index, start=1):
            song_text = f"{index}. {song} - {songs[song]} plays"
            song_entry = ctk.CTkLabel(self.songs_frame, text=song_text, font=('Helvetica', 12))
            song_entry.pack(anchor='w', padx=20)


if __name__ == "__main__":
    data_processor = DataProcessor()
    app = App(data_processor)
    app.mainloop()