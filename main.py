from elevenlabs import elevenlabs_tts
import sys

def main():
    # Test text to convert to speech
    test_text = "Experience the power of ElevenLabs' multilingual model! With enhanced naturalness and expressiveness, this model can handle multiple languages and dialects with ease. Let's explore how it can bring your text to life with rich, natural-sounding speech."
    output_file = "output.mp3"
    
    print(f"\nGenerating speech for: '{test_text}'")
    print(f"Output will be saved to: {output_file}")
    
    # Generate speech
    success = elevenlabs_tts.generate_speech(test_text, output_file, model_id='eleven_multilingual_v2')
    
    if success:
        print("\nSpeech generation completed successfully!")
    else:
        print("\nSpeech generation failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
