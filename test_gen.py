from elevenlabs import VoiceSettings

from elevenlabs import set_api_key, generate

set_api_key("gyiu")

audio_data = generate(text="Hello world!", voice="Adam")
