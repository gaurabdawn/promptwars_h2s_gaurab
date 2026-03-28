from google.cloud import texttospeech

class SetuVoice:
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()

    def speak_summary(self, text):
        """Converts Hinglish summary to Audio bytes for Accessibility"""
        synthesis_input = texttospeech.SynthesisInput(text=text)
        
        # Voice optimized for Indian context (Hindi-India)
        voice = texttospeech.VoiceSelectionParams(
            language_code="hi-IN", 
            ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
        )
        
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        # In a real app, you'd upload this to Cloud Storage and return a URL
        return response.audio_content