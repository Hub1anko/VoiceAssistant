# VoiceAssistant
## Usage
To use voice assistant you need to create Long-Lived Access Tokens in homeassistant:
- login to homeassistant,
- go to profile,\
  ![location of profile](https://github.com/Hub1anko/VoiceAssistant/blob/main/img/profile.png)
- at bottom of the page in section "Long-Lived Access Tokens", "CREATE TOKEN"\
  ![location of create token](https://github.com/Hub1anko/VoiceAssistant/blob/main/img/token.png)


After that run install.py and follow instructions.\
Alternatevely open config.yaml and paste token after "token: ".

If you have NVIDIA gpu run "microphone_recognition_gpu.py" otherwise "micropone_recognition.py" runs on cpu
