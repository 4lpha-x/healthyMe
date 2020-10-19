from pygame import mixer
import time
import datetime

print("Love from Alpha! Specially made for our Harry bhai <3")

def playmusic(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def nowtime():
    return datetime.datetime.now()


i = 14  # how many times you've to drink water

watTime = time.time()
eyeTime = time.time()
exTime = time.time()

while True:
    if i > 0:
        if time.time()-watTime > 2040:
            while True:
                print("Drink 250 ml Water, NOWWWW!!!")
                playmusic("water.mp3")
                ask = input("Have you drink water?? (y for yes, n for no): ")
                if ask == "y":
                    with open("waterlog.txt", "a" ) as wl:
                        wl.write(str([str(nowtime())])+": Drank water\n")
                    i = i-1
                    mixer.music.fadeout(2)
                    print("Drank water!")
                    watTime = time.time()
                    break
                else:
                    continue
        elif time.time()-eyeTime > 1800:
            while True:
                print("Do eye exercise, NOWWWW!!!")
                playmusic("eye.mp3")
                ask = input("Have you done eye exercise?? (y for yes, n for no): ")
                if ask == "y":
                    with open("eyelog.txt", "a") as el:
                        el.write((str[str(nowtime())]) + ": Eye exercise done\n")
                    mixer.music.fadeout(2)
                    print("Eye exercise done!")
                    eyeTime = time.time()
                break
        elif time.time()-exTime > 2700:
            while True:
                print("Do exercise, NOWWWW!!!")
                playmusic("exercise.mp3")
                ask = input("Have you done exercise?? (y for yes, n for no): ")
                if ask == "y":
                    with open("exlog.txt", "a") as exl:
                        exl.write(str([str(nowtime())]) + ": Exercise done\n")
                    mixer.music.fadeout(2)
                    print("Exercise done!")
                    exTime = time.time()
                break

    else:
        print("Today's health job has finished!!!")
        break
