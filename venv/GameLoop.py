#this file will create the GUI, pack it, update the GUI when needed, and close it when the X button is clicked

import tkinter as tk
import FaceGUI as GUI
import asyncio
import SpeechToTextRealTime as sttrt
class App(tk.Tk):
    def __init__(self, loop):
        super().__init__()
        self.loop = loop
        self.protocol("WM_DELETE_WINDOW",self.close)
        #self.futures = [self.updater(), sttrt.speech_to_text()]
        self.tasks = []
        self.tasks.append(loop.create_task(self.updater()))
        #this runs multiple times, which closes the connection to the API
        #self.tasks.append(loop.create_task(sttrt.send_data()))
        #self.tasks.append(loop.create_task(sttrt.receive_data()))
        self.tasks.append(loop.create_task(sttrt.speech_to_text()))

        self.canvas = tk.Canvas(self, width=800, height=800)
        self.canvas.pack()
        self.smiley = GUI.SmileyFace(self.canvas)

        #self.win = Tk()
        #self.canvas = Canvas(self.win, width=800, height=800)
        #self.canvas.pack()
        #self.smiley = GUI.SmileyFace(self.canvas)
        #futures = [sttrt.speech_to_text()]
        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(asyncio.wait(futures))

    async def updater(self):
        self.tk.willdispatch()
        while True:
            self.update_idletasks()
            self.update()
            await asyncio.sleep(0)

    def close(self):
        for task in self.tasks:
            task.cancel()
        self.loop.stop()
        self.destroy()

app = None


