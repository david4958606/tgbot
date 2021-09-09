import time, os, urllib, shutil

head = "https://sayuri.fumiama.top/dice?class=9&url="
datapath = ""
cachefile = ""
lastvisit = int(time.time())
comments = ["[0]这啥啊",
		"[1]普通欸",
		"[2]有点可爱",
		"[3]不错哦",
		"[4]很棒",
		"[5]我好啦!",
		"[6]影响不好啦!",
		"[7]太涩啦，🐛了!",
		"[8]已经🐛不动啦..."]

def create_datapath():
    folder = os.path.exists(datapath)
    if not folder:
        os.makedirs(datapath)
    else:
        shutil.rmtree(datapath)
        os.makedirs(datapath)
    global cachefile
    cachefile = datapath + "\cache"
    # print(cachefile)

def flush_time():
    lastvisit

