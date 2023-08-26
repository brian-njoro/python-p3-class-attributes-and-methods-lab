class Song:

    #class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_genres()
        Song.add_song_to_count()
        Song.add_to_artist()
        Song.add_to_genre_count()



    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
        
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artist(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    #uncertain
    @classmethod
    def add_to_genre_count(cls):
        if cls.genre_count.get(cls.genre):
            cls.genre_count[cls.genre] += 1
        else:
            cls.genre_count[cls.genre] = 1

    