# Dicoit - Voice-Controlled AI Assistant

Dicoit is a Python-based voice-controlled virtual assistant inspired by JARVIS. It can perform various tasks using natural voice commands.

---

## 🚀 Features

- 🎙️ **Voice Interaction**: Communicate using natural speech
- 🌐 **Web Automation**: Open websites like YouTube, Google, etc.
- 🎵 **Media Control**: Play YouTube videos or songs
- 📚 **Information Retrieval**:
  - Search Wikipedia
  - Get the current time and date
- 🎭 **Entertainment**: Hear random jokes
- 💬 **Conversational**: Handles basic Q&A interactions

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/MaheshDhingra/Dicoit.git
cd Dicoit-AI-Assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Additional Setup (if needed)

#### Linux:
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

#### macOS:
```bash
brew install portaudio
```

---

## 🧠 Usage

### Run the Assistant
```bash
python dicoit.py
```

### Try These Voice Commands
- "Open YouTube"
- "Play [song name]"
- "What time is it?"
- "Tell me a joke"
- "Wikipedia search for [topic]"
- "What can you do?"
- "Goodbye" (to exit)

---

## ⚙️ Configuration

### Voice Settings
To change the voice, modify the following in the code:
```python
# Set index to 0 for male voice, 1 for female
engine.setProperty('voice', voices[1].id)
```

### Language Settings
To adjust for different accents, update the language setting in `take_command()`:
```python
language = 'en-in'
```

---

## 🧾 Dependencies

### Requirements
- Python 3.6+

### Core Packages
- `SpeechRecognition` – For processing audio input
- `pyttsx3` – Text-to-speech conversion
- `pywhatkit` – YouTube integration
- `wikipedia` – Fetches information from Wikipedia

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch:
```bash
git checkout -b feature/AmazingFeature
```
3. Commit your changes:
```bash
git commit -m "Add AmazingFeature"
```
4. Push to the branch:
```bash
git push origin feature/AmazingFeature
```
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙌 Acknowledgments

- Inspired by JARVIS from Iron Man
- Icons by [Icons8](https://icons8.com)
- Built using Python's powerful AI/ML ecosystem

