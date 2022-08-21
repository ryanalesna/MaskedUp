#main method
#this is where we will call all of our functions

#imports
import SpeechToTextRealTime as sttrt
import asyncio
import FaceGUI as GUI



#calling speech to text algorithm
futures = [sttrt.speech_to_text()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

GUI.main()




