# HollySpiritEcho

This demo app selects a pair of correlated Old and New Testament passages for the current liturgical year using OpenAI, displays them in the user's preferred language, and provides audio narration using the browser's voice.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Obtain an OpenAI API key and set it in your environment:
   ```bash
   export OPENAI_API_KEY=your_key_here
   ```
   If no API key is provided, placeholder passages will be used.

3. Run the server:
   ```bash
   python app.py
   ```

Visit `http://localhost:5000` in your browser. The app detects your browser language, requests passages in that language, displays them, and lets you play them using text-to-speech.
