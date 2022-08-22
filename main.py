#main method
#this is where we will call all of our functions

#imports
import SpeechToTextRealTime as sttrt
import asyncio
import GameLoop


#calling speech to text algorithm

loop = asyncio.get_event_loop()

GameLoop.app = GameLoop.App(loop)
loop.run_forever()
loop.close()



