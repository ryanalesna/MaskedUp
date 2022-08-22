#main method
#this is where we will call all of our functions

#imports
import SpeechToTextRealTime as sttrt
import asyncio
import FaceGUI as GUI
from tkinter import *


class GameLoop:
    def __init__(self):
        self.win = Tk()
        self.canvas = Canvas(self.win, width=800, height=800)
        smiley = GUI.SmileyFace(self.canvas)

    def main(self):
        self.canvas.pack()
        # Button(win, text='Smile', command=smiley.smile).pack()
        # Button(win, text='Closed', command=smiley.closed).pack()
        # Button(win, text='Open', command=smiley.open).pack()
        # Button(win, text='Quit', command=win.destroy).pack()

        self.win.mainloop()


#calling speech to text algorithm
futures = [sttrt.speech_to_text()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

gameLoop = GameLoop()
gameLoop.main()





