import os
import json


def initconfig(path = "config.txt"):
    if os.path.isfile(path):
        with open(path,"r") as f:
            k = f.read()
            if (len(k)) != 0:
                info = json.loads(k,encoding="utf-8")
    else:
        info = {}
        info["musicStorage"] = os.getcwd() + "\\music"
        info["userName"] = "Administrator"
        info["config"] = {0:
                              {0:
                                   ["默认音乐储存", "", "选择位置"],
                               1:
                                   ["默认头像储存", "", "选择位置"],
                               2:
                                   ["", "", ""]},
                          1:
                              {0:
                                   ["关闭后仍记录播放列表", "是", "更改"],
                               1:
                                   ["循环播放列表", "是", "更改"],
                               2:
                                   ["", "", ""]},
                          2:
                              {0:
                                   ["", "", ""],
                               1:
                                   ["", "", ""],
                               2:
                                   ["", "", ""]},
                          3:
                              {0:
                                   ["", "", ""],
                               1:
                                   ["", "", ""],
                               2:
                                   ["", "", ""]}
                          }
        with open(path, "w") as f:
            f.write(json.dumps(info))
    return info


def first_create_config(info):
    if len(info) != 4:
        return -1
    path = info[0]
    musicStorage = info[1]
    head = info[2]
    userName = info[3]
    ret = {}
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)
    print(os.getcwd())
    try:
        os.mkdir(path + "\\music")
        os.mkdir(path+"\\Head")
    except:
        pass
    ret["path"] = path
    ret["musicStorage"] = musicStorage
    ret["head"] = head
    ret["userName"] = userName
    with open("cond.txt", "w") as f:
        f.write(json.dumps(info))

    return ret



def saveConfig(infos):
    with open("config.txt","w") as f:
        f.write(json.dumps(infos))