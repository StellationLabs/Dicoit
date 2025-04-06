Dicoit - Voice-Controlled AI Assistant


Dicoit is a Python-based voice-controlled virtual assistant inspired by JARVIS, capable of performing a variety of tasks through natural voice commands.

🚀 Features
🎙️ Voice Interaction: Communicate using natural speech

🌐 Web Automation: Open websites (YouTube, Google, etc.)

🎵 Media Control: Play YouTube videos or songs

📚 Information Retrieval:

Search Wikipedia

Get the current time and date

🎭 Entertainment: Tell random jokes

💬 Conversational: Handle basic questions

📦 Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/Dicoit-AI-Assistant.git
cd Dicoit-AI-Assistant
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Additional Setup (if needed)
Linux:
bash
Copy
Edit
sudo apt-get install portaudio19-dev python3-pyaudio
macOS:
bash
Copy
Edit
brew install portaudio
🧠 Usage
Run the Assistant
bash
Copy
Edit
python dicoit.py
Try These Voice Commands
“Open YouTube”

“Play [song name]”

“What time is it?”

“Tell me a joke”

“Wikipedia search for [topic]”

“What can you do?”

“Goodbye” (to exit)

⚙️ Configuration
Voice Settings
Change the voice in the code:

python
Copy
Edit
# Set index to 0 for male voice, 1 for female
engine.setProperty('voice', voices[1].id)
Language Settings
To adjust for different accents, update the language setting in take_command():

python
Copy
Edit
language = 'en-in'
🧾 Dependencies
Python 3.6+

Core Packages
SpeechRecognition – For processing audio input

pyttsx3 – Text-to-speech conversion

pywhatkit – YouTube integration

wikipedia – Fetches information from Wikipedia

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository

Create a feature branch

bash
Copy
Edit
git checkout -b feature/AmazingFeature
Commit your changes

bash
Copy
Edit
git commit -m 'Add AmazingFeature'
Push to the branch

bash
Copy
Edit
git push origin feature/AmazingFeature
Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

🙌 Acknowledgments
Inspired by JARVIS from Iron Man

Icons by Icons8

Built using Python's powerful AI/ML ecosystem