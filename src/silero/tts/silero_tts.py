import os

import torch

from silero.config.audio_config import AudioConfig
from silero.config.device_config import DeviceConfig
from silero.config.model_config import ModelConfig
from silero.config.speaker_config import SpeakerConfig


class SileroTTS:
    def __init__(self):
        self.device = torch.device(DeviceConfig.DEVICE.value)
        self.model = None
        self.model_file = ModelConfig.FILE.value
        self.model_url = ModelConfig.URL.value
        self.sample_rate = SpeakerConfig.SAMPLE_RATE.value
        self.speaker = SpeakerConfig.SPEAKER.value
        torch.set_num_threads(DeviceConfig.THREAD_NUMBER.value)

    def download_model(self):
        if not os.path.isfile(self.model_file):
            torch.hub.download_url_to_file(self.model_url, self.model_file)

    def load_model(self):
        importer = torch.package.PackageImporter(self.model_file)
        self.model = importer.load_pickle("tts_models", "model")
        self.model.to(self.device)

    def generate_audio(self, text):
        sample_rate = self.sample_rate
        save_wav = self.model.save_wav
        speaker = self.speaker

        wav_options = {
            "audio_path": AudioConfig.FILENAME.value,
            "sample_rate": sample_rate,
            "speaker": speaker,
            "text": text
        }

        save_wav(**wav_options)

    def tts(self, text):
        self.download_model()
        self.load_model()
        self.generate_audio(text)
