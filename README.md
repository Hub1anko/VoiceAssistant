# VoiceAssistant
## Usage

This VoiceAssistant is designed to seamlessly integrate with Home Assistant, providing voice-controlled functionalities. To get started, follow these simple steps:
## 1. Create Long-Lived Access Tokens in Home Assistant

- Log in to your Home Assistant instance.
- Navigate to your profile page. You can find this by clicking on your profile picture in the top right corner.\
    ![location of profile](https://github.com/Hub1anko/VoiceAssistant/blob/main/img/profile.png)
- Scroll down to the "Long-Lived Access Tokens" section at the bottom of the page.
- Click on "CREATE TOKEN" to generate a new access token.\
    ![location of create token](https://github.com/Hub1anko/VoiceAssistant/blob/main/img/token.png)

## 2. Setup Voice Assistant

After obtaining your access token, you have two options to configure the Voice Assistant:
Option 1: Use the Installer Script

Run the install.py script and follow the on-screen instructions. This script will prompt you to enter the access token generated in the previous step.

```bash

python install.py
```
Option 2: Manual Configuration

Alternatively, you can open the config.yaml file and paste the access token after the "token:" field.

```yaml

token: your_access_token_here
```
## 3. Choose GPU or CPU for Microphone Recognition

If you have an NVIDIA GPU, run the "microphone_recognition_gpu.py" script for optimized performance. Otherwise, use "microphone_recognition.py," which runs on the CPU.

```bash

# For NVIDIA GPU
python3 microphone_recognition_gpu.py

# For CPU
python3 microphone_recognition.py
```
## 4. Configure intents inside Homeassistant. 

The VoiceAssistant script focuses on handling voice recognition and converting spoken words into text, but it leaves the interpretation of these texts to Home Assistant. It is essential to configure specific intents within your Home Assistant instance to determine how recognized sentences are interpreted and acted upon.

This script operates by sending the recognized sentence to Home Assistant, which then handles the intent based on your configurations. To set up custom intents, follow the guidelines provided by Home Assistant at https://www.home-assistant.io/voice_control/custom_sentences.