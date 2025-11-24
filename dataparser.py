import os
import glob
import pandas as pd

class DataProcessor:
    def __init__(self, dir='./json_files/', year=2024):
        self.dir = dir
        self.data = self.load_data()
        self.year = year

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

        data = data[data['year'] == self.year]
        data = data[data['skipped'] != True]  
        data = data[data['ms_played'] > 30000]
        return data

    def top_artists(self):
        return self.data['artist'].value_counts().head(5)

    def top_songs(self):
        return self.data['track'].value_counts().head(5)
    
    def total_time(self):
        return round(self.data['ms_played'].sum()/60000)