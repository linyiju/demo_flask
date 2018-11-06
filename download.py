import os
import webbrowser
from gtts import gTTS

def check_and_create(folder_name):
    check_dir = folder_name

    if os.path.exists(check_dir):  # Checks if the dir exists
        print("The directory exists")
    else:
        print("No directory found for " + check_dir)  # Output if no directory
        print()
        os.makedirs(check_dir)  # Creates a new dir for the given name
        print("Directory created for " + check_dir)



def sound(speak): #轉變成語音檔
    tts=gTTS(text=speak,lang="zh")
    tts.save("{}/Fart.mp3".format("gossip")) #指定目錄(gossip)找"放屁.mp3"
    # webbrowser.open("news.mp3")