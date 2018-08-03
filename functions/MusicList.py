class singleMusic:

    def __init__(self, length, absPath="", name="Unknown", artist="Unknown", album="Unknown"):
        self.length = length
        self.path = absPath
        if name is None:
            self.name = "Unknown"
        else:
            self.name = name
        if artist is None:
            self.artist = "Unknown"
        else:
            self.artist = artist
        if album is None:
            self.album = "Unknown"
        else:
            self.album = album
        self.played = 0
        self.isEnabled = True

    def play(self):
        self.played += 1

    def generalInfo(self):
        print("<%s> by %s in %s from %s"%(self.name,self.artist,self.album,self.path))


class musicList:

    """To save the user's favorite songs"""

    def __init__(self, name, user, description="", pic=None):
        self.name = name
        self.user = user
        self.picPath = pic
        self.description = description
        self.musicContent = []
        self.times = 0

    def ChangeName(self,new):
        self.name = new

    def ChangePic(self,new):
        self.picPath = new

    def ChangeDescription(self, new):
        self.description = new

    def AddNewMusic(self, new):
        self.musicContent.append(new)

    def DeleteMusic(self, index):
        del self.musicContent[index]
