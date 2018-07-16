import eyed3
import os
from functions.MusicList import singleMusic
import time

def getMp3(more=[]):
    # a = time.clock()
    music = []
    if hasattr(more,"__init__") == False:
        more = []
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
    return music

def musicFilter(music):
    ret = []
    for i in music:
        p = eyed3.load(i)
        if p is not None:
            if p.info.time_secs >50:
                ret.append(singleMusic(p.info.time_secs,i,p.tag.title,p.tag.artist,p.tag.album))
    for i in ret:
        i.generalInfo()
    return ret

#q = getMp3()
#for i in q:
   # print(i)
#musicFilter(q)
    # print(disk)
    # b =time.clock()
    # print(b-a)
    # for i in music:
    #     print(i)
