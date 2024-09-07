from elevenlabs import VoiceSettings

from elevenlabs import set_api_key, generate

set_api_key("d53c9dd6499c7fdca63c14f4348b779c")

audio_data = generate(text="Hello world!", voice="Adam")
