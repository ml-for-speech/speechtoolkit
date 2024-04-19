from transformers import pipeline
from speechtoolkit.data.languages import language_codes
from speechtoolkit.utils.device import device_map

class WhisperLanguageClassifier:
    def __init__(self, device = 'auto', model='sanchit-gandhi/whisper-base-ft-common-language-id', **kwargs,):
        self.pipe = pipeline('audio-classification', model, device=device_map(device))
    def infer_file(self, file_path):
        result = self.pipe(file_path)[0]['label']
        if result in language_codes.keys():
            return language_codes[result]
        else:
            return result