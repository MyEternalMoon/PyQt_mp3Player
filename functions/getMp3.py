from eyed3 import mp3
import os
import pickle
from functions.MusicList import singleMusic


# class MyTimer():
#     def __init__(self,startV,parent):
#         self.timer = QtCore.QTimer()
#         self.n = startV*10//10
#         self.timer.timeout.connect(self.go)
#         self.timer.setInterval(250)
#         self.timer.start()
#
#     def go(self):
#         if self.n == 0:
#             pygame.mixer.music.pause()
#             self.timer.stop()
#         else:
#             self.n -= 0.1
#             pygame.mixer.music.set_volumn(self.n/10)

def getFormattedTime(s):
    return ("%02d:%02d"%(s//60,s%60))

def getMp3(more=[]):
    music = []
    disk = ["D:\\"]
    new = [""]
    while len(new) != 0:
        new = []
        for i in range(len(disk)):
            try:
                f = os.listdir(disk[i])
                for j in f:
                    if j.endswith(".mp3"):
                        music.append(disk[i]+"\\"+j)
                    elif os.path.isdir(disk[i]+"\\"+j):
                        new.append(disk[i]+"\\"+j)
            except PermissionError as e:
                print(e)
        disk = new
    return musicFilter(music)

def getMp3FromStore(path):
    music = []
    if os.path.isdir(path):
        List = os.listdir(path)
        for i in List:
            if i.endswith(".mp3"):
                music.append(path+'/'+i)
        music = musicFilter(music)
    return music

def saveMp3(path,music):
    if not len(music):
        return
    w = pickle.dumps(music)
    with open(path+"cache.dat","wb") as f:
        f.write(w)

def getMp3FromCache(path):
    with open(path+"cache.dat","rb") as f:
        a = f.read()
        if not len(a):
            music = []
        else:
            music = pickle.loads(a)
    return music

def musicFilter(music):
    ret = []
    for i in music:
        p = mp3.Mp3AudioFile(i)
        if p is not None:
            if p.info.time_secs >50:
                ret.append(singleMusic(p.info.time_secs,i,p.tag.title,p.tag.artist,p.tag.album))
    for i in ret:
        i.generalInfo()
    return ret

def deleteMusic(path):
    try:
        os.remove(path)
    except:
        print(path)
        print("Can't do that")
        return 0
    else:
        print("Done delete")
        return 1
