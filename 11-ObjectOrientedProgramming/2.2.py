

class Song:
   def __init__(self, performer, title, album, year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year

      
      
      
   def __str__(self):
      return f"Performer: {self.performer}\n Title:{self.title}\n Album: {self.album}\n Year: {self.year}"

song1 = Song("Ed Sheeran", "XYZ" , "ZYX" , 2222)




## object usage
print(song1)
