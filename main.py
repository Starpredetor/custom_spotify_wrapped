import glob
import pandas as pd
import tkinter as tk
from tkinter import ttk
import os

#Data Parsing from the JSON files
class DataProcessor:
    def __init__(self, dir='./json_files/'):
        self.dir = dir
        self.data = self.load_data()

    def load_data(self):
        json_files = glob.glob(os.path.join(self.dir, '*.json'))
    
        if not json_files:
            raise ValueError(f"No JSON files found in directory: {self.dir} Please add your JSON files in that directory.")
    
        file_paths = glob.glob(f"{self.dir}/*.json")
        dataframes = [pd.read_json(file) for file in file_paths]
        data = pd.concat(dataframes, ignore_index=True)
        data['ts'] = pd.to_datetime(data['ts'], errors='coerce')
        data['year'] = data['ts'].dt.year
        data.rename(columns={
            'master_metadata_track_name': 'track',
            'master_metadata_album_artist_name': 'artist',
        }, inplace=True)

        data = data[data['year'] == 2024]
        data = data[data['skipped'] != True]  
        data = data[data['ms_played'] > 30000]
        return data

    def top_artists(self):
        return self.data['artist'].value_counts().head(5)

    def top_songs(self):
        return self.data['track'].value_counts().head(5)
    
    def total_time(self):
        return round(self.data['ms_played'].sum()/60000)


#GUI
class App(tk.Tk):
    def __init__(self, data_processor):
        super().__init__()
        self.title("Your Own Wrapped")
        self.geometry("800x600")
        self.configure(bg='#000000')  
        self.iconphoto(False, tk.PhotoImage(file='assets/black_icon.png'))  
        self.iconbitmap('assets/black_icon.ico')

        self.data_processor = data_processor

        self.total_minutes_frame = tk.Frame(self, bg='#000000')
        self.total_minutes_frame.pack(pady=10)
        total_minutes = self.data_processor.total_time()
        total_minutes_label = tk.Label(self.total_minutes_frame, text=f"Total Listening Time: {format(total_minutes, ',d')} minutes", bg='#000000', fg='white', font=('Helvetica', 14))
        total_minutes_label.pack()

        self.artists_frame = tk.Frame(self, bg='#000000')
        self.songs_frame = tk.Frame(self, bg='#000000')

        self.artists_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.songs_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.populate_artists()
        self.populate_songs()

    def populate_artists(self):
        artists = self.data_processor.top_artists()

        artist_label = tk.Label(self.artists_frame, text="Top Artists:", bg='#000000', fg='white', font=('Helvetica', 14))
        artist_label.pack(pady=10)

        for index, artist in enumerate(artists.index, start=1):
            artist_text = f"{index}. {artist} - {artists[artist]} plays"
            artist_entry = tk.Label(self.artists_frame, text=artist_text, bg='#000000', fg='white', font=('Helvetica', 12))
            artist_entry.pack(anchor='w', padx=20)

    def populate_songs(self):
        songs = self.data_processor.top_songs()

        song_label = tk.Label(self.songs_frame, text="Top Songs:", bg='#000000', fg='white', font=('Helvetica', 14))
        song_label.pack(pady=10)

        for index, song in enumerate(songs.index, start=1):
            song_text = f"{index}. {song} - {songs[song]} plays"
            song_entry = tk.Label(self.songs_frame, text=song_text, bg='#000000', fg='white', font=('Helvetica', 12))
            song_entry.pack(anchor='w', padx=20)


if __name__ == "__main__":
    data_processor = DataProcessor()
    app = App(data_processor)
    app.mainloop()