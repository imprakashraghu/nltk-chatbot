import json 
import numpy as np

title_bag = []
tip_bag = []
tip_content = []
tip_link = []

# formatting the tip with a rectangular frame
def frame_printer(*words):
    size = max(len(word) for word in words)
    print('*' * (size + 4))
    for word in words:
        print('* {:<{}} *'.format(word.center(size," "), size))
    print('*' * (size + 4))

# show the tip
def show_tip():
    with open("dataset/tips.json", "rb") as file:
        jsdata = json.load(file)

    for j in jsdata["tips"]:
        title_bag.append(j["title"])
        tip_bag.append(j["tip"])
        tip_content.append(j["content"])
        tip_link.append(j["redirect"])

    tip_num_x = np.random.randint(0,len(title_bag))
    tip_num_y = np.random.randint(0,len(tip_bag))        
    # tip_num_w = np.random.randint(0,len(tip_link))  
    # frame_printer(title_bag[tip_num_x],tip_bag[tip_num_y])
    
    # get me some random stuff from tips
    return {"title":title_bag[tip_num_x],"tip":tip_bag[tip_num_y],"default":"Start talking with your bot (type quit to exit)","content":tip_content[tip_num_y],"redirect":tip_link[tip_num_y]}
