class Cancion:
    def __init__(self, id=None, artist_name=None, track_year="" ,track_name=None, track_id = "", track_popularity=0 , track_duration_ms=0):
        self.id = id
        self.artist_name = artist_name
        self.track_name = track_name
        self.track_year = track_year 
        self.track_id = track_id
        self.track_popularity = track_popularity  
        self.track_duration_ms = track_duration_ms  

    # Métodos set
    def set_id(self, id):
        self.id = id

    def set_artist_name(self, artist_name):
        self.artist_name = artist_name

    def set_track_year(self, track_year):
        self.track_year = track_year

    def set_track_name(self, track_name):
        self.track_name = track_name

    def set_track_id(self, track_id):
        self.track_id = track_id

    def set_track_popularity(self, track_popularity):
        self.track_popularity = track_popularity

    def set_track_duration_ms(self, track_duration_ms):
        self.track_duration_ms = track_duration_ms

    # Métodos get
    def get_id(self):
        return self.id

    def get_artist_name(self):
        return self.artist_name

    def get_track_name(self):
        return self.track_name
    
    def get_track_year(self):
        return self.track_year
    
    def get_track_id(self):
        return self.track_id
    
    def get_track_popularity(self):
        return self.track_popularity
    
    def get_track_duration_ms(self):
        return self.track_duration_ms

    # Método especial para representación en cadena
    def __str__(self):
        return f"Cancion{{artistName='{self.get_artist_name()}', trackName='{self.get_track_name()}'}}" 