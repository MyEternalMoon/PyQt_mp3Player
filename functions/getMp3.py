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


def moveToStorage(paths, dire):
    print("later...")
    pass

def getFormattedTime(s):
    return ("%02d:%02d"%(s//60,s%60))

def getMp3(disk):
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
    with open(path+"/cache.dat","wb") as f:
        f.write(w)

def savePlayList(path, music):
    with open(path + "/listcache.dat","wb") as f:
        if not len(music):
            return
        w = pickle.dumps(music)
        f.write(w)

def getMp3ToPlayList(path):
    if os.path.isfile(path+"/listcache.dat"):
        with open(path + "/listcache.dat","rb") as f:
            a = f.read()
            if not a:
                music = []
            else:
                music = pickle.loads(a)
    else:
        music = []
    return music

def getMp3FromCache(path):
    if os.path.isfile(path+"/cache.dat"):
        with open(path+"/cache.dat","rb") as f:
            a = f.read()
            if not len(a):
                music = []
            else:
                music = pickle.loads(a)
    else:
        music = []
    return music

def musicFilter(music):
    ret = []
    names = []
    for i in music:
        p = mp3.Mp3AudioFile(i)
        if p is not None:
            try:
                if p.info.time_secs > 50:
                    if p.tag.title not in names or p.tag.title is None:
                        names.append(p.tag.title if p.tag.title is not None else None)
                        ret.append(singleMusic(p.info.time_secs, i,p.tag.title,p.tag.artist,p.tag.album))
            except AttributeError or TypeError:
                continue
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
