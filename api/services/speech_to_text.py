from api.services import *

class SpeechToText:
    def __init__(self, apikey):
        self.client = genai.Client(api_key=apikey)

    def retrieve_script(self, audio_data):
        myfile = self.client.files.upload(file=audio_data, config={"mime_type": "audio/wav"})
        # Gọi model để lấy transcript
        response = self.client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=[
                "Transcribe this audio, return text only.",
                myfile
            ]
        )
        return response.text