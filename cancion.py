class Cancion:
    def __init__(self):
        self.artist_name = ""
        self.track_name = ""
        self.track_year = ""
        self.track_id = ""
        self.track_popularity = 0  
        self.track_duration_ms = 0  

    def set_artist_name(self, name):
        self.artist_name = name

    def set_track_name(self, name):
        self.track_name = name

    def set_track_id(self, id):
        self.track_id = id

    def set_year(self, year):
        self.track_year = year

    def set_popularity(self, popularity):
        self.track_popularity = popularity

    def set_duration_ms(self, duration):
        self.track_duration_ms = duration

    def get_artist_name(self):
        return self.artist_name

    def get_track_name(self):
        return self.track_name
    
    def get_track_id(self):
        return self.track_id
    
    def get_year(self):
        return self.track_year
    
    def get_popularity(self):
        return self.track_popularity

    def get_duration_ms(self):
        return self.track_duration_ms