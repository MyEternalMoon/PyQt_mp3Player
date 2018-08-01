import os
import pickle
from functions import MusicList

def moveUp(store, cur):
    if cur == 0:
        pass
    else:
        tmp = store[cur-1]
        store[cur-1] = store[cur]
        store[cur] = tmp

def pureSave(store):
    byte_list = pickle.dumps(store)
    with open("MusicList.dat", "wb") as f:
        f.write(byte_list)
    print("Done save")

def saveList(lis,store):
    store.append(lis)
    byte_list = pickle.dumps(store)
    with open("MusicList.dat","wb") as f:
        f.write(byte_list)
    print("Done save")

def loadList():
    if os.path.isfile("MusicList.dat"):
        with open("MusicList.dat","rb") as f:
            return pickle.loads(f.read())
    else:
            return []

def dealCrush(store,path):
    for i in range(len(store)):
        for j in range(len(store[i].musicContent)):
            if store[i].musicContent[j].path == path:
                store[i].musicContent[j].isEnabled = False

def deleteList(index,store):
    del store[index]
    byte_list = pickle.dumps(store)
    with open("MusicList.dat","wb") as f:
        f.write(byte_list)
    print("Done delete")