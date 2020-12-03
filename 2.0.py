from pynput.keyboard import Key, Listener
import pyautogui

x1=0
y1=0
x2=0
y2=0

f = open("data.txt", "r")
data = f.read()

def on_release(key):
    global x1, x2, y1, y2
    global st
    global abp,abm,pos

    keypress = format(
        key)
    #print(keypress)
    #fragt bestimmten Druck ab
    if keypress == "'p'":
        currentMouseX, currentMouseY = pyautogui.position()
        x1=currentMouseX
        y1=currentMouseY
        print("wert eins")
        print(x1)
        print(y1)
    if keypress == "'o'":
        currentMouseX, currentMouseY = pyautogui.position()
        x2=currentMouseX
        y2=currentMouseY
        print("wert zwei")
        print(x2)
        print(y2)

    if keypress == "'i'":
        i=0
        xdiff=x1-x2
        ydiff=y1-y2
        if xdiff < 0:
            xdiff=xdiff*-1

        xdiffer= xdiff+ydiff*0.364
        print(xdiffer)
        print("Ergebniss")
        #print(xdiffer)
        abp=xdiff
        abm=xdiff
        #Flugbahn berechner
        while i <100:
            posp=data.find(str(abp))
            posm=data.find(str(abm))
            if posm > 0:
                pos=posm
                i=1000
            elif posp >0:
                pos=posp
                i=1000
            else:
                i=i+1
                abp=abp+1
                abm=abm+1
       
        starke= data[pos-5:pos-1]

        #print(pos)
        print("Winkel 70, Stärke")
        print(starke)

        


# Collect events until released
with Listener(
        on_release=on_release) as listener:
    listener.join()