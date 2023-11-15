# VoiceAssistant
## Usage
To use voice assistant you need to create Long-Lived Access Tokens in homeassistant:
- login to homeassistant,
- go to profile,\
  ![alt text](http://url/to/img.png)
- at bottom of the page in section "Long-Lived Access Tokens", "CREATE TOKEN"\
  ![alt text](http://url/to/img.png)


After that run install.py and follow instructions.\
Alternatevely open config.yaml and paste token after "token: ".

If you have NVIDIA gpu run "microphone_recognition_gpu.py" otherwise "micropone_recognition.py" runs on cpu