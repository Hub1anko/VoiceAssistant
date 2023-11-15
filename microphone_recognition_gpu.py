#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyaudio
import numpy as np
import time
import os
from playsound import playsound
import wave
from openwakeword import Model
from requests import post
from piper import PiperVoice

recognizer = sr.Recognizer()
wakewordmodel = Model(wakeword_models=['alexa'])

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1280
pyaudio = pyaudio.PyAudio()
mic_stream = pyaudio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
processor_device = 'cuda'

#set delay for activation
cooldown = 3 #seconds
activation_time = 0
hassurl = "http://192.168.1.224:8123"

#send message to home assistant
def postHass(action, data):
	headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIxMjJjODJmMmFjODI0YjM4OWZmNjc3YzUxMTVjNTllMyIsImlhdCI6MTY5MTQyMTk3MCwiZXhwIjoyMDA2NzgxOTcwfQ.oXuUjufQc5tpxpLuZYTV9r0EUpfQ0vKQg5y2oDmEQ0o", "content-type": "application/json"}
	response = post(hassurl + action, headers=headers, json=data)
	response_dict = response.json()
	#print(response_dict)
	#print(response_dict['response']['speech']['plain']['speech'])

	#try to synthesize response
	try:
		response_speech = response_dict['response']['speech']['plain']['speech']
		synthesizeOutput(response_speech)
	except:
		print('no response speech')

#synthesize response using piper
def synthesizeOutput(text):
	voice = PiperVoice.load("voice/en_GB-semaine-medium.onnx")
	with wave.open("voice/output.wav", "wb") as wav_file:
		voice.synthesize(text, wav_file)

while True:
	# Get audio
	audio = np.frombuffer(mic_stream.read(CHUNK), dtype=np.int16)

	prediction = wakewordmodel.predict(audio)
	#print(prediction)
	
	if prediction['alexa_v0.1.tflite'] >= 0.7 and (time.time() - activation_time) >= cooldown:
		playsound('voice/yesmaster.wav')
		
		# obtain audio from the microphone
		with sr.Microphone() as source:
			print("Say something!")
			audio = recognizer.listen(source)

			# recognize speech using whisper
			try:
				response = recognizer.recognize_whisper(audio, language="english", load_options=dict(device=processor_device))
				print("Whisper thinks you said: " + response)
				data = {
					"text": response,
					"language": "en"
					}

				postHass("/api/conversation/process", data)
			except sr.UnknownValueError:
				print("Whisper could not understand audio")
			except sr.RequestError as e:
				print("Could not request results from Whisper")
		#try to play and remove file with response from home assistant
		try:
			playsound('voice/output.wav')
			os.remove('voice/output.wav')
		except:
			playsound('voice/asyouwish.wav')
		#playAudio(sleepresponse)
		activation_time = time.time()


