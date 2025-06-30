import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ElevenLabsTTS:
    def __init__(self):
        self.api_key = os.getenv('ELEVENLABS_API_KEY')
        self.base_url = 'https://api.elevenlabs.io/v1'
        self.default_voice_id = os.getenv('ELEVENLABS_VOICE_ID', 'u4HtmbcjVZVpiJLQ2GZn')
        
    def generate_speech(self, text: str, output_file: str, voice_id: str = None, model_id: str = None) -> bool:
        """
        Generate speech from text using ElevenLabs API.
        
        Args:
            text (str): Text to convert to speech
            output_file (str): Output file path to save the audio
            voice_id (str, optional): Voice ID to use. Defaults to None (uses default voice)
            model_id (str, optional): Model ID to use. Defaults to None (uses 'eleven_monolingual_v1')
            
        Returns:
            bool: True if successful, False otherwise
        """
        """
        Generate speech from text using ElevenLabs API.
        
        Args:
            text (str): Text to convert to speech
            output_file (str): Output file path to save the audio
            voice_id (str, optional): Voice ID to use. Defaults to None (uses default voice)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.api_key:
            print("Error: ELEVENLABS_API_KEY not found in environment variables")
            return False
            
        if not voice_id:
            voice_id = self.default_voice_id.strip()  # Remove any whitespace
        else:
            voice_id = voice_id.strip()  # Remove any whitespace from custom voice ID
            
        headers = {
            'Accept': 'audio/mpeg',
            'Content-Type': 'application/json',
            'xi-api-key': self.api_key
        }
        
        if not model_id:
            model_id = 'eleven_multilingual_v2'  # Default model
            
        data = {
            'text': text,
            'model_id': model_id,
            'voice_settings': {
                'stability': 0.5,
                'similarity_boost': 0.5
            }
        }
        
        try:
            response = requests.post(
                f'{self.base_url}/text-to-speech/{voice_id}',
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                print(f"Successfully generated speech and saved to {output_file}")
                return True
            else:
                print(f"Error: API request failed with status code {response.status_code}")
                print(f"Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"Error generating speech: {str(e)}")
            return False

# Create an instance for easier use
elevenlabs_tts = ElevenLabsTTS()
