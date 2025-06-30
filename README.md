# ElevenLabs Text-to-Speech API Test

This project demonstrates how to use the ElevenLabs Text-to-Speech API to convert text to speech and save the output as an MP3 file.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
   - Copy `.env` to your project directory
   - Replace `your_api_key_here` with your actual ElevenLabs API key
   - Optionally change the default voice ID if desired

3. Run the test:
```bash
python main.py
```

## Features

- Reusable ElevenLabs TTS client implementation
- Environment-based configuration
- Error handling and logging
- Easy to extend with additional voice parameters

## Security Note

- Never commit your `.env` file containing API keys
- The `.env` file is already included in `.gitignore`

## Project Structure

- `main.py`: Entry point that tests the TTS functionality
- `elevenlabs.py`: Contains the ElevenLabs TTS client implementation
- `.env`: Configuration file for API credentials
- `requirements.txt`: Project dependencies
- `.gitignore`: Git ignore rules
# elevenLabstest
