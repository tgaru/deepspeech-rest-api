import wave
from io import BytesIO
from pathlib import Path

import ffmpeg
import numpy as np
from deepspeech import Model


class SpeechToTextEngine:
    def normalize_audio(self, audio):
        out, err = ffmpeg.input('pipe:0') \
            .output('pipe:1', f='WAV', acodec='pcm_s16le', ac=1, ar='16k', loglevel='error', hide_banner=None) \
            .run(input=audio, capture_stdout=True, capture_stderr=True)
        if err:
            raise Exception(err)
        return out

    def getModelFile(self, lang_key, file_name):
        return Path(__file__).parents[1].joinpath('models').joinpath(lang_key).joinpath(file_name).absolute().as_posix()

    def setLang(self, lang_key):
        self.model = Model(model_path=self.getModelFile(lang_key, 'output_graph.pbmm'))

    def run(self, audio):
        audio = self.normalize_audio(audio)
        audio = BytesIO(audio)
        with wave.Wave_read(audio) as wav:
            audio = np.frombuffer(wav.readframes(wav.getnframes()), np.int16)
        result = self.model.stt(audio_buffer=audio)
        return result
