#this should convert speech to text in real time
#install pyaudio, websockets, and brew install portaudio on mac
#based on code from https://towardsdatascience.com/real-time-speech-recognition-python-assemblyai-13d35eeed226
import json

import base64
import asyncio
import pyaudio
import websockets
import FaceGUI
import GameLoop

SAMPLE_RATE = 16000
FRAMES_PER_BUFFER = 3200
API_KEY = '230b201ea1674d49b8c0c41a70eece8a'
ASSEMBLYAI_ENDPOINT = f'wss://api.assemblyai.com/v2/realtime/ws?sample_rate={SAMPLE_RATE}'

p = pyaudio.PyAudio()
audio_stream = p.open(
    frames_per_buffer=FRAMES_PER_BUFFER,
    rate=SAMPLE_RATE,
    format=pyaudio.paInt16,
    channels=1,
    input=True,
)


async def speech_to_text():
    while True:
        print("has done speech to text")
        data_sent, data_received = await asyncio.gather(send_data(), receive_data())

        await asyncio.sleep(0)

async def send_data():
    """
    Asynchronous function used for sending data
    """
    async with websockets.connect(
            ASSEMBLYAI_ENDPOINT,
            ping_interval=5,
            ping_timeout=40,
            extra_headers=(('Authorization', API_KEY),),
    ) as ws_connection:
        await asyncio.sleep(0.1)
        await ws_connection.recv()
        print('Websocket connection initialised')

        try:
            data = audio_stream.read(FRAMES_PER_BUFFER)
            data = base64.b64encode(data).decode('utf-8')
            await ws_connection.send(json.dumps({'audio_data': str(data)}))
        except Exception as e:
            print(f'Something went wrong in sending. Error code was {e.code}')

    return True


async def receive_data():
    """
    Asynchronous function used for receiving data
    """

    async with websockets.connect(
            ASSEMBLYAI_ENDPOINT,
            ping_interval=5,
            ping_timeout=40,
            extra_headers=(('Authorization', API_KEY),),
    ) as ws_connection:
        await asyncio.sleep(0.1)
        await ws_connection.recv()
        print('Websocket connection initialised')

        try:
            received_msg = await ws_connection.recv()
            data = json.loads(received_msg)['text']
            print(data)
            GameLoop.gameLoop.smiley.moveLips(data)
        except Exception as e:
            print(f'Something went wrong in recieving. Error code was {e.code}')

    return True