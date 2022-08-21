from tkinter import *

class SmileyFace:
    def __init__(self, canvas):
        self.canvas = canvas

        canvas.create_oval(70, 70, 350, 350, fill='yellow')
        canvas.create_oval(125, 125, 175, 175, fill='black', tags='left')
        canvas.create_oval(225, 125, 275, 175, fill='black', tags='right')
        canvas.create_line(125, 250, 275, 250, width=5, tags='mouth')

    def smile(self):
        self.canvas.delete('right||mouth')
        self.canvas.create_oval(225, 125, 275, 175, fill='black', tags='right')
        self.canvas.create_arc(125, 175, 275, 300, extent=-180, width=5, style="arc", tags='mouth')

    def closed(self):
        self.canvas.delete('right||mouth')
        self.canvas.create_oval(225, 125, 275, 175, fill='black', tags='right')
        self.canvas.create_line(125, 275, 275, 275, width=5, tags='mouth')

    def open(self):
        self.canvas.delete('right||mouth')
        self.canvas.create_oval(225, 125, 275, 175, fill='black', tags='right')
        self.canvas.create_oval(130, 250, 280, 300, fill="black", tags = 'mouth')

    def moveLips(data):
        wordList = list(data)
        #checks last word of the list
        currWord = wordList.index(len(wordList))
        #loop through characters of each word
        for element in currWord:
            if data == 'm' or data == 'b' or data == 'p' or data == ' ':
                closed
                aysncio.sleep(0.2)
            else:
                open
def main():
    win = Tk()
    canvas = Canvas(win, width=800, height=800)
    canvas.pack()

    smiley = SmileyFace(canvas)

    #Button(win, text='Smile', command=smiley.smile).pack()
    #Button(win, text='Closed', command=smiley.closed).pack()
    #Button(win, text='Open', command=smiley.open).pack()
    #Button(win, text='Quit', command=win.destroy).pack()
    while(True):
        smiley.moveLips(data)

    win.mainloop()


    #closed/open mouth
    #if spaces, p,b,m. maybe f and v